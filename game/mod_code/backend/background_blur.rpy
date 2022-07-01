# Effect used for the overlay VN interface.

# It gets the layers as a single displayable behind 
# the object's layer, and applies a shader which 
# performs alpha masking, blurring and the final 
# composition of the object over the blured background.

# The Kawase blur is chosen due to its very low performance hit.

# This is essentially how Q did his blurred multiply blend 
# blue square, just modularized.

init python in _wm_bg_blur:
    from store import Fixed, persistent

    class BackgroundBlur(renpy.Container):
        def __init__(self, child, background, **kwargs):
            super(BackgroundBlur, self).__init__(**kwargs)
            self.background = renpy.displayable(background)
            self.add(self.background)
            self.add(child)

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            br = renpy.render(self.background, width, height, st, at)

            rv = renpy.Render(*cr.get_size())
            rv.blit(br, (0, 0))
            rv.blit(cr, (0, 0))

            rv.mesh = True
            rv.shaders = None
            rv.add_shader("wm.kawase_background")
            rv.add_uniform("u_lod_bias", 2.0)
            rv.add_uniform("u_iteration", 1.0)

            self.offsets = [ (0, 0), (0, 0) ]

            return rv

    @renpy.curry
    def apply(layers, d):
        if not persistent.blur_effects:
            return d

        if not isinstance(layers, list):
            layers = [ layers ]

        d = Fixed(d)
        scene_lists = renpy.game.context().scene_lists
        layer_properties = renpy.display.interface.layer_properties

        bg = [ scene_lists.make_layer(l, layer_properties[l]) for l in layers ]
        bg_root = renpy.Container(*bg)

        return BackgroundBlur(d, bg_root)