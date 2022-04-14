init python:
    renpy.register_shader("wm.antifisheye", variables="""
        uniform float u_time;
        uniform vec2 res0;
        uniform sampler2D tex0;

        uniform float u_value;

    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300="""
        vec2 p = v_tex_coord.xy;
                                                            
        float prop = 1.0;
        vec2 m = vec2(0.5, 0.5 / prop);
        vec2 d = p - m;
        float r = sqrt(dot(d, d));

        float power = ( 2.0 * 3.141592 / (2.0 * sqrt(dot(m, m))) ) * u_value;

        float bind;
        if (prop < 1.0) bind = m.x; 
        else bind = m.y;

        vec2 uv;
        if (power > 0.0)
            uv = m + normalize(d) * atan(r * -power * 10.0) * bind / atan(-power * bind * 10.0);
        else uv = p;
                                                        
        gl_FragColor = texture2D(tex0, vec2(uv.x, uv.y));
    """)