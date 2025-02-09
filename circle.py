import numpy as np
import matplotlib.pyplot as plt

def circle(x, y, r):
    th = np.arange(0, 2*np.pi + np.pi/50, np.pi/50)
    xunit = r * np.cos(th) + x
    yunit = r * np.sin(th) + y
    line, = plt.plot(xunit, yunit, 'b')
    return line