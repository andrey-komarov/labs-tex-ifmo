#!/bin/bash
#~ latex all.tex
pushd tables/txt
bash ./make_tables.sh
popd

pushd pics
./r.sh
popd

pdflatex all.tex
