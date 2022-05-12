init python:
    renpy.register_shader("wm.gradient", variables="""
        uniform float u_theta;
        uniform float u_start_pos;
        uniform float u_end_pos;
        uniform vec4 u_start_color;
        uniform vec4 u_end_color;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        mat2 rotate_matrix(float x) {
            return mat2(
                cos(radians(x)), -sin(radians(x)),
                sin(radians(x)), cos(radians(x))
            );
        }

        float map(float value, float min1, float max1, float min2, float max2) {
            return min2 + (value - min1) * (max2 - min2) / (max1 - min1);
        }
    """, fragment_200="""
        vec2 uv = v_tex_coord.xy * 2.0 - 1.0;
        uv *= rotate_matrix(u_theta);
        uv = (uv + 1.0) / 2.0;

        float coeff = clamp(uv.x, 0.0, 1.0);
        coeff = map(coeff, u_start_pos, u_end_pos, 0.0, 1.0);
        gl_FragColor = mix(u_start_color, u_end_color, clamp(coeff, 0.0, 1.0));
    """)