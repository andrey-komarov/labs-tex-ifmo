#!/bin/bash

cat title_base.tex | sed "s/NAME/$1/g" > title.tex

pushd tables/txt
bash ./make_tables.sh
popd

pushd pics
./r.sh
popd

pdflatex all.tex

mkdir ready

cp all.pdf "ready/$1.pdf"
