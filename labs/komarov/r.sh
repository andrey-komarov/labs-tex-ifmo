#!/bin/bash
#~ latex all.tex
pushd tables/txt
./make_tables.sh
popd

pushd pics
~/scripts/mp2pdf.sh points.mp
popd

pdflatex all.tex
