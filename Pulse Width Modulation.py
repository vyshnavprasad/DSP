import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 1, .001)
A = 2
I = (A/2)*np.cos(2*np.pi*3*t) + A/2
Ts = 20
y = []
y = np.zeros(len(t))

for i in range(len(t)//Ts):
    Start = Ts*i
    D = int((I[Start]/A)*Ts)
    y[Start:Start+D] = np.ones(D)

plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.subplot(2, 1, 1)
plt.plot(t, I)
plt.show()