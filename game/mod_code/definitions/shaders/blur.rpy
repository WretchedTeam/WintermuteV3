init python:
    renpy.register_shader("wm.default_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = vec4(0.);
        float renpy_blur_norm = 0.;

        for (float i = -5.; i < 1.; i += 1.) {
            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.));
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor += renpy_blur_norm * texture2D(tex0, v_tex_coord.xy, 0.);

        for (float i = 1.; i < 14.; i += 1.) {

            if (i >= u_renpy_blur_log2 + 5.) {
                break;
            }

            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.));
            gl_FragColor += renpy_blur_weight * texture2D(tex0, v_tex_coord.xy, i);
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor /= renpy_blur_norm;
    """)

    renpy.register_shader("wm.box_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform vec2 u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord);

        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            col += texture2D(tex0, v_tex_coord + u_direction * i / res0.xy);
            col += texture2D(tex0, v_tex_coord + u_direction * i / res0.xy);
            sum += 2.0;
        }

        gl_FragColor = col / sum;
    """)

    renpy.register_shader("wm.weighted_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_lod_bias;
        uniform vec2 res0;

        uniform float u_radius;
        uniform vec2 u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        float calc_weight(float x)
        {
            return pow((cos(x * 3.14) + 1.0) * 0.5, 2.0);
        }
    """, fragment_200="""
        vec4 color = texture2D(tex0, v_tex_coord, u_lod_bias);
        float sum = 1.0;

        for (float i = 1.0; i <= u_radius; i++)
        {
            float weight = calc_weight(i / u_radius);

            color += texture2D(tex0, v_tex_coord + u_direction * i / res0.xy, u_lod_bias) * weight;
            color += texture2D(tex0, v_tex_coord - u_direction * i / res0.xy, u_lod_bias) * weight;

            sum += 2.0 * weight;
        }

        gl_FragColor = color / sum;
    """)

    renpy.register_shader("wm.shadow_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_lod_bias;
        uniform float u_radius;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord);

        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            float weight = 1.0 - i / u_radius;
            vec2 pixel_offset = vec2(i / res0.x, i / res0.y);

            col += texture2D(tex0, v_tex_coord + vec2(pixel_offset.x, 0), u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord - vec2(pixel_offset.x, 0), u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord + vec2(0, pixel_offset.y), u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord - vec2(0, pixel_offset.y), u_lod_bias) * weight;

            sum += 4.0 * weight;
        }

        gl_FragColor = col / sum;
    """)

    renpy.register_shader("wm.gaussian_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_lod_bias;
        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
        uniform vec2 u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord, u_lod_bias);

        float sum = 1.0;

        for (float i=1.0; i <= u_radius; i++) {
            float weight = exp(-i * i / (2.0 * u_sqr_sigma));
            col += texture2D(tex0, v_tex_coord + u_direction * i /res0.xy, u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord - u_direction * i /res0.xy, u_lod_bias) * weight;
            sum += weight * 2.0;
        }

        gl_FragColor = col / sum;
    """)

    renpy.register_shader("wm.gaussian_blur_incre", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_lod_bias;
        uniform float u_radius;
        uniform vec3 u_incre_gauss;
        uniform vec2 u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec3 incre_gauss = u_incre_gauss;
        vec4 col = texture2D(tex0, v_tex_coord) * incre_gauss.x;
        float sum = incre_gauss.x;
        incre_gauss.xy *= incre_gauss.yz;

        for (float i=1.0; i <= u_radius; i++) {
            vec2 offset = vec2(i / res0.x, 0.0);
            col += texture2D(tex0, v_tex_coord + u_direction * i / res0.xy, u_lod_bias) * incre_gauss.x;
            col += texture2D(tex0, v_tex_coord - u_direction * i / res0.xy, u_lod_bias) * incre_gauss.x;
            sum += incre_gauss.x * 2.0;
            incre_gauss.xy *= incre_gauss.yz;
        }
        gl_FragColor = col / sum;
    """)

    renpy.register_shader("wm.kawase_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_lod_bias;
        uniform float u_iteration;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec4 KawaseBlurFilter(sampler2D tex, vec2 texCoord, vec2 pixelSize, float iteration, float u_lod_bias)
        {
            vec2 texCoordSample;
            vec2 halfPixelSize = pixelSize / 2.0f;
            vec2 dUV = (pixelSize.xy * vec2(iteration)) + halfPixelSize.xy;

            vec4 cOut;

            // Sample top left pixel
            texCoordSample.x = texCoord.x - dUV.x;
            texCoordSample.y = texCoord.y + dUV.y;
            
            cOut = texture2D(tex, texCoordSample, u_lod_bias);

            // Sample top right pixel
            texCoordSample.x = texCoord.x + dUV.x;
            texCoordSample.y = texCoord.y + dUV.y;

            cOut += texture2D(tex, texCoordSample, u_lod_bias);

            // Sample bottom right pixel
            texCoordSample.x = texCoord.x + dUV.x;
            texCoordSample.y = texCoord.y - dUV.y;
            cOut += texture2D(tex, texCoordSample, u_lod_bias);

            // Sample bottom left pixel
            texCoordSample.x = texCoord.x - dUV.x;
            texCoordSample.y = texCoord.y - dUV.y;

            cOut += texture2D(tex, texCoordSample, u_lod_bias);

            // Average 
            cOut *= 0.25f;
            
            return cOut;
        } 
    """, fragment_200="""
        gl_FragColor = KawaseBlurFilter(tex0, v_tex_coord, 1.0 / res0.xy, u_iteration, u_lod_bias);
    """)