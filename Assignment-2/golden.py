import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return 1-x**2*np.exp(-x)
rho = float((3-5**0.5)/2)
l,u,eps = -0.5,2.5,0.05
w = float(u-l)
l_,u_ = l+w*rho,u-w*rho
fl_,fu_ = f(l_),f(u_)
width,minim = [],[]
while(w>eps):
    if fu_ > fl_:
        u = u_
        w = u - l
        u_,fu_ = l_,fl_
        l_ = l+w*rho
        fl_ = f(l_)
    else:
        l = l_
        w = u-l
        l_,fl_ = u_,fu_
        u_ = u-w*rho
        fu_ = f(u_)
    width.append(w)
    minim.append((l+u)/2)
fig,axs = plt.subplots(1,2, constrained_layout=True)
axs[0].plot(width)
axs[0].set_ylabel("width")
axs[0].set_xlabel("Iterations")
axs[1].plot(minim)
axs[1].set_ylabel("minima")
axs[1].set_xlabel("Iterations")
fig.suptitle("Golden Section Search")
plt.show()
        


