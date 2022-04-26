python early:
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
    from math import sqrt

    def new_transform_render(self, width, height, st, at):
        rv = transform_render(self, width, height, st, at)

        def gaussian_blur(render, blur):

            def apply_gaussian_blur(render, s, blur, sqr_sigma, norm_coeff):
                cr = render

                render = renpy.Render(*cr.get_size())
                render.mesh = True
                render.blit(cr, (0, 0))
                render.add_shader("-renpy.texture")

                render.add_shader(s)
                render.add_uniform("u_radius", blur)
                render.add_uniform("u_sqr_sigma", sqr_sigma)
                
                render.add_uniform("u_norm_coeff", norm_coeff)

                return render

            sigma = blur / 2.0
            sqr_sigma = sigma ** 2
            norm_coeff = 1.0 / sqrt(2.0 * 3.14 * sqr_sigma)

            shaders = [ "wm.gaussian_h", "wm.gaussian_v" ]
            for s in shaders:
                render = apply_gaussian_blur(render, s, blur, sqr_sigma, norm_coeff)

            return render

        blur = (self.state.blur or None)

        if blur is not None:
            rv = gaussian_blur(rv, blur)

        return rv

    renpy.display.transform.Transform.render = new_transform_render