#Listing 6.12 : Motion of a wavepackage

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

a=1
oneoverpi=1/(np.sqrt(np.pi))
fig = plt.figure()
ax = fig.add_subplot(111,autoscale_on=False,xlim=(-5,5),ylim=(0,1.5))
ax.grid()
plt.title("Wave Packet in H. O. potential")
plt.xlabel("x")
plt.ylabel("$|\psi(x,t)|^2$")

line,=ax.plot([],[],lw=2)
def init():#baseframe
    line.set_data([],[])
    return line

def animate(t):  #Called repeatedly
    y=oneoverpi*np.exp(-(x-a*np.cos(0.01*t))**2)  #Plot ea 0.01*t
    line.set_data(x,y) 
    return line,

x=np.arange(-5,5,0.01)  #range for x values
ani=FuncAnimation(fig,animate,init_func=init,frames=1000,interval=10)
plt.show()

