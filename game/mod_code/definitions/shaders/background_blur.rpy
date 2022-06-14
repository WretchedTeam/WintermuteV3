init python:
    renpy.register_shader("wm.kawase_background", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;

        uniform float u_lod_bias;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform vec2 res0;
        uniform vec2 res1;
        uniform float u_iteration;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec4 kawase_pass(sampler2D tex, vec2 uv, vec2 pixel_size, float iteration, float u_lod_bias)
        {
            vec2 off = (pixel_size.xy * vec2(iteration + 0.5));

            vec4 color = texture2D(tex, uv + vec2(-off.x, off.y), u_lod_bias); // Sample top left pixel
            color += texture2D(tex, uv + off, u_lod_bias); // Sample top right pixel
            color += texture2D(tex, uv + vec2(off.x, -off.y), u_lod_bias); // Sample bottom right pixel
            color += texture2D(tex, uv - off, u_lod_bias); // Sample bottom left pixel

            color *= 0.25; // Average 
            
            return color;
        } 
    """, fragment_200="""
        vec4 foreground = texture2D(tex1, v_tex_coord);
        if (foreground.a == 0.0) discard;

        vec4 background = kawase_pass(tex0, v_tex_coord, 1.0 / res0, u_iteration * 2.0, u_lod_bias);
        gl_FragColor = mix(background, foreground, foreground.a);
    """)