import numpy as np
from math import pi
import matplotlib.pyplot as plt

Data = np.array([1, 0, 1, 1])
Data = np.repeat(5**(Data), 100)

time = np.linspace(0, 4, len(Data))

Carrier = np.sin(10*pi*time)
output = Carrier*Data

plt.plot(time, output)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
