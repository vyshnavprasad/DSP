import numpy as np
from math import pi
import matplotlib.pyplot as plt

f1 = 5
f2 = 10
Tfinal = 1
time = np.arange(0, Tfinal, .001)
f = f1 + ( ((f2-f1)/Tfinal) * time )         #frequency array.(increasing from f1 to f2)
output = np.sin(2*pi*f*time)

plt.plot(time, output)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()