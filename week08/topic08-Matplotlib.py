# Learning how to use matplotlib

import numpy as np
import matplotlib.pyplot as plt
    # We'll usee this to create a plot to use 
    # to draw points (markeers) in a diagram

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

    # plt.plot(xpoints, ypoints)
    # plt.show()

    # to add colours in the lines of the diagram

plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot(xpoints, ypoints, label="straight", color="blue")
plt.legend()

randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label= "random")

plt.show()

