#!/bin/bash

masterdir="../src/en/overlay"
mdlist=$(ls "$masterdir")
srcdir="../src"
langlist=$(ls "$srcdir")
yamlfile="settings.yaml"
filesync=false
urlfix=false

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

        if [ -f "$srcdir/$dirmd/overlay/$overlay" ]; then
            besturl=$(grep "^url: http" "$masterdir/$overlay")
            langurl=$(grep "^url: http" "$srcdir/$dirmd/overlay/$overlay")
            if [ "$besturl" != "$langurl" ]; then
                echo "url in en $overlay is $besturl"
                echo "url in $dirmd $overlay is $langurl"
                if confirm "would you like to fix this discrepancy?"; then
                    sed -i "s|^url.*$|$besturl|" "$srcdir/$dirmd/overlay/$overlay"
                    echo "external link was fixed" && urlfix=true
                fi
            fi
        fi
    done
done

if ! $filesync && ! $urlfix;then
    echo "all translations are up-to-date"
fi

exit 0
