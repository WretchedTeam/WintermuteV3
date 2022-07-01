# Unused.
# `wm.reload_glitch` is from Q.

init python:
    renpy.register_shader("wm.reload_glitch", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec4 u_random;
        uniform float u_time;
        uniform float u_amt;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        float rand(vec2 n) { 
            return fract(sin(dot(vec2(n.y), vec2(12.9, 78.2))) * 437.5);
        }
    """, fragment_300="""
        vec2 uv = v_tex_coord;
        uv.x += 0.01 * u_amt * rand(uv + u_time);
        gl_FragColor = texture2D(tex0, uv) - rand(uv);
    """)

    renpy.register_shader("wm.scanlines", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_time;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        float rand(vec2 n) { 
            return fract(sin(dot(n, vec2(12.9898, 4.1414))) * 43758.5453);
        }
    """, fragment_200="""
        vec2 st = v_tex_coord;
        vec4 color = texture2D(tex0, st);

        float count = res0.y * 1.0;
        float val = (st.y + u_time * 0.005);
        vec2 scanlineCoords = vec2(sin(val * count), cos(val * count));
        vec3 scanlines = vec3(scanlineCoords.x, scanlineCoords.x, scanlineCoords.x);

        color.rgb -= (scanlines * 0.1);
        color.rgb -= rand(st + u_time * 0.005) * 0.1;

        color.rgb *= color.a;

        gl_FragColor = color;
    """)

transform -10 wm_scanlines():
    mesh True
    shader "wm.scanlines"
    linear 10.0 alpha 1.0
    repeat
    