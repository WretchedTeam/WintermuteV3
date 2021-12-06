init python:
    renpy.register_shader("wm.genie", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_complete;
        uniform vec2 u_pos;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        #define IN_BOUNDS(v, mi, mx) ((v < mx && v > mi))

        vec4 color(sampler2D tex0, vec2 uv)
        {
            if (IN_BOUNDS(uv.x, 0.0, 1.0) && IN_BOUNDS(uv.y, 0.0, 1.0))
                return texture2D(tex0, uv);

            return vec4(0.0);
        }
    """, fragment_200="""
        vec2 uv2 = v_tex_coord + normalize(v_tex_coord - u_pos) * (u_complete * 1.5);
        gl_FragColor = color(tex0, uv2);
    """)

transform genie_shader_test():
    mesh True shader "wm.genie"

    u_pos (0.0, 1.0)
    u_complete 0.0
    easein 2.0 u_complete 1.0 