import numpy as np
from math import pi
import matplotlib.pyplot as plt

time = np.arange(0, 4, 0.001)
Carrier = np.sin(20*pi*time)
Amplitude = np.exp(2*time)
output = Carrier*Amplitude

plt.plot(time, output)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
