#!/usr/bin/python
# -*- coding: utf8 -*-
from approx2 import Approx

inf = open("plot.txt")
out = open("plot.mp.txt", 'w').write

n = 10
picnum = "4"
allx = []
ally = []
y = []
out('u' +picnum + '1 = 1000cm;\n')
out('u' + picnum + '2 = 0.1cm;\n')

for i in range(n):
    y.append(float(inf.readline()))    
inf.readline()

#labels = ["50", "90", "140"]
labels = ["", "", ""]

for l in range(1):
    x = []
    for i in range(n):
        x.append(float(inf.readline()))    
    inf.readline()
    
    a = Approx(x, y)
    
    for i in range(n):
        out(('dotlabel.top(btex %s etex, (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2));\n')%(labels[l], x[i], y[i]))
    allx.extend(x)
    ally.extend(y)

    xmin = min(x)
    xmax = max(x)
    
    dx = (xmax - xmin) / 9
    
    xmin -= dx
    xmax += dx
    xmin = 0
    
    
    out(('draw (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2)--(%.10f * u' + picnum + '1, %.10f * u' + picnum + '2);\n')%(xmin, a.get(xmin), xmax, a.get(xmax)))

xmin = min(allx)
xmax = max(allx)
ymin = min(ally)
ymax = max(ally)

dx = (xmax - xmin) / 10
dy = (ymax - ymin) / 10

xmin -= dx
xmax += dx
ymin -= dy
ymax += dy
xmin = 0

print a.get(0)

X = Y = lambda x: x

out(('drawarrow (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2)--(%.10f * u' + picnum + '1, %.10f * u' + picnum + '2);\n')%(X(xmin), Y(ymin), X(xmin), Y(ymax)))
out(('drawarrow (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2)--(%.10f * u' + picnum + '1, %.10f * u' + picnum + '2);\n')%(X(xmin), Y(ymin), X(xmax), Y(ymin)))
out(((u'label.bot(btex $\\tilde t_0$, ${}^{\\circ}C$ etex, (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2));\n')%(X(xmax), Y(ymin))).encode('utf8'))
out(((u'label.lft(btex  $\\frac1{V_ц}$, м$^{-3}$ etex, (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2));\n')%(X(xmin), Y(ymax))).encode('utf8'))

serifs = 7
serifsize = 0.2

out('u' + picnum + '3 = 0.1cm;\n')

for i in range(1, serifs):
    curx = (xmax - xmin) * i / serifs + xmin
    out(('draw (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2 - u' + picnum + '3)--(%.10f * u' + picnum + '1, %.10f * u' + picnum + '2 + u' + picnum + '3) withpen pencircle scaled 0.5;\n')%(X(curx), Y(ymin), X(curx), Y(ymin)))
    out(('label.bot("%.06f", (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2));\n')%(curx, X(curx), Y(ymin) - serifsize / 2))
    cury = (ymax - ymin) * i / serifs + ymin
    out(('draw (%.10f * u' + picnum + '1 - u' + picnum + '3, %.10f * u' + picnum + '2)--(%.10f * u' + picnum + '1 + u' + picnum + '3, %.10f * u' + picnum + '2) withpen pencircle scaled 0.5;\n')%(X(xmin), Y(cury), X(xmin), Y(cury)))
    out(('label.lft("%.0f", (%.10f * u' + picnum + '1, %.10f * u' + picnum + '2));\n')%(cury, X(xmin), Y(cury) - serifsize / 2))
