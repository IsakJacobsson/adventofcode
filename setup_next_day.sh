#!/bin/bash

year=$1
day=$2

mkdir -p $year/day$day

cd $year/day$day

echo 'with open("input.txt", "r") as f:
    s = f.read().strip()

' > main.py
