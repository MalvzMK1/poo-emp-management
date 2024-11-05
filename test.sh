#!/bin/bash

for param in $@; do
    if [ $param = "--no-cache" ]; then
        find ./ \
            -type d \
            -name "*pycache*" \
            -exec rm -r {} \;
    fi

    if [ $param = "--migrate" ]; then
        echo "Migrate"
    fi
done
