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

def plot(q1,q2,r):	
    _, x1, y1, z1 = q1 
    _, x2, y2, z2 = q2
    if r == 1:
        ax.plot([x1,x2],[y1,y2],[z1,z2],linewidth = math.ceil(r),c =  (0, 0.8, 0.176))
    else:
        ax.plot([x1,x2],[y1,y2],[z1,z2],linewidth = math.ceil(r),c = (0.33, (1-r/7)/2, 0.176))


def tree(a,b,scale,angle,rec_factor):
	plot(a,b,rec_factor)
	if rec_factor > 0:
		exp_1 = quat_exp(angle/2,(0,1,0))
		exp_2 = quat_exp(angle/2,(-0.866025,-0.5,0))
		exp_3 = quat_exp(angle/2,(0.866025,-0.5,0))
		branch_1 = (exp_1@((b-a)*scale)@exp_1.inv())+b
		branch_2 = (exp_2@((b-a)*scale)@exp_2.inv())+b
		branch_3 = (exp_3@((b-a)*scale)@exp_3.inv())+b
		tree(b,branch_1,scale,angle,rec_factor-1)	
		tree(b,branch_2,scale,angle,rec_factor-1)
		tree(b,branch_3,scale,angle,rec_factor-1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = Quaternion(0,0,0,0)
b = Quaternion(0,0,0,1)

angel = math.pi / 6

tree(a,b,0.83,angel,7)

#print(r)
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(0, 3)


plt.show()