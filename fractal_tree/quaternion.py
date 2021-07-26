
from math import sqrt


class Quaternion:
    def __init__(self, w, i, j, k):
        self.w = w; 
        self.i = i;
        self.j = j;
        self.k = k;

    def __add__(self,q):
        return Quaternion(self.w+q.w,self.i+q.i,self.j+q.j,self.k+q.k)
    
    def __sub__(self,q):
        return Quaternion(self.w-q.w,self.i-q.i,self.j-q.j,self.k-q.k)
    def __mul__(self,c):
        return Quaternion(self.w*c,self.i*c,self.j*c,self.k*c)
    def __str__(self):
        return f'[{self.w},{self.i},{self.j},{self.k}]'   
    def __iter__(self):
        return iter((self.w,self.i,self.j,self.k))
    def __abs__(self):
        return sqrt(self.w**2+self.i**2+self.j**2+self.k**2)
    def __matmul__(self,q):
        a0, a1, a2, a3 = self
        b0, b1, b2, b3 = q
        return Quaternion((a0*b0-a1*b1-a2*b2-a3*b3),
                            (a0*b1+a1*b0+a2*b3-a3*b2),
                            (a0*b2-a1*b3+a2*b0+a3*b1),
                            (a0*b3+a1*b2-a2*b1+a3*b0))
    def inv(self):
        c = 1/(self.w**2+self.i**2+self.j**2+self.k**2)
        return Quaternion(self.w,-self.i,-self.j,-self.k)*c

