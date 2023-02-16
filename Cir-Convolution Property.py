import numpy as np

N1 = 6
N2 = 6
x1 = np.random.randint(9, size=N1)
x2 = np.random.randint(4, size=N2)

y = np.convolve(x1, x2)                 #Linear convolution

M = max(N1, N2)
yc = y[0:M]
overlap_idx = np.arange(len(y[M:]))
yc[overlap_idx] += y[M:]                #Circular convolution
fft = np.fft.fft(yc)
print(yc)

z1 = np.fft.fft(x1.flatten())
z2 = np.fft.fft(x2.flatten())
z = z1*z2
print(np.real(np.fft.ifft(z)))