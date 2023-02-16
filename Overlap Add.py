import numpy as np
X = np.array([1,2,3,4,4,3,2,1,0,1,1,2,3,4,5,2,1,2,0,1,2])
H = np.array([1,2,1])
Ls = 4          # = l
Lx = len(X)
Lh = len(H)     # = m
Lm = Ls+Lh-1    # Order for matrix

Xa = np.append(X, np.zeros((-Lx) % Ls))
Ra = len(Xa)//Ls  # Row count
Xa = Xa.reshape(Ra, Ls)

ROA = np.zeros([Ra, Ls*Ra+Lh-1])
for i in range(Ra):
    ROA[i][(i*Ls):(Lm+Ls*i)] = np.convolve(H, Xa[i])
print('Convolution by Overlap Add : \n',sum(ROA))