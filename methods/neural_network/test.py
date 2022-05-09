import numpy as np
import t_net
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from time import perf_counter as tm

U0 = 0.5

hset = np.arange(23) * 0.5
fig, ax = plt.subplots()
line, = plt.plot(hset, t_net.predict(U0), lw=2)

ax.set_ylim(-100, 25)
ax.set_ylabel('Temperature (Celsius)')
ax.set_xlabel('Altitude (km)')

plt.subplots_adjust(left=0.25, bottom=0.25)
axu = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax=axu,
    label='Relative Humidity',
    valmin=0,
    valmax=1,
    valstep=0.01,
    valinit=U0)


def update(val):
    global count, duration
    start = tm()
    line.set_ydata(t_net.predict(val))
    fig.canvas.draw_idle()
    duration += tm() - start
    count += 1


count, duration = 0, 0
slider.on_changed(update)
plt.show()
print(f"Average update took {duration/count:.5f}, from {count} updates.")
