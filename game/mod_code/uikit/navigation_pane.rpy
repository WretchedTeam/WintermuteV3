screen navigation_pane(options, _xsize):
    frame background "#fff":
        padding (0, 0) 
        xsize _xsize yfill True

        vbox xfill True:
            add "icosahedron" xalign 0.5

            use navbar_buttons(options)

        vbox align (0.0, 1.0):
            add "#828282" ysize 2

            frame style "empty":
                padding (30, 30)
                use username_display()