#!/bin/bash

cd $(dirname $0)

draftpng="../draft/boards"
dirpng="../resources/boards"
draftmd="../draft/overlay"
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"

if [ "$#" -eq 0 ]; then
    echo "please specify a board to publish!" && exit 1
fi

board=$1

for dirmd in ${langlist[@]}; do
    if [ $dirmd != "en" ]; then
        if ! [ -f $srcdir/$dirmd/overlay/$board.md ]; then
            cp $draftmd/$board.md $srcdir/$dirmd/translate/
        fi
    else
        cp $draftmd/$board.md $srcdir/$dirmd/overlay/
    fi
    if ! grep -e $board $srcdir/$dirmd/$yamlfile &> /dev/null; then
        echo "- $board" | tee -a $srcdir/$dirmd/$yamlfile &> /dev/null
    fi
done

rm $draftmd/$board.md

if [ -f $draftpng/$board.png ];then
    mv $draftpng/$board.png $dirpng
fi

exit 0
