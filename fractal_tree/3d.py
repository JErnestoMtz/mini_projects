from timeit import timeit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import math
from quaternion import Quaternion


def quat_exp(theta,vec):
	imag = Quaternion(0,*vec)*math.sin(theta)
	real = Quaternion(math.cos(theta),0,0,0)
	return imag + real

def plot(q1,q2):	
	_, x1, y1, z1 = q1 
	_, x2, y2, z2 = q2
	ax.plot([x1,x2],[y1,y2],[z1,z2])


def tree(a,b,scale,angle,rec_factor):
	plot(a,b)
	if rec_factor > 0:
		exp_lef = quat_exp(angle/2,(1,0,0))
		exp_rigth = quat_exp(-angle/2,(1,0,0))
		left = (exp_lef@((b-a)*scale)@exp_lef.inv())+b
		rigth = (exp_rigth@((b-a)*scale)@exp_rigth.inv())+b
		tree(b,left,scale,angle,rec_factor-1)	
		tree(b,rigth,scale,angle,rec_factor-1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = Quaternion(0,0,0,0)
b = Quaternion(0,0,0,1)

angel = math.pi / 9

tree(a,b,0.7,angel,3)

#print(r)
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(0, 3)


plt.show()