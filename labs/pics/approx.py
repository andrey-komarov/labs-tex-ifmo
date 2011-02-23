#!/usr/bin/python
from math import *
sqr = lambda x: x * x

n = 0
x = []
y = []

def init(xx, yy):
    x = xx
    y = yy
    n = len(x)

if __name__ == "__main__":
    inf = open('input.txt')
    for l in inf.readlines():
        curx, cury = map(float, l.split())
        x.append(curx)
        y.append(cury)
        n += 1
    
x_ave = sum(x) / n
y_ave = sum(y) / n

D = 0
for i in range(n):
    D += sqr(x[i] - x_ave)

A = 0
for i in range(n):
    A += (x[i] - x_ave) * y[i]
A /= D

C = y_ave - A * x_ave

E = 0
for i in range(n):
    E += sqr(y[i] - A * x[i] - C)
E /= n - 2

dA = sqrt(E/D)
dC = sqrt((1./n + x_ave*x_ave/D) * E)

dt = 290 * sqrt(sqr(dA/A) + sqr(dC/C))

if __name__ == "__main__":
    print "A, C, C/A, dt:"
    print A
    print C
    print C / A
    print "dt: %f"%dt
    print "dA: %f"%dA
    print "dC: %f"%dC

def appr(x):
    return A * x + C
