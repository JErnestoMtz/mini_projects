import numpy as np 
from math import ceil, e
import matplotlib.pyplot as plt




def plot_complex(origen, fin, r):
    x = [origen.real, fin.real]
    y = [origen.imag, fin.imag]
    plt.plot(x,y, linewidth = 3 , c = (0.33, (1-r/11)/3, 0.176))


def tree(origin, branch, anglel, angler, scalel, scaler, rec_factor):
    if rec_factor > 0:
        plot_complex(origin,branch, rec_factor)
        branch_l = ((branch-origin) * e ** (1j*anglel)*scalel)+branch
        branch_r = ((branch-origin) * e ** (-1j*angler)*scaler)+branch
        tree(branch,branch_l,anglel,angler,scalel,scaler,rec_factor-1)
        tree(branch,branch_r,anglel,angler,scalel,scaler,rec_factor-1)

origen = 0 + 0j 
tronco = 0 + 0.7j

angler = 0.44
anglel = 0.44

scaler = 0.5
scalel = 0.5
recurtion_factor = 1

tree(origen,tronco,anglel,angler,scalel, scaler,recurtion_factor)
ax = plt.gca()
#ax.set_facecolor((1, 0.835, 0.804))
plt.show()
