init python:
    renpy.register_shader("wm.box_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord);

        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            vec2 offset = u_direction == 0.0 ? vec2(i / res0.x, 0.0) : vec2(0.0, i / res0.y);
            col += texture2D(tex0, v_tex_coord + offset);
            col += texture2D(tex0, v_tex_coord - offset);
            sum += 2.0;
        }

        gl_FragColor = col / sum;
    """)

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
        uniform vec3 u_incre_gauss;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec3 incre_gauss = u_incre_gauss;
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
        uniform vec3 u_incre_gauss;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec3 incre_gauss = u_incre_gauss;
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

    renpy.register_shader("wm.kawase_pass", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_iteration;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec4 KawaseBlurFilter( sampler2D tex, vec2 texCoord, vec2 pixelSize, float iteration )
        {
            vec2 texCoordSample;
            vec2 halfPixelSize = pixelSize / 2.0f;
            vec2 dUV = (pixelSize.xy * vec2(iteration)) + halfPixelSize.xy;

            vec4 cOut;

            // Sample top left pixel
            texCoordSample.x = texCoord.x - dUV.x;
            texCoordSample.y = texCoord.y + dUV.y;
            
            cOut = texture2D(tex, texCoordSample);

            // Sample top right pixel
            texCoordSample.x = texCoord.x + dUV.x;
            texCoordSample.y = texCoord.y + dUV.y;

            cOut += texture2D(tex, texCoordSample);

            // Sample bottom right pixel
            texCoordSample.x = texCoord.x + dUV.x;
            texCoordSample.y = texCoord.y - dUV.y;
            cOut += texture2D( tex, texCoordSample );

            // Sample bottom left pixel
            texCoordSample.x = texCoord.x - dUV.x;
            texCoordSample.y = texCoord.y - dUV.y;

            cOut += texture2D(tex, texCoordSample);

            // Average 
            cOut *= 0.25f;
            
            return cOut;
        } 
    """, fragment_200="""
        gl_FragColor = KawaseBlurFilter(tex0, v_tex_coord, 1.0 / res0.xy, u_iteration * 2.0 + 1.0);
    """)