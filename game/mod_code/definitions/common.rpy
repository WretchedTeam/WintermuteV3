init python:
    import time

    def turnell_username():
        """
        Returns an email username handle generated from the firstname 
        and lastname variables.
        """
        return "%s.%s" % (persistent.firstname[0].lower(), persistent.lastname.lower())


label test_prompt_button(t):
    menu:
        "[t]":
            pass