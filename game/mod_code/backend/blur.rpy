python early in _wm_blur_funcs:
    from renpy.config import gl_lod_bias
    # Override renpy's default blur
    renpy.register_shader("renpy.blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = texture2D(tex0, v_tex_coord);
    """)

    from math import sqrt, exp, log

    def new_render(crend, shader):
        rv = renpy.Render(*crend.get_size())
        rv.mesh = True
        rv.blit(crend, (0, 0))
        rv.shaders = None
        rv.add_shader(shader)
        return rv

    def zoom_render(crend, factor):
        w, h = crend.get_size()
        zw, zh = w * factor, h * factor 

        rv = renpy.display.render.Render(zw, zh)

        if zw == 0 or zh == 0 or w == 0 or h == 0:
            return rv

        rv.forward = renpy.display.render.Matrix2D(1.0 / factor, 0, 0, 1.0 / factor)
        rv.reverse = renpy.display.render.Matrix2D(factor, 0, 0, factor)

        rv.xclipping = True
        rv.yclipping = True

        rv.blit(crend, (0, 0))

        return rv

    def box_blur(render, blur, passes, lod=gl_lod_bias):
        def apply_box_blur(render, blur, direction):
            render = new_render(render, "wm.box_blur")
            add_uniform = render.add_uniform
            
            add_uniform("u_radius", blur)
            add_uniform("u_direction", direction)
            add_uniform("u_lod_bias", lod)

            return render

        for d in range(int(passes)):
            render = apply_box_blur(render, blur, (0.0, 1.0))
            render = apply_box_blur(render, blur, (1.0, 0.0))

        return render

    def weighted_blur(render, blur, lod=gl_lod_bias):
        def apply_weighted_blur(render, blur, direction):
            render = new_render(render, "wm.weighted_blur")
            add_uniform = render.add_uniform

            add_uniform("u_radius", blur)
            add_uniform("u_direction", direction)
            add_uniform("u_lod_bias", lod)

            return render

        render = apply_weighted_blur(render, blur, (0.0, 1.0))
        render = apply_weighted_blur(render, blur, (1.0, 0.0))

        return render

    def gaussian_blur(render, blur, incre=False, lod=gl_lod_bias):
        RECI_SQRT_2PI = 1.0 / 2.50662827463

        def apply_gaussian_blur(render, blur, direction, incre=False):
            sigma = blur / 2.0
            shader = "wm.gaussian_blur_incre" if incre else "wm.gaussian_blur"

            render = new_render(render, shader)
            add_uniform = render.add_uniform

            add_uniform("u_radius", blur)
            add_uniform("u_lod_bias", lod)
            add_uniform("u_direction", direction)

            if incre:
                ycomp = exp(-0.5 / (sigma * sigma))

                incre_gauss = (
                    RECI_SQRT_2PI / sigma,
                    ycomp,
                    ycomp * ycomp
                )

                add_uniform("u_incre_gauss", incre_gauss)

            else:
                add_uniform("u_sigma", sigma)
                add_uniform("u_sqr_sigma", sigma * sigma)

            return render

        render = apply_gaussian_blur(render, blur, (0.0, 1.0), incre)
        render = apply_gaussian_blur(render, blur, (1.0, 0.0), incre)

        return render

    def kawase_blur(render, passes, lod=gl_lod_bias):
        def apply_kawase_blur(render, i):
            render = new_render(render, "wm.kawase_blur")
            add_uniform = render.add_uniform

            add_uniform("u_iteration", i)
            add_uniform("u_lod_bias", lod)
            
            return render

        for i in range(int(passes)):
            render = apply_kawase_blur(render, i)

        return render

    def default_blur(render, blur, lod=gl_lod_bias):
        def apply_default_blur(render, i):
            render = new_render(render, "wm.default_blur")
            add_uniform = render.add_uniform

            add_uniform("u_renpy_blur_log2", log(i, 2))
            add_uniform("u_lod_bias", lod)
            
            return render

        render = apply_default_blur(render, blur)
        return render

    def shadow_blur(render, blur, lod):
        def apply_shadow_blur(render, i):
            render = new_render(render, "wm.shadow_blur")
            add_uniform = render.add_uniform

            add_uniform("u_radius", i)
            add_uniform("u_lod_bias", lod)
            
            return render

        render = apply_shadow_blur(render, blur)
        return render

python early in _wm_replace_transform_blur:
    from store._wm_blur_funcs import gaussian_blur
    from renpy.display.accelerator import transform_render

    def new_transform_render(self, width, height, st, at):
        rv = transform_render(self, width, height, st, at)

        blur = (self.state.blur or None)

        if blur is not None:
            rv = gaussian_blur(rv, blur, lod=0.5)

        return rv

    renpy.display.transform.Transform.render = new_transform_render