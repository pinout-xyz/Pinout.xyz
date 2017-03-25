#!/bin/bash

cd $(dirname $0)

draftpng="../draft/boards"
dirpng="../resources/boards"
draftmd="../draft/overlay"
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"

if [ "$#" -eq 0 ]; then
    echo "please specify a board to unpublish!" && exit 1
fi

board=$1

for dirmd in ${langlist[@]}; do
    if [ $dirmd != "en" ]; then
        rm $srcdir/$dirmd/translate/$board.md &> /dev/null
    else
        mv $srcdir/$dirmd/overlay/$board.md $draftmd
    fi
    if grep -e $board $srcdir/$dirmd/$yamlfile &> /dev/null; then
        sed -i "/$board/d" $srcdir/$dirmd/$yamlfile
    fi
done

if [ -f $dirpng/$board.png ]; then
    mv $dirpng/$board.png $draftpng
fi

exit 0
