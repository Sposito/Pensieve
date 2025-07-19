#!/bin/bash
# Open file in Obsidian
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

file="$1"
if [ -f "$file" ]; then
    obsidian "$file"
else
    echo "File not found: $file"
    exit 1
fi 