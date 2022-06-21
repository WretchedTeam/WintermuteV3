python early in _wm_fix_screen_use_limit:
    from renpy.sl2.slast import SLUse

    def used_screens(self, callback):
        if not isinstance(self.target, renpy.ast.PyExpr):
            callback(self.target)

        if self.block is not None:
            self.block.used_screens(callback)

    SLUse.used_screens = used_screens