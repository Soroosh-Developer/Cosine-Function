import matplotlib.pyplot as plt
import numpy as np

Fs = 8000
f = 3
sample = 8000
x = np.arange(sample)
y = np.cos(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
