python early in _wm_gaussian:
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

    renpy.register_shader("wm.default_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = vec4(0.);
        float renpy_blur_norm = 0.;

        for (float i = -5.; i < 1.; i += 1.) {
            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.));
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor += renpy_blur_norm * texture2D(tex0, v_tex_coord.xy, 0.);

        for (float i = 1.; i < 14.; i += 1.) {

            if (i >= u_renpy_blur_log2 + 5.) {
                break;
            }

            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.));
            gl_FragColor += renpy_blur_weight * texture2D(tex0, v_tex_coord.xy, i);
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor /= renpy_blur_norm;
    """)

    from renpy.display.accelerator import transform_render
    from math import sqrt, exp, log

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
            cr = render
            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("wm.box_blur")
            render.add_uniform("u_radius", blur)
            render.add_uniform("u_direction", direction)
            render.add_uniform("u_lod_bias", lod)

            return render

        for d in (0.0, 1.0) * passes:
            render = apply_box_blur(render, blur, d)

        return render

    def weighted_blur(render, blur):
        def apply_weighted_blur(render, blur, direction):
            cr = render
            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("wm.weighted_blur")
            render.add_uniform("u_radius", blur)
            render.add_uniform("u_direction", direction)
            render.add_uniform("u_lod_bias", lod)

            return render

        for d in (0.0, 1.0):
            render = apply_weighted_blur(render, blur, d)

        return render

    def gaussian_blur(render, blur, incre=False, lod=gl_lod_bias):
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
            render.add_uniform("u_lod_bias", lod)
            
            return render

        def apply_incre_gaussian_blur(render, s, blur, sigma, sqr_sigma):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader(s)
            render.add_uniform("u_radius", blur)
            render.add_uniform("u_lod_bias", lod)

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

    def kawase_blur(render, blur, lod=gl_lod_bias):
        def apply_kawase_blur(render, i):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("wm.kawase_pass")
            render.add_uniform("u_iteration", i)
            render.add_uniform("u_lod_bias", lod)
            
            return render

        for i in range(int(blur)):
            render = apply_kawase_blur(render, i)

        return render

    def default_blur(render, blur, lod=gl_lod_bias):
        def apply_default_blur(render, i):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("wm.default_blur")
            render.add_uniform("u_renpy_blur_log2", log(i, 2))
            render.add_uniform("u_lod_bias", lod)
            
            return render

        render = apply_default_blur(render, blur)
        return render

    def shadow_blur(render, blur, lod):
        def apply_shadow_blur(render, i):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("wm.shadow_blur")
            render.add_uniform("u_radius", i)
            render.add_uniform("u_lod_bias", lod)
            
            return render

        render = apply_shadow_blur(render, blur)
        return render

    def new_transform_render(self, width, height, st, at):
        rv = transform_render(self, width, height, st, at)

        blur = (self.state.blur or None)

        if blur is not None:
            rv = gaussian_blur(rv, blur, lod=0.0)

        return rv

    renpy.display.transform.Transform.render = new_transform_render