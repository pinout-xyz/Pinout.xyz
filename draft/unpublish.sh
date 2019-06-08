#!/bin/bash

cd $(dirname $0)

draftpng="../draft/boards"
dirpng="../resources/boards"
draftmd="../draft/overlay"
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"

if [ "$#" -eq 0 ]; then
    echo "please specify a board to unpublish!"
    exit 1
fi

board=$1

if ! [ -f $srcdir/en/overlay/$board.md ]; then
    echo "Board $1 does not exist!"
    exit 1
fi

for dirmd in ${langlist[@]}; do
    if [ $dirmd != "en" ]; then
        echo "Removing $srcdir/$dirmd/translate/$board.md"
        rm $srcdir/$dirmd/translate/$board.md &> /dev/null
    else
        echo "Moving $srcdir/$dirmd/overlay/$board.md to $draftmd"
        mv $srcdir/$dirmd/overlay/$board.md $draftmd
    fi
done

if [ -f $dirpng/$board.png ]; then
    echo "Moving $dirpng/$board.png to $draftpng"
    mv $dirpng/$board.png $draftpng
fi

exit 0
