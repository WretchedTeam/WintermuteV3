init python:
    # Requires a specific fontmap from ShaderToy, 
    # the text function is hardcoded for that map.

    renpy.register_shader("wm.matrix",  variables="""
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        uniform float u_time;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        const float tilesize = 16.0;
        const vec3 green = vec3(0.0, 1.0, 0.0);

        float random(vec2 st) {
            return fract(sin(dot(st.xy,vec2(12.9898,78.233))) * 43758.5453123);
        }

        float text(sampler2D tex0, vec2 uv, vec2 r, float time) {
            vec2 uv1 = mod(uv.xy, tilesize) * 0.0625;
            vec2 block = uv * 0.0625 - uv1;
            uv1 += floor((random(block / r.xy) + time * 0.1) * tilesize);
            uv1 = mod(uv1, tilesize);
            return texture2D(tex0, uv1 * 0.0625).r;
        }

        float rain(vec2 uv, vec2 r, float time) {
            uv -= mod(uv, tilesize);
            float offset = sin(uv.x * 10.0);
            float y = fract(-uv.y / r.y + offset + 0.25 * time);
            return clamp(0.0, 1.0, 1.0 / (y * 20.0));
        }
    """,fragment_200="""
        float text = text(tex0, gl_FragCoord.xy, res0, u_time);
        float rain = rain(gl_FragCoord.xy, u_model_size, u_time);
        gl_FragColor = vec4(vec3(text * rain), 1.0);
    """
    )