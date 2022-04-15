python early:
    renpy.register_shader("wm.gaussian_h", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_sqr_sigma;
        uniform float u_norm_coeff;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        if (u_radius != 0.0) {
            vec4 col = vec4(0.0);
            float sum = 0.0;


            for (float offset=-u_radius; offset <= u_radius; offset++) {
                float weight = u_norm_coeff * exp(-(offset * offset) / (2.0 * u_sqr_sigma));
                vec2 uv_offset = vec2(offset / res0.x, 0.0);
                col += texture2D(tex0, v_tex_coord + uv_offset, 1.5) * weight;
                sum += weight;
            }

            gl_FragColor = col / sum;
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord);
        }
    """)

    renpy.register_shader("wm.gaussian_v", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_sqr_sigma;
        uniform float u_norm_coeff;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        if (u_radius != 0.0) {
            vec4 col = vec4(0.0);
            float sum = 0.0;


            for (float offset=-u_radius; offset <= u_radius; offset++) {
                float weight = u_norm_coeff * exp(-(offset * offset) / (2.0 * u_sqr_sigma));
                vec2 uv_offset = vec2(0.0, offset / res0.x);
                col += texture2D(tex0, v_tex_coord + uv_offset, 1.5) * weight;
                sum += weight;
            }

            gl_FragColor = col / sum;
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord);
        }
    """)

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

    renpy.register_shader("emr.renpy_blur", variables="""
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
    from math import pow, sqrt, log

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

            sqr_sigma = pow(blur / 2.0, 2.0)
            norm_coeff = 1.0 / sqrt(2.0 * 3.14 * sqr_sigma)

            for s in [ "wm.gaussian_h", "wm.gaussian_v" ]:
                render = apply_gaussian_blur(render, s, blur, sqr_sigma, norm_coeff)

            return render

        def renpy_blur(render, blur):
            cr = render

            render = renpy.Render(*cr.get_size())
            render.mesh = True
            render.blit(cr, (0, 0))
            render.add_shader("-renpy.texture")

            render.add_shader("emr.renpy_blur")
            render.add_uniform("u_renpy_blur_log2", log(blur, 2))
            return render

        blur = (self.state.blur or None)

        if blur is not None:
            rv = gaussian_blur(rv, blur)

        return rv

    renpy.display.transform.Transform.render = new_transform_render