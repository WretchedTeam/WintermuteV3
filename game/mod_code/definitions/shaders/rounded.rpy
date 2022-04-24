init -100 python:
    renpy.register_shader("wm.rounded_corners", variables="""
        uniform float u_radius;
        uniform float u_outline_width;
        uniform vec4 u_outline_color;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_resolution;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
    """, fragment_200="""
        vec2 center = u_resolution.xy / 2.0;
        vec2 uv = v_tex_coord.xy * u_resolution.xy;
        vec2 center_outline = center - u_outline_width;

        // https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm
        #define ROUNDED_RECT(p, b, r) (length(max(abs(p) - b + r, 0.0)) - r)

        float crop1 = ROUNDED_RECT(uv - center, center, u_radius);
        float crop2 = ROUNDED_RECT(uv - center, center_outline, u_radius);

        vec4 color = texture2D(tex0, v_tex_coord);

        float coeff1 = smoothstep(1.0, -1.0, crop1);
        float coeff2 = smoothstep(1.0, -1.0, crop2);

        float outline_coeff = (coeff1 - coeff2);
        gl_FragColor = mix(vec4(0.0), mix(color, u_outline_color, outline_coeff), coeff1);
    """)

    renpy.register_shader("wm.rounded_corners_normalized", variables="""
        uniform float u_radius;
        uniform float u_outline_width;
        uniform vec4 u_outline_color;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_resolution;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
    """, fragment_200="""
        float aspect = u_resolution.x / u_resolution.y;
        vec2 center = vec2(0.5);
        vec2 uv = v_tex_coord.xy;

        uv.x *= aspect;
        center.x *= aspect;

        vec2 center_outline = center - u_outline_width;

        // https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm
        #define ROUNDED_RECT(p, b, r) (length(max(abs(p) - b + r, 0.0)) - r)

        float crop1 = ROUNDED_RECT(uv - center, center, u_radius);
        float crop2 = ROUNDED_RECT(uv - center, center_outline, u_radius);

        vec4 color = texture2D(tex0, v_tex_coord);

        float coeff1 = smoothstep(0.001, -0.001, crop1);
        float coeff2 = smoothstep(0.001, -0.001, crop2);

        float outline_coeff = (coeff1 - coeff2);
        gl_FragColor = mix(vec4(0.0), mix(color, u_outline_color, outline_coeff), coeff1);
    """)