import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1-x**2*np.exp(-x)
def f_(x):
    return x**2*np.exp(-x) - 2*x*np.exp(-x)
def f__(x):
    return -x**2*np.exp(-x) + 4*x*np.exp(-x) - 2*np.exp(-x)
head = -0.5
eps = 0.05
deri = []
while(np.abs(f_(head))>eps):
    print(head, f_(head))
    head = head - (f_(head))/(f__(head))
    deri.append(f_(head))
plt.plot(deri)
plt.show()