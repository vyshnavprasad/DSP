import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5, 5, 101)                      #Impulse
y = []
for i in t:
    y.append(i==0)
plt.subplot(2, 4, 1)
plt.stem(t, y)
plt.title("Impulse(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

t = np.linspace(-5, 5, 101)                      #Unit Step
y = []
for i in t:
    y.append(i>0)
plt.subplot(2, 4, 2)
plt.plot(t, y)
plt.title("Unit Step(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

t = np.linspace(-5, 5, 101)                      #Unit Pulse
y = []
for i in t:
    y.append(0<=i<=1)
plt.subplot(2, 4, 3)
plt.plot(t, y)
plt.title("Unit Pulse(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

t = np.linspace(-2, 2, 101)                      #Rectangular
y = []
for i in t:
    y.append(np.abs(i)<.5)
plt.subplot(2, 4, 4)
plt.plot(t, y)
plt.title("Rectangular(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

t = np.linspace(-5, 5, 101)                      #unit Ramp
y = []
for i in t:
    y.append((0<i)*i)
plt.subplot(2, 4, 5)
plt.plot(t, y)
plt.title("Unit Ramp(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

t = np.linspace(-5, 5, 101)                      #Bipolar
y = []
for i in t:
    y.append((i>0) * (-1)**int(i%2))
plt.subplot(2, 4, 6)
plt.plot(t, y)
plt.title("Bipolar(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

t = np.linspace(-5, 5, 101)                      #Triangular
y = []
for i in t:
        y.append((i>0)* ((i%3)%1.5))
plt.subplot(2, 4, 7)
plt.plot(t, y)
plt.title("Triangular(54)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

# t = np.linspace(-5, 5, 101)  # Triangular
# y = []
# for i in t:
#     if i < 0:
#         y.append(0)
#     elif int((i/1) % 1) == 0:
#         y.append(i % 1)
#     else:
#         y.append(1 - (i % 1))
# plt.subplot(2, 4, 7)
# plt.plot(t, y)
# plt.title("Triangular(54)")
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")

t = np.linspace(-10, 10, 101)                      #Cosine
y = []
for i in t:
    y.append(np.sin(i))
plt.subplot(2, 4, 8)
plt.plot(t, y)
plt.title("Cosine(52)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

plt.show()