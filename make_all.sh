#!/bin/bash
for d in src/??; do
    if [ -d $d ]; then
        l=$(basename $d)
        make LANG=$l
    fi
done
