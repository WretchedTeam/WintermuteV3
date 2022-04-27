init python:
    # Normal gaussian
    renpy.register_shader("wm.gaussian_h", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord);
        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            float weight = exp(-i * i / (2.0 * u_sqr_sigma));
            vec2 offset = vec2(i / res0.x, 0.0);
            col += texture2D(tex0, v_tex_coord + offset) * weight;
            col += texture2D(tex0, v_tex_coord - offset) * weight;
            sum += weight * 2.0;
        }

        gl_FragColor = col / sum;
    """)

    renpy.register_shader("wm.gaussian_v", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord);
        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            float weight = exp(-i * i / (2.0 * u_sqr_sigma));
            vec2 offset = vec2(0.0, i / res0.y);
            col += texture2D(tex0, v_tex_coord + offset) * weight;
            col += texture2D(tex0, v_tex_coord - offset) * weight;
            sum += weight * 2.0;
        }

        gl_FragColor = col / sum;
    """)

    # Incremental Gaussian
    renpy.register_shader("wm.gaussian_incre_h", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec3 incre_gauss;
        incre_gauss.x = 1.0 / (sqrt(2.0 * 3.14) * u_sigma);
        incre_gauss.y = exp(-0.5 / u_sqr_sigma);
        incre_gauss.z = incre_gauss.y * incre_gauss.y;

        vec4 col = texture2D(tex0, v_tex_coord) * incre_gauss.x;
        float sum = incre_gauss.x;
        incre_gauss.xy *= incre_gauss.yz;

        for (float i=1.0; i <= u_radius; i++) {
            vec2 offset = vec2(i / res0.x, 0.0);
            col += texture2D(tex0, v_tex_coord + offset) * incre_gauss.x;
            col += texture2D(tex0, v_tex_coord - offset) * incre_gauss.x;
            sum += incre_gauss.x * 2.0;
            incre_gauss.xy *= incre_gauss.yz;
        }
        gl_FragColor = col / sum;
    """)

    renpy.register_shader("wm.gaussian_incre_v", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec3 incre_gauss;
        incre_gauss.x = 1.0 / (sqrt(2.0 * 3.14) * u_sigma);
        incre_gauss.y = exp(-0.5 / u_sqr_sigma);
        incre_gauss.z = incre_gauss.y * incre_gauss.y;

        vec4 col = texture2D(tex0, v_tex_coord) * incre_gauss.x;
        float sum = incre_gauss.x;
        incre_gauss.xy *= incre_gauss.yz;

        for (float i=1.0; i <= u_radius; i++) {
            vec2 offset = vec2(0.0, i / res0.y);
            col += texture2D(tex0, v_tex_coord + offset) * incre_gauss.x;
            col += texture2D(tex0, v_tex_coord - offset) * incre_gauss.x;
            sum += incre_gauss.x * 2.0;
            incre_gauss.xy *= incre_gauss.yz;
        }
        gl_FragColor = col / sum;
    """)