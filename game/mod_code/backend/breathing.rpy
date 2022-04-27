init -100 python in _wm_breathing:
    import random
    from store import absolute
    from store._warper import easein_cubic

    def random_step():
        return random.randint(1,6) * 0.1 + random.randint(1,20) * 0.005 + 1.5
