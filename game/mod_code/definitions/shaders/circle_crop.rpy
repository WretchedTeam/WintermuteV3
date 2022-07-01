# Unused.
init -100 python:
    renpy.register_shader("wm.circle_crop", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_model_size;
        uniform vec2 u_center;
        uniform float u_complete;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        #define NEAREST_CORNER(pos) (1.0 - (step(0.5, pos)))
    """,fragment_200="""
        vec4 color = texture2D(tex0, v_tex_coord);
        float max_dist = distance(u_center, NEAREST_CORNER(u_center));

        float coeff = distance(u_center, v_tex_coord);

        coeff = smoothstep(
            max_dist * u_complete * 0.99,
            max_dist * u_complete * 1.01, 
            coeff
        );

        gl_FragColor = mix(color, vec4(0.0), coeff);
    """)

transform circle_crop(start=(0.0, 0.0), d=10.0):
    on show:
        mesh True 
        shader "wm.circle_crop"
        u_center start
        u_complete 0.0
        ease d u_complete 2.5