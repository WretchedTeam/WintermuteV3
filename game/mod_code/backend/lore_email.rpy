init python in _wm_lore_emails:
    import os 
    import os.path

    from renpy.config import basedir

    file_directory = "mod_assets/lore_emails/"
    output_directory = basedir + "/email_backups/"

    def copy_file(src, dst):
        from shutil import copyfileobj

        srcf = renpy.file(src) 
        dstf = open(dst, "wb")

        copyfileobj(srcf, dstf)

        srcf.close()
        dstf.close()

    def unlock_email(f):
        src = file_directory + f

        if not renpy.exists(src):
            return

        dst = os.path.join(output_directory, f)

        dstfolder = os.path.dirname(dst)

        if not os.path.exists(dstfolder): 
            os.makedirs(dstfolder)

        copy_file(src, dst)
