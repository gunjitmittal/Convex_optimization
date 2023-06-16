import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1-x**2*np.exp(-x)
def f_(x):
    return x**2*np.exp(-x) - 2*x*np.exp(-x)
l,u,eps = -0.5,2.5,0.05
w = u-l
x = 0 
width,minim = [],[]
while w>eps:
    c = (l+u)/2
    fc = f_(c)
    if fc>0:
        u = c
    elif fc<0:
        l = c
    else:
        x = c
        break
    w = u-l
    width.append(w)
    minim.append(c)
fig,axs = plt.subplots(1,2, constrained_layout=True)
axs[0].plot(width)
axs[0].set_ylabel("width")
axs[0].set_xlabel("Iterations")
axs[1].plot(minim)
axs[1].set_ylabel("minima")
axs[1].set_xlabel("Iterations")
fig.suptitle("Bisection Search")
plt.show()