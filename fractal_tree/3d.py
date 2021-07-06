from timeit import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import math


A = []

for i in range(10):
	A.append((i,i+1,i+2,i+3))

B = A.copy()


def quat_mult(a,b):
	a0, a1, a2, a3 = a 
	b0, b1, b2, b3 = b
	return ((a0*b0-a1*b1-a2*b2-a3*b3),(a0*b1+a1*b0+a2*b3-a3*b2),(a0*b2-a1*b3+a2*b0+a3*b1),(a0*b3+a1*b2-a2*b1+a3*b0))

def scalr_mult(a,c):
	a0, a1, a2, a3 = a
	return (a0*c, a1*c, a2*c, a3*c)

def quat_inv(a):
	a0, a1, a2, a3 = a
	return scalr_mult((a0,-a1,-a2,-a3),(1/(a0**2+a1**2+a2**2+a3**4)))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def quat_exp(theta,v):
	return quat_sum((math.cos(theta),0,0,0),scalr_mult(v,math.sin(theta)))



def plot(p1,p2):
	r1, x1, y1, z1 = p1
	r2, x2, y2, z2 = p2
	ax.plot([x1,x2],[y1,y2],[z1,z2])

def quat_sum(a,b):
	a0, a1, a2, a3 = a 
	b0, b1, b2, b3 = b
	return (a0+b0,a1+b1,a2+b2,a3+b3)


def quat_sub(a,b):
	a0, a1, a2, a3 = a 
	b0, b1, b2, b3 = b
	return (a0-b0,a1-b1,a2-b2,a3-b3)

def tree(p1,p2,angle,scale,rec_factor):
	if rec_factor > 0:
		plot(p1,p2)
		scaled = scalr_mult(quat_sub(p2,p1),scale)
		exp_left = quat_exp(angle/2, (0,1,0,0))		
		exp_rigth = quat_exp(-angle/2, (0,1,0,0))
		left = quat_mult(exp_left,quat_mult(quat_inv(exp_left),scaled))
		rigth = quat_mult(exp_rigth,quat_mult(quat_inv(exp_rigth),scaled))
		left = quat_sum(left,p1)
		rigth = quat_sub(rigth,p1)
		print(rigth)
		print(left)
		tree(p2,left,angle,scale,rec_factor-1)
		tree(p2,rigth,angle,scale,rec_factor-1)


a = (0,0,0,0)
b = (0,0,0,1)
angle = math.pi/6

scale = 0.8
rec_factor = 3

tree(a,b,angle,scale,rec_factor)
#q = quat_exp(math.pi/12,(0,1,,0))
#q_prime = quat_inv(q)
#r = quat_mult(q_prime,q)

#print(r)

plt.show()

