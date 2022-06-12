init python:
    renpy.register_shader("wm.kawase_background", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;

        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform vec2 res0;
        uniform vec2 res1;
        uniform float u_iteration;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        vec4 KawaseBlurFilter(sampler2D tex, vec2 texCoord, vec2 pixelSize, float iteration)
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
            cOut += texture2D( tex, texCoordSample);

            // Sample bottom left pixel
            texCoordSample.x = texCoord.x - dUV.x;
            texCoordSample.y = texCoord.y - dUV.y;

            cOut += texture2D(tex, texCoordSample);

            // Average 
            cOut *= 0.25;
            
            return cOut;
        } 
    """, fragment_200="""
        vec4 foreground = texture2D(tex1, v_tex_coord);
        if (foreground.a == 0.0) discard;

        vec4 background = KawaseBlurFilter(tex0, v_tex_coord, 1.0 / res0, u_iteration * 2.0 + 1.0);
        gl_FragColor = mix(background, foreground, foreground.a);
    """)