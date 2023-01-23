#


import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import seaborn as sbs

# sbs.set_style('darkgrid')
import numpy as np
from numpy.random import rand


x, y, c, s = rand(4, 100)

def remove_annotations():
    for child in plt.gca().get_children():
        if isinstance(child, matplotlib.text.Annotation):
            child.remove()

def add_annotation(x, y):
    text_location = (x - .08, y - .08)
    message = 'x={:.3f} y={:.3f}'.format(x, y)
    plt.gca().annotate(
        message, xy=(x,y), xytext=text_location,
        bbox=dict(facecolor='red', alpha=0.5)
    )

def on_pick(event):
    ind = event.ind
    x_val = np.take(x, ind)[0]
    y_val = np.take(y, ind)[0]
    # remove_annotations()
    add_annotation(x_val, y_val)
    plt.draw()
    # print('onpick3 scatter:', ind, np.take(x, ind), np.take(y, ind), x_val, y_val)

plt.scatter(x, y, 100*s, c, picker=.1)
fig = plt.gcf()
fig.canvas.mpl_connect('pick_event', on_pick)
# fig.canvas.mpl_connect('axes_enter_event', enter_axes)
# fig.canvas.mpl_connect('axes_leave_event', leave_axes)

plt.show()
