#import dependencies 
import numpy as np
from matplotlib import animation, rc
import matplotlib.pyplot as plt
from IPython.display import HTML
import matplotlib.patches as patches


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

patch = patches.Rectangle((0, 0), 0, 0,fc='y')


def init():
    ax.add_patch(patch)
    return patch, 


anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=len(x),
                               interval=50,
                               blit=True)

plt.show()
