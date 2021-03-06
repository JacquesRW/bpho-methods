from methods import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from time import perf_counter as tm

'''
METHODS:
- cpp_euler_scheme
- py_euler_scheme
- cpp_rk4_scheme
- py_rk4_scheme
set h=0.01 for euler and 0.1 for rk4
'''

methods = [cpp_euler_scheme, py_euler_scheme, cpp_rk4_scheme, py_rk4_scheme]
method = methods[0]
dh = 0.1

'''
PARAMETERS:
- dN : the step size for display output
- h0 : the initial altitude
- h1 : the height when the tropsphere ends
- P0 : the initial pressure at h0
- T0 : the initial temperature at h0
- U0 :  the initial relative humidity value
'''

U0 = 0.5
H = np.arange(111) * 0.1


def update(val: float) -> None:
    global count, duration
    start = tm()
    data = method(val)
    line1.set_ydata(data[0])
    line2.set_ydata(data[1])
    line3.set_ydata(data[2])
    duration += tm() - start
    count += 1


if __name__ == "__main__":
    fig, axs = plt.subplots(ncols=3, nrows=1, figsize=(12, 6))
    init_data = method(U0)
    line1, = axs[0].plot(H, init_data[0], lw=2)
    line2, = axs[1].plot(H, init_data[1], lw=2)
    line3, = axs[2].plot(H, init_data[2], lw=2)

    plt.subplots_adjust(left=0.1,
                        bottom=0.25,
                        right=0.95,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)

    axs[0].set_ylim(0, 1100)
    axs[0].set_ylabel('Pressure (mbar)')
    axs[1].set_ylim(-100, 25)
    axs[1].set_ylabel('Temperature (Celsius)')
    axs[2].set_xlabel('Altitude (km)')
    axs[2].set_ylim(0, 10)
    axs[2].set_ylabel('Lapse Rate (Kelvin/km)')

    axu = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider = Slider(
        ax=axu,
        label='Relative Humidity',
        valmin=0,
        valmax=1,
        valstep=0.01,
        valinit=U0)

    count, duration = 0, 0
    slider.on_changed(update)
    plt.show()
    print(f"Average update took {(1_000_000 * duration / count):.4f} microseconds, from {count} updates.")
