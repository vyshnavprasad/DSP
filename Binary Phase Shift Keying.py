import numpy as np
from math import pi
import matplotlib.pyplot as plt

Data = np.array([1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,])
time = np.arange(0, len(Data), .01)
Data = np.repeat(Data, 100)
Phase = (-1)**(Data<1) 
Carrier = np.sin(4*pi*time)
Output = Carrier * Phase

plt.subplot(2,1,1)
plt.plot(time, Data) 
plt.subplot(2, 1, 2)
plt.plot(time, Output) 
plt.show()