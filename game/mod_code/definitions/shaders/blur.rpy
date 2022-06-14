# Types of Blurs
# --------------
#
# Default "Blur" (wm.default_blur)
# --------------------------------
# The default weird ass low quality blur/level-of-detail hack which RenPy ships with.
#
# Box Blur (wm.box_blur)
# ----------------------
# It's an actual convolution blur with all the kernel values set to 1 (each pixel 
# within the radius has constant weight). Even has the weird artifacts which are 
# characteristic for a box blur.
#
# Weighted Blur (wm.weighted_blur)
# --------------------------------
# Convolution blur with a kernel calculated using a cosine curve and the distance
# from the origin pixel.
#
# The curve equation is `((cos(x * 3.14) + 1.0) * 0.5) ^ 2` or 
# `cos^2(x * 3.14 * 0.5) ^ 2` where `x` is the pixel offset divided by the radius.
#
# This was made to be used instead of `wm.gaussian_blur`, but there wasn't much 
# of a difference in performance between the two, with the gaussian being faster
# in some cases on my MBP.
#
# "Shadow" Blur (wm.shadow_blur)
# ------------------------------
# Blur which just samples the edges and uses LOD to fill in the gaps. 
# Just used for the drop shadow where quality isn't a main priority (Thus the 
# shader name).
#
# Gaussian Blur (wm.gaussian_blur)
# --------------------------------
# Convolution blur with a kernel calculated using the gaussian function. Sigma is 
# taken to be half the radius.
#
# Gaussian Blur with Incremental Gaussian Computation (wm.gaussian_blur_incre):
# Same as `wm.gaussian_blur` but instead of performing a exponential function
# for each sample, it uses a polynomial approximation which just needs a vector
# multiplication per sample.
#
# Not much performance difference here either (on my MBP).
#
# Refer:
# https://developer.nvidia.com/gpugems/gpugems3/part-vi-gpu-computing/chapter-40-incremental-computation-gaussian
#
# Kawase Blur (wm.kawase_blur)
# ----------------------------
# Multipass blur which samples the corners at increasing distance per pass 
# and averages them to produce a effect identical to a gaussian blur.
#
# Refer:
# https://community.arm.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-20-66/siggraph2015_2D00_mmg_2D00_marius_2D00_notes.pdf
# https://www.intel.com/content/www/us/en/developer/articles/technical/an-investigation-of-fast-real-time-gpu-based-image-blur-algorithms.html

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