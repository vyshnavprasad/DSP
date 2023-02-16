import numpy as np
import matplotlib.pyplot as plt

fm = 10
fs = 100
t = np.arange(0, 1, .001)
I = np.cos(2*np.pi*fm*t)
s = len(t)//fs

O = np.zeros(len(t))
for x in range(len(t)):
    O[x] = (I[x] if (x % s) == 0 else O[x-1])

plt.subplot(2, 1, 1)
plt.plot(t, I, 'b')
plt.subplot(2, 1, 2)
plt.plot(t, O, 'r')
plt.show()
