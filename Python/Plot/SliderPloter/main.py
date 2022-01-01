import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


# The parametrized function to be plotted
def f(x, a, b, c):
    return a*x**2 + b*x + c

t = np.linspace(-10, 10, 1000)

# Define initial parameters
init_a= 5
init_b = 3
init_c = 3

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = plt.plot(t, f(t, init_a, init_b, init_c), lw=2)
ax.set_xlabel('x')
ax.set_ylabel('y')

# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.45)

# Make a horizontal slider to control the frequency.
axa = plt.axes([0.12, 0.1, .78, 0.03])
a_slider = Slider(
    ax=axa,
    label='a',
    valmin=0,
    valmax=10,
    valinit=init_a,
)

axb = plt.axes([0.12, 0.2, .78, 0.03])
b_slider = Slider(
    ax=axb,
    label='b',
    valmin=0,
    valmax=10,
    valinit=init_b,
)

axc = plt.axes([0.12, 0.3, .78, 0.03])
c_slider = Slider(
    ax=axc,
    label='c',
    valmin=0,
    valmax=10,
    valinit=init_c,
)

"""
# Make a vertically oriented slider to control the amplitude
axamp = plt.axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)
"""

# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(t, a_slider.val, b_slider.val, c_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    a_slider.reset()
    b_slider.reset()
    c_slider.reset()
button.on_clicked(reset)

plt.show()