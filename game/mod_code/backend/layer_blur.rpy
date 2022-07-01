# To keep track of blur transforms used an entire layer.

init 10 python in _wm_layer_blur:
    from store import Function, SetDict, easein_blur, easeout_blur

    layer_keys = None
    layer_blur_radius = None 

    @renpy.config.start_callbacks.append
    def __set_blurred_layers():
        global layer_keys, layer_blur_radius
        layer_keys = dict.fromkeys(renpy.config.layers, None)
        layer_blur_radius = dict.fromkeys(renpy.config.layers, None)

    def ApplyBlur(key, blur, layers):
        """
        Applies blur to the given layers and keeps track of the key 
        and layers.

        `key`
            Unique key to store values for the blur.

        `blur`
            Intensity of the blur.

        `layers`
            List of layers to be blurred.
        """
        layers = [ l for l in layers if layer_keys[l] is None ]

        return [ 
            [ Function(renpy.show_layer_at, easein_blur(blur), l) for l in layers ],
            [ SetDict(layer_keys, l, key) for l in layers ],
            [ SetDict(layer_blur_radius, l, blur) for l in layers ]
        ]

    def RemoveBlur(key, layers):
        """
        Remove blur from the given layers given that they 
        have the same assigned key.

        `key`
            Unique key used for blurring the layers.

        `layers`
            Layers to remove the blur from.
        """

        layers = [ layer for layer in layers if layer_keys[layer] == key ]

        return [ 
            [ Function(renpy.show_layer_at, easeout_blur(layer_blur_radius[l]), l) for l in layers ],
            [ SetDict(layer_keys, layer, None) for layer in layers ],
            [ SetDict(layer_blur_radius, layer, None) for layer in layers ]
        ]

transform -10 easein_blur(b):
    blur 0.0
    easein_quad 0.5 blur b

transform -10 easeout_blur(b):
    blur b
    easein_quad 0.5 blur 0.0
