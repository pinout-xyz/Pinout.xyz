#!/bin/bash

masterdir="../src/en/overlay"
mdlist=$(ls "$masterdir")
srcdir="../src"
langlist=$(ls "$srcdir")
filesync=false

for overlay in $mdlist; do
    for dirmd in ${langlist[@]}; do
        if [ -f $srcdir/$dirmd/translate/$overlay ]; then
            if [ -n "$(diff "$masterdir/$overlay" "$srcdir/$dirmd/translate/$overlay" 2> /dev/null)" ]; then
                echo "overwriting $dirmd/translate/$overlay"
                cp $masterdir/$overlay $srcdir/$dirmd/translate/
                filesync=true
            fi
        fi
    done
done

if ! $filesync;then
    echo "all pending translations are up-to-date"
fi

exit 0
