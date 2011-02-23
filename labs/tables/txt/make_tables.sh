#!/bin/bash

for i in *.txt
do
    ~/scripts/txttable2tex.py $i
done

mv *.tex ..
