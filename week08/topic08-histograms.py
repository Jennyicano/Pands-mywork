# Learning about histograms

import numpy as np
import matplotlib.pyplot as plt

normData = np.random.normal(size=10000)

plt.hist(normData)
plt.show()

