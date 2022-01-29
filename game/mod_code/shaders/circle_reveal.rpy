init -100 python:
    renpy.register_shader("wm.circle_reveal", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_model_size;
        uniform float u_complete;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        #define NEAREST_CORNER(pos) (1.0 - (step(0.5, pos)))
    """,fragment_200="""
        vec4 color = texture2D(tex0, v_tex_coord);

        vec2 uv2 = v_tex_coord * 500.0;
        uv2.x *= res0.x / res0.y;

        float dist = distance(fract(uv2), vec2(0.5));
        float RADIUS = u_complete;

        float fudge = 0.05;
        float coeff = smoothstep(
            RADIUS * (1.0 - fudge), RADIUS * (1.0 + fudge), dist
        );

        gl_FragColor = mix(vec4(0.0), color, 1.0 - coeff);
    """)

transform circle_reveal(t=10.0, d=0.0):
    mesh True 
    shader "wm.circle_reveal"
    u_complete 0.0
    pause d
    ease t u_complete 1.0