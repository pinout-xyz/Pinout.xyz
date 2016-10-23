#!/bin/bash

draftpng="../draft/boards"
dirpng="../resources/boards"
draftmd="../draft/overlay"
mdlist=$(ls "$draftmd")
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"

FORCE=$1

confirm() {
    if [ "$FORCE" == '-y' ]; then
        true
    else
        read -r -p "$1 [y/N] " response < /dev/tty
        if [[ $response =~ ^(yes|y|Y)$ ]]; then
            true
        else
            false
        fi
    fi
}

for overlay in $mdlist; do
    if [ $overlay != "template.md" ]; then
        board=$(echo "$overlay" | rev | cut -c 4- | rev)
        if confirm "Would you like to publish $board?"; then
            for dirmd in ${langlist[@]}; do
                if [ $dirmd != "en" ]; then
                    if ! [ -f $srcdir/$dirmd/overlay/$overlay ]; then
                        cp $draftmd/$overlay $srcdir/$dirmd/translate/
                    fi
                else
                    cp $draftmd/$overlay $srcdir/$dirmd/overlay/
                fi
                if ! grep -e $board ../src/$dirmd/$yamlfile &> /dev/null; then
                    echo "- $board" | tee -a ../src/$dirmd/$yamlfile &> /dev/null
                fi
            done
            rm $draftmd/$overlay
            if [ -f $draftpng/$board.png ];then
                mv $draftpng/$board.png $dirpng
            fi
        fi
    fi
done

exit 0
