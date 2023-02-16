import numpy as np
X = np.array([3, -1, 0, 1, 3, 2, 0, 1, 2, 1])
H = np.array([1, 1, 1])
Xe = 6  # 7
Lx = len(X)  # 21
Lh = len(H)  # 3
Xc = int(np.ceil(Lx//Xe))  # 3
La = Xe + Lh - 1  # 9
H = np.append(H, np.zeros(La-Lh))

XA = np.append(X, np.zeros((-Lx) % Xe))
XA = XA.reshape(Xc, Xe)
XOA = np.zeros([Xc, La, La])
for i in range(Xc):
    XOA[i][0][0:Xe] = XA[i]
    for j in range(1, La):
        XOA[i][j][:] = np.roll(XOA[i][j-1][:], 1)
ROA = np.zeros([Xc, Lx+Lh-1])
for i in range(Xc):
    ROA[i][(i*Xe):(i*Xe+La)] = ((XOA[i].T) @ H.T)[:]
print("Convolution by Overlap Add : \n" + str(sum(ROA)))
