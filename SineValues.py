import numpy as np
from math import pi
import matplotlib.pyplot as plt
x = np.arange(400)
s = np.arange(0, 400, 5)
yx = []
ys = []
for t in x:
    yx.append(int(256*(1+(np.sin(2*pi*t/50)*np.exp(-t/100)))))
for t in s:
    ys.append(yx[t]*((t % 10) > 0))
print(ys)
plt.step(x, yx)
plt.step(s, ys)
plt.show()
