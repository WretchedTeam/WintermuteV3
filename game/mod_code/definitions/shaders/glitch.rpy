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


    renpy.register_shader("wm.terminal", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_time;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        float rand(vec2 n) { 
            return fract(sin(dot(n, vec2(12.9, 78.2))) * 437.5);
        }
    """, fragment_200="""
        vec2 uv = v_tex_coord.xy;
        vec2 onepixel = 1.0 / res0.xy;
        vec4 color = texture2D(tex0, uv);

        color.r += texture2D(tex0, uv + vec2(onepixel.x, 0.0)).r;
        color.g += texture2D(tex0, uv - vec2(onepixel.x, 0.0)).g;

        color.rg *= 0.5;

        float scanliney = abs(sin(uv.y * res0.y / 1.5) * 0.5);
        float grey = dot(color.rgb, vec3(0.299, 0.587, 0.114));
        color.rgb = mix(vec3(grey), color.rgb, 0.85);
        color.rgb += rand(uv + u_time) * 0.3;

        gl_FragColor = mix(color, vec4(0.0), scanliney) * color.a;
    """)

transform -10 wm_scanlines():
    mesh True
    shader "wm.scanlines"
    repeat

# transform -10 wm_terminal_effect():
#     mesh True
#     shader "wm.terminal"
#     linear 10.0 alpha 1.0
#     gl_pixel_perfect True
#     repeat

transform -10 wm_terminal_effect(child):
    contains:
        child
        blur 16.0 alpha 5.0
        mesh True
        shader "wm.terminal"

    contains:
        child
        mesh True
        shader "wm.terminal"
