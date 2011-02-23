#!/bin/python
#-*- coding: utf8 -*-
sqr = lambda x: x * x 

V = range(50, 150, 10)
points = []
first = []
last = []

def X(x):
    x_coef = 1359.
    return (x)* x_coef
    
def Y(y):
    y_coef = 0.1
    return y * y_coef

inf = open('points.txt')
out = open('points.mp.txt', 'w').write

n = 5

xmin = ymin = 10**9
xmax = ymax = -10**9

for i in range(n):
    x = []
    y = []
    x_ave = 0
    y_ave = 0
    for j in range(10):
        f = float(inf.readline())
        x.append(f)
        y.append(V[j])
        x_ave += f
        y_ave += V[j]        
        points.append((i + 1, f, V[j]))
    x_ave /= 10.
    y_ave /= 10.
    D = sum(sqr(x[i] - x_ave) for i in range(10))
    A = sum((x[i] - x_ave) * y[i] for i in range(10)) / D
    C = y_ave - A * x_ave
    print A
    approx = lambda x: A * x + C
    delta = (x[9] - x[0]) / 10.
    first.append((x[0] - delta, approx(x[0] - delta)))
    last.append((x[9], approx(x[9])))
    xmin = min(xmin, min(x))
    ymin = min(ymin, min(y))
    xmax = max(xmax, max(x))
    ymax = max(ymax, max(y))
    inf.readline()

out('u = 0.65cm;\n')

for index, x, y in points:
    out('dotlabel.top("%d", (%.10f * u, %.10f * u));\n'%(index, X(x), Y(y)))

for i in range(n):
    out('draw (%.10f * u, %.10f * u)--(%.10f * u, %.10f * u);\n'%(X(first[i][0]), Y(first[i][1]), X(last[i][0]), Y(last[i][1])))

dx = (xmax - xmin) / 10
dy = (ymax - ymin) / 10

xmin -= dx
xmax += dx
ymin -= dy
ymax += dy

out('drawarrow (%.10f * u, %.10f * u)--(%.10f * u, %.10f * u);\n'%(X(xmin), Y(ymin), X(xmin), Y(ymax)))
out('drawarrow (%.10f * u, %.10f * u)--(%.10f * u, %.10f * u);\n'%(X(xmin), Y(ymin), X(xmax), Y(ymin)))
out((u'label.bot(btex $\\frac1P$ ,кПа${}^{-1}$ etex, (%.10f * u, %.10f * u));\n'%(X(xmax), Y(ymin))).encode('utf8'))
out((u'label.lft(btex $V_ц$, мл etex, (%.10f * u, %.10f * u));\n'%(X(xmin), Y(ymax))).encode('utf8'))

serifs = 8
serifsize = 0.2

for i in range(1, serifs):
    curx = (xmax - xmin) * i / serifs + xmin
    out('draw (%.10f * u, %.10f * u)--(%.10f * u, %.10f * u) withpen pencircle scaled 0.5;\n'%(X(curx), Y(ymin)-serifsize, X(curx), Y(ymin)+serifsize))
    out('label.bot("%.3f", (%.10f * u, %.10f * u));\n'%(curx, X(curx), Y(ymin) - serifsize / 2))
    cury = (ymax - ymin) * i / serifs + ymin
    out('draw (%.10f * u, %.10f * u)--(%.10f * u, %.10f * u) withpen pencircle scaled 0.5;\n'%(X(xmin) - serifsize, Y(cury), X(xmin) + serifsize, Y(cury)))
    out('label.lft("%.0f", (%.10f * u, %.10f * u));\n'%(cury, X(xmin), Y(cury) - serifsize / 2))
    
