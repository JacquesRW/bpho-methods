from resources import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from time import perf_counter as tm

'''
PARAMETERS:
- dh : the step size used for altitude
- h0 : the initial altitude, recommended to leave at 0
- h1 : the height when the tropsphere ends
- P0 : the initial pressure at h0
- T0 : the initial temperature at h0
- dN : the step size for output to csv
-  U :  the humidity value between 0 and 1 inclusive -> single simulations
'''

dh = 0.01
dN = 0.5 
h0 = 0 
h1 = 11
P0 = 1013.25 
T0 = 15
U0 = 0.5

N = int((h1-h0)/dN)+1
H = np.arange(N)*dN

fig, axs = plt.subplots(ncols=3,nrows=1, constrained_layout=True,figsize=(12,6))
init_data = cpp_single_sim(dh, h0, h1, P0, T0, U0, dN)
line1, = axs[0].plot(H, init_data[0], lw=2)
line2, = axs[1].plot(H, init_data[1], lw=2)
line3, = axs[2].plot(H, init_data[2], lw=2)

plt.subplots_adjust(left=0.1,
                    bottom=0.25, 
                    right=0.95, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

axs[0].set_ylim(0,1100)
axs[0].set_ylabel('Pressure (mbar)')
axs[1].set_ylim(-100,25)
axs[1].set_ylabel('Temperature (Celsius)')
axs[2].set_xlabel('Altitude (km)')
axs[2].set_ylim(0,10)
axs[2].set_ylabel('Lapse Rate (Kelvin/km)')

axu = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax=axu,
    label='Relative Humidity',
    valmin=0,
    valmax=1,
    valinit=U0 )

def update(val: float) -> None:
    global count, duration
    start = tm()
    data = cpp_single_sim(dh, h0, h1, P0, T0, val, dN)
    line1.set_ydata(data[0])
    line2.set_ydata(data[1])
    line3.set_ydata(data[2])
    fig.canvas.draw_idle()
    duration += tm()-start
    count += 1

count, duration = 0, 0
slider.on_changed(update)
plt.show()
print(f"Average update took {duration/count:.5f}, from {count} updates.")