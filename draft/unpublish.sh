#!/bin/bash

draftpng="../draft/boards"
dirpng="../resources/boards"
draftmd="../draft/overlay"
mdlist=$(ls "$draftmd")
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"

if [ "$#" -eq 0 ]; then
    warning "please specify a board to unpublish!" && exit 1
fi

board=$1

for dirmd in ${langlist[@]}; do
    if [ $dirmd != "en" ]; then
        rm $srcdir/$dirmd/translate/$board.md
    else
        mv $srcdir/$dirmd/overlay/$board.md $draftmd
    fi
    if grep -e $board $srcdir/$dirmd/$yamlfile &> /dev/null; then
        sed -i "|- $board|d" $yamlfile &> /dev/null
    fi
done

if [ -f $dirpng/$board.png ]; then
    mv $dirpng/$board.png $draftpng
fi

exit 0
