# Shader code for an Anti-Fisheye effect which  I ripped 
# off Q's dumb ass (ily)

# `wm.antifisheye` is Q's unmodified one.
# `wm.antifisheye_transition` is a modified version to
# serve as a transition.

init python:
    renpy.register_shader("wm.antifisheye", variables="""
        uniform sampler2D tex0;
        uniform float u_value;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
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
        if (power > 0.0) uv = m + normalize(d) * atan(r * -power * 10.0) * bind / atan(-power * bind * 10.0);
        else uv = p;
                                                        
        gl_FragColor = texture2D(tex0, uv);
    """)

    renpy.register_shader("wm.antifisheye_transition", variables="""
        uniform float u_lod_bias;
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_complete;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec2 fisheye(vec2 p, float val) {
            vec2 m = vec2(0.5, 0.5);
            vec2 d = p - m;
            float r = length(d);
            float power = (2.0 * 3.141592) / (2.0 * length(m)) * val;
            float bind = 0.5;
            vec2 uv = m + normalize(d) * atan(r * -power * 10.0) * bind / atan(-power * bind * 10.0);
            return power > 0.0 ? uv : p;
        }

        vec2 zoom(vec2 uv, float zoom) {
            mat2 zoom_mat = mat2(1.0 / zoom, 0, 0, 1.0 / zoom);
            return (uv - 0.5) * zoom_mat + 0.5;
        }
    """, fragment_300="""
        vec2 p = v_tex_coord;
        float fisheye1 = 0.06 * u_complete;
        float fisheye2 = 0.06 - fisheye1;
        
        float zoom1 = 1.0 + (1.4 - 1.0) * u_complete;
        float zoom2 = 1.4 + (1.0 - 1.4) * u_complete;

        vec4 color1 = texture2D(tex0, fisheye(zoom(p, zoom1), fisheye1));
        vec4 color2 = texture2D(tex1, fisheye(zoom(p, zoom2), fisheye2));

        gl_FragColor = mix(color1, color2, u_complete);
    """)