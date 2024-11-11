#!/bin/bash

SRC="./venv/bin/python"

if [ ! -e $SRC ]; then
  SRC="./venv/Scripts/python.exe"

  if [ ! -e $SRC ]; then
    echo "Venv not found"

    exit 1
  fi
fi

for param in $@; do
    if [ $param = "--no-cache" ]; then
        find ./app \
            -type d \
            -name "*pycache*" \
            -exec rm -r {} \; \
            &> /dev/null
    fi

    if [ $param = "--migrate" ]; then
      find ./ -name "*.db" -exec rm {} \;

      $SRC ./run_migration.py
    fi
done

$SRC ./main.py
