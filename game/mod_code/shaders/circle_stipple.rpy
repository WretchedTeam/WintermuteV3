init -100 python:
    renpy.register_shader("wm.circle_reveal", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_model_size;
        uniform float u_complete;
        uniform float u_amount;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        #define NEAREST_CORNER(pos) (1.0 - (step(0.5, pos)))
    """,fragment_200="""
        vec2 uv2 = v_tex_coord * u_amount;
        uv2.x *= res0.x / res0.y;

        float dist = distance(fract(uv2), vec2(0.5));
        float RADIUS = u_complete;

        float fudge = 0.05;
        float coeff = smoothstep(
            RADIUS * (1.0 - fudge), RADIUS * (1.0 + fudge), dist
        );

        gl_FragColor = mix(texture2D(tex0, v_tex_coord), texture2D(tex1, v_tex_coord), 1.0 - coeff);
    """)
