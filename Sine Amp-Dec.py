import numpy as np
from math import pi
import matplotlib.pyplot as plt
x = np.array(range(400))
yx = []
ys = []
for t in x:
    yx.append(int(256*(1+(np.sin(2*pi*t/50)*np.exp(-t/100)))))
s = np.array(range(0, 400, 5))
for t in s:
    ys.append(yx[t]*((t % 10) > 0))
plt.step(x, yx)
plt.step(s, ys)
plt.show()
