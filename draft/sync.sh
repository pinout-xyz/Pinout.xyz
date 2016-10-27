#!/bin/bash

masterdir="../src/en/overlay"
mdlist=$(ls "$masterdir")
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"
filesync=false

for overlay in $mdlist; do
    board=$(echo "$overlay" | rev | cut -c 4- | rev)
    for dirmd in ${langlist[@]}; do
        if [ -f $srcdir/$dirmd/translate/$overlay ]; then
            if [ -n "$(diff "$masterdir/$overlay" "$srcdir/$dirmd/translate/$overlay" 2> /dev/null)" ]; then
                echo "overwriting $dirmd/translate/$overlay"
                cp $masterdir/$overlay $srcdir/$dirmd/translate/
                filesync=true
            fi
        elif ! [ -f $srcdir/$dirmd/overlay/$overlay ]; then
            echo "copying $overlay to $dirmd/translate/"
            cp $masterdir/$overlay $srcdir/$dirmd/translate/
                filesync=true
        fi
        if ! grep -e $board ../src/$dirmd/$yamlfile &> /dev/null; then
            echo "adding $board to $dirmd/$yamlfile"
            echo "- $board" | tee -a ../src/$dirmd/$yamlfile &> /dev/null
        fi
    done
done

if ! $filesync;then
    echo "all pending translations are up-to-date"
fi

exit 0
