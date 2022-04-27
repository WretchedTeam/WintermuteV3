init -10 python:
    import datetime
    def debug(method):
        def inner(*args, **kwargs):
            if config.developer:
                method(*args, **kwargs)
            else:
                raise Exception("Not in dev mode.")

        return inner

label test_prompt_button(t):
    menu:
        "[t]":
            pass