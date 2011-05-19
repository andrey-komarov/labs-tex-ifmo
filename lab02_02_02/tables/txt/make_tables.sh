#!/bin/bash
javac txt2tex.java
javac txt2tex2.java

cp table1.txt txt2tex.in
java txt2tex2
cp txt2tex.out ../table1.tex

cp table2.txt txt2tex2.in
java txt2tex
cp txt2tex.out ../table2.tex



for i in ../*.txt; do j=`echo $i | sed 's/txt/tex/g'`; mv "$i" "$j"; done
