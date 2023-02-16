import numpy as np
X = np.array([1,2,3,4,4,3,2,1,0,1,1,2,3,4,5,2,1,2,0,1,2])
H = np.array([1,2,1])
Ls = 4          # = l
Lx = len(X)
Lh = len(H)     # = m
Lm = Ls+Lh-1    # Order for matrix

Rs = int(np.ceil(Lx/Ls))  # Row count
Xs = np.concatenate((np.zeros(Lh-1), X, np.zeros(Lm-(Lx%Ls))))
Xx = np.zeros([Rs, Lm])
for i  in range(Rs):
    Xx[i] = Xs[Ls*i : Ls*i+Lm]
    
ROS = np.zeros([Rs ,Lm+Lh-1])
for i in range(Rs):
    ROS[i] = np.convolve(H, Xx[i])
print("Convolution by Overlap Save: \n" , (ROS[:,-Lm:Lm]).flatten())