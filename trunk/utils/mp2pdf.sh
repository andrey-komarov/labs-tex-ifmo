#!/bin/sh
# Скрипт для превращения MetaPost файла в EPS и PDF рисунки
 
# каталоги для хранения eps- и  pdf-файлов
EPS_DIR=./eps
PDF_DIR=./pdf
PNG_DIR=./png
TMP_FILE=tmp
RESOLUTION=1000
 
if [[ "$@" == ""]];
then
  echo 
  echo Скрипт обрабатывает mp-файл, создает eps- и pdf-файлы и
  echo перемещает их соответственно в каталоги $EPS_DIR и $PDF_DIR
  echo Использование: ./mp2pdf.sh file.mp
  echo
  exit
fi
 
if [ ! -d $EPS_DIR ]; then
  echo ======== Создание каталога для eps-файлов 
  mkdir $EPS_DIR
fi
if [ ! -d $PDF_DIR ]; then
  echo ======== Создание каталога для pdf-файлов
  mkdir $PDF_DIR
fi 
if [ ! -d $PNG_DIR ]; then
  echo ======== Создание каталога для pdf-файлов
  mkdir $PNG_DIR
fi 

 
echo ======== Исходный файл: $@
 
list=`grep beginfig $1 | sed -e 's/beginfig(//' -e 's/);//'`
echo ======== Список блоков:  $list
 
echo ======== Запуск mpost...
mpost -mem=mpost -tex=latex $1 #>/dev/null 2>/dev/null
 
for i in $list          # цикл по блокам beginfig()
do
 epsi=${1%mp}$i
 eps=${1%.mp}${i}.eps
 pdf=${1%.mp}${i}.pdf
 ps=${1%.mp}${i}.ps
 png=${1%.mp}${i}.png
 echo Блок ${i}: ' >> ' $epsi ' >> ' $eps ' >> ' $pdf
 
if [ ! -e $epsi ]; then
  echo
  echo Ошибки при обработке mp-файла!
  echo
  exit
else
  echo ======== MetaPost ===== Ok!
fi
 
echo ======== Генерация временного LaTeX-файла...
echo \\documentclass[12pt]{minimal} > ${TMP_FILE}.tex
echo \\usepackage{mathtext} >> ${TMP_FILE}.tex
echo \\usepackage{amsmath} >> ${TMP_FILE}.tex
echo \\usepackage[T2A]{fontenc} >> ${TMP_FILE}.tex
echo \\usepackage[utf8]{inputenc} >> ${TMP_FILE}.tex
echo \\usepackage[english,russian]{babel} >> ${TMP_FILE}.tex
echo \\usepackage{graphics} >> ${TMP_FILE}.tex
echo -n "\\" >> ${TMP_FILE}.tex
echo begin{document} >> ${TMP_FILE}.tex
echo \\pagestyle{empty} >> ${TMP_FILE}.tex
echo \\includegraphics{${epsi}} >> ${TMP_FILE}.tex
echo \\end{document} >> ${TMP_FILE}.tex
 
echo ======== Запуск LaTeX...
latex ${TMP_FILE} #>/dev/null 2>/dev/null
 
if [ ! -e ${TMP_FILE}.dvi ]; then
  echo
  echo ======== Не найден dvi-файл!
  echo
  exit
else
  echo ======== LaTeX ===== Ok!
fi
echo ======== Запуск dvips...
dvips -E ${TMP_FILE} -o $eps #>/dev/null 2>/dev/null
 
echo ======== Запуск epstopdf...
epstopdf $eps #>/dev/null 2>/dev/null

echo ======== Создание PNG
pdftops $pdf #>/dev/null 2>/dev/null
ps2image -res $RESOLUTION $ps $png #>/dev/null 2>/dev/null

if [ -e $pdf ]; then
 mv $eps $EPS_DIR 
 mv $pdf $PDF_DIR
 mv $png $PNG_DIR
 echo ======== Перенос $eps и $pdf в нужное место...
fi
 
echo ======== Зачистка...
rm *.ps *.log *.mpx ${TMP_FILE}.* *.aux *.dvi *.tex $epsi #2>>/dev/null
 
done

echo ======== Готово! ========
