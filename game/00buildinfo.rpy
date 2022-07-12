init -1400 python in _wm_buildinfo:
    import os
    from store import build

    def buildinfo_command():
        """
        The buildinfo command. This retrieves the required config values 
        and stores it in buildinfo.txt for generating a draft GH release.
        """

        output = os.path.join(renpy.config.basedir, "buildinfo.txt")

        with open(output, "w") as f:
            f.write(renpy.config.name + "\n")
            f.write(renpy.config.version + "\n")

            destination = build.destination.format(
                directory_name=build.directory_name,
                executable_name=build.executable_name,
                display_name=build.display_name,
                version=renpy.config.version,
            )

            f.write(destination + "\n")

            for package in build.packages:
                f.write(build.directory_name + "-" + package["name"] + "\n")

        return False


    renpy.arguments.register_command("buildinfo", buildinfo_command)
