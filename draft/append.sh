#!/bin/bash

draftmd="../draft/overlay"
draftpng="../draft/boards"
dirmd="../src/en/overlay"
dirpng="../resources/boards"
tmpmd="$dirmd/template.md"
tmppng="$dirpng/template.png"
yamlfile="../src/en/settings.yaml"
mdlist=$(ls "$draftmd")

mv -R $draftmd/* $dirmd && rm $tmpmd
mv -R $draftpng/* $dirpng && rm $tmppng

for overlay in $mdlist; do
    if [ $overlay != "template.md" ]; then
        board=$(echo "$overlay" | rev | cut -c 4- | rev)
        if ! grep -e $board $yamlfile &> /dev/null; then
            echo "- $board" | tee -a $yamlfile &> /dev/null
        fi
    fi
done

exit 0
