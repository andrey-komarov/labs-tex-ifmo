#!/usr/bin/python
from math import *
sqr = lambda x: x * x


class Approx():
    
    def __init__(self,xx, yy):
        self.x = xx
        self.y = yy
        self.n = len(self.x)
        self.x_ave = sum(self.x) / self.n
        self.y_ave = sum(self.y) / self.n
    
        self.D = 0
        for i in range(self.n):
            self.D += sqr(self.x[i] - self.x_ave)
    
        self.A = 0
        for i in range(self.n):
            self.A += (self.x[i] - self.x_ave) * self.y[i]
        self.A /= self.D
    
        self.C = self.y_ave - self.A * self.x_ave
    
    def get(self, x):
        return self.A * x + self.C
    

