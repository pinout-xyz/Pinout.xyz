#!/bin/bash

draftmd="../draft/overlay"
draftpng="../draft/boards"
dirmd="../src/en/overlay"
dirpng="../resources/boards"
tmpmd="$dirmd/template.md"
tmppng="$dirpng/template.png"
yamlfile="../src/en/settings.yaml"
mdlist=$(ls "$draftmd")

for overlay in $mdlist; do
    if [ $overlay != "template.md" ]; then
        board=$(echo "$overlay" | rev | cut -c 4- | rev)
        if ! grep -e $board $yamlfile &> /dev/null; then
            echo "- $board" | tee -a $yamlfile &> /dev/null
        fi
        mv $draftmd/$overlay $dirmd
        mv $draftpng/$board.png $dirpng
    fi
done

exit 0
