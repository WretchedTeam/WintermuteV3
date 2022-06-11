python early in _wm_gaussian:
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

    from renpy.display.accelerator import transform_render
    from math import sqrt, exp

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

    def box_blur(render, blur, passes):
        def apply_box_blur(render, blur, direction):
            cr = render
            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("wm.box_blur")
            render.add_uniform("u_radius", blur)
            render.add_uniform("u_direction", direction)

            return render

        for d in (0.0, 1.0) * passes:
            render = apply_box_blur(render, blur, d)

        return render

    def gaussian_blur(render, blur, incre=False):
        def apply_gaussian_blur(render, s, blur, sigma, sqr_sigma):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader(s)
            render.add_uniform("u_radius", blur)
            render.add_uniform("u_sigma", sigma)
            render.add_uniform("u_sqr_sigma", sqr_sigma)
            
            return render

        def apply_incre_gaussian_blur(render, s, blur, sigma, sqr_sigma):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader(s)
            render.add_uniform("u_radius", blur)

            ycomp = exp(-0.5 / sqr_sigma)
            incre_gauss = (
                1.0 / (sqrt(2.0 * 3.14) * sigma),
                ycomp,
                ycomp * ycomp
            )

            render.add_uniform("u_incre_gauss", incre_gauss)
            
            return render

        sigma = blur / 3.0
        sqr_sigma = sigma ** 2

        if incre:
            for s in ("wm.gaussian_incre_h", "wm.gaussian_incre_v"):
                render = apply_incre_gaussian_blur(render, s, blur, sigma, sqr_sigma)

        else:
            for s in ("wm.gaussian_h", "wm.gaussian_v"):
                render = apply_gaussian_blur(render, s, blur, sigma, sqr_sigma)

        return render

    def new_transform_render(self, width, height, st, at):
        rv = transform_render(self, width, height, st, at)

        blur = (self.state.blur or None)

        if blur is not None:
            rv = gaussian_blur(rv, blur)

        return rv

    renpy.display.transform.Transform.render = new_transform_render