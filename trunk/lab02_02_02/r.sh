#!/bin/bash
#~ latex all.tex
#~ pushd tables/txt
#~ ./make_tables.sh
#~ popd
#~ 
pushd pics
./r.sh
popd

pdflatex all.tex
