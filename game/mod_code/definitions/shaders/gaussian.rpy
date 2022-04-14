init python:
    renpy.register_shader("wm.gaussian_hpass", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_radius;
        uniform float u_norm_coeff;
        uniform float u_sqr_sigma;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec4 blur_h(sampler2D tex0, vec2 uv, vec2 res0, float radius, float norm_coeff, float sqr_sigma)
        {
            vec4 col = vec4(0.0);
            float sum = 0.0;
            for (float offset=-radius; offset <= radius; offset++) {
                float weight = norm_coeff * exp(-(offset * offset) / (2.0 * sqr_sigma));
                vec2 uv2 = uv + vec2(offset / res0.x, 0.0);
                col += texture2D(tex0, uv2) * weight;
                sum += weight;
            }
            return col / sum;
        }
    """, fragment_200="""
        gl_FragColor = blur_h(tex0, v_tex_coord, res0, u_radius, u_norm_coeff, u_sqr_sigma);
    """)

    renpy.register_shader("wm.gaussian_vpass", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_radius;
        uniform float u_norm_coeff;
        uniform float u_sqr_sigma;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec4 blur_v(sampler2D tex0, vec2 uv, vec2 res0, float radius, float norm_coeff, float sqr_sigma)
        {
            vec4 col = vec4(0.0);
            float sum = 0.0;
            for (float offset=-radius; offset <= radius; offset++) {
                float weight = norm_coeff * exp(-(offset * offset) / (2.0 * sqr_sigma));
                vec2 uv2 = uv + vec2(0.0, offset / res0.y);
                col += texture2D(tex0, uv2) * weight;
                sum += weight;
            }
            return col / sum;
        }
    """, fragment_200="""
        gl_FragColor = blur_v(tex0, v_tex_coord, res0, u_radius, u_norm_coeff, u_sqr_sigma);
    """)