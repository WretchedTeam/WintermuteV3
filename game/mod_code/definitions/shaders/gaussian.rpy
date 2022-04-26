init python:
    # Normal gaussian
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
        #define E 2.7183

        if (u_radius != 0.0) {
            vec4 col = vec4(0.0);

            for (float offset=0.0; offset <= u_radius; offset++) {
                // float weight = exp(-(offset * offset) / (2.0 * u_sqr_sigma));
                float weight = pow(E, -(offset * offset) / (2.0 * u_sqr_sigma));
                vec2 uv_offset = vec2(offset / res0.x, 0.0);
                col += texture2D(tex0, v_tex_coord + uv_offset) * weight;
                col += texture2D(tex0, v_tex_coord - uv_offset) * weight;
            }

            gl_FragColor = col * u_norm_coeff;
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
        #define E 2.7183

        if (u_radius != 0.0) {
            vec4 col = vec4(0.0);

            for (float offset=0.0; offset <= u_radius; offset++) {
                // float weight = exp(-(offset * offset) / (2.0 * u_sqr_sigma));
                float weight = pow(E, -(offset * offset) / (2.0 * u_sqr_sigma));
                vec2 uv_offset = vec2(0.0, offset / res0.y);
                col += texture2D(tex0, v_tex_coord + uv_offset) * weight;
                col += texture2D(tex0, v_tex_coord - uv_offset) * weight;
            }

            gl_FragColor = col * u_norm_coeff;
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord);
        }
    """)