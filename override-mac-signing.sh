case "$(uname -s)" in
    Darwin|mac)
        ;;
    *)
        echo "Not a Mac device!"
        ;;
esac

if test ! -d "WintermuteV3.app"; then
    echo "WintermuteV3.app not found."
    exit
fi

sudo chmod -R 755 WintermuteV3.app
sudo xattr -d com.apple.quarantine WintermuteV3.app

echo "Done."
exit
