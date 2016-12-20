#import dependencies
import numpy as np
from matplotlib import animation, rc
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

y = np.arange(0,10,.1)
x = np.zeros(len(y))

patch = patches.Rectangle((0, 0), 0, 0,fc='y')


def init():
    ax.add_patch(patch)
    return patch,


def animate(i):
    patch.set_width(10)
    patch.set_height(1.0)
    patch.set_xy([x[i], y[i]])
    return patch,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=len(x),
                               interval=50,
                               blit=False)

plt.show()