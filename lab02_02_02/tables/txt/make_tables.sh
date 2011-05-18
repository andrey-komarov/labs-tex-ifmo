#!/bin/bash
javac *.java

for i in *.txt
do
    cp $i txt2tex.in
    java txt2tex
    cp txt2tex.out ../$i
done

for i in ../*.txt; do j=`echo $i | sed 's/txt/tex/g'`; mv "$i" "$j"; done
