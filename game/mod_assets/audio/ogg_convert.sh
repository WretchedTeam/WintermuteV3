# To keep Lonesome from hunting down my ass.

for f in *.mp3 **/*.mp3 *.wav **/*.wav *.flac **/*.flac ;
    do name=`echo "$f" | cut -d'.' -f1`

    ffmpeg -i "$f" "${name}.ogg"

    if [ $? -eq 0 ]; then
        rm "$f"
    fi
done