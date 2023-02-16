import numpy as np
x=np.array([3, -1, 0, 1, 3, 2, 0, 1, 2, 1])
h=np.array([1, 1, 1])
print('\nx[n] =',x)
print('\nh[n] =',h)
Lx=len(x)
Lh=len(h)
LCl=Lx+Lh-1
L=int(input("\nEnter length of the segment:"))
Ll=L+Lh-1
if (Lx%L!=0):   x=np.pad(x,(0,L-Lx%L)) #for reshaping   
Lxp=len(x)
Nl=Lxp//L
yi=x.reshape(Nl,L)
yi=np.pad(yi,((0,0),(0,Ll-L)))
print('\n',yi)
hp=np.pad(h,(0,Ll-Lh))
hr=[]
for i in range(Ll):    hr=np.append(hr,np.roll(hp,i))
hr=hr.reshape(Ll,Ll)
hr=hr.T
print('\n',hr)
yi2=[]
for i in range(Nl):
    temp=[]
    temp=np.append(temp,yi[i])
    temp=temp.T
    yi2=np.append(yi2,hr@temp)
yi2=yi2.reshape(Nl,Ll)
print('\n',yi2)
sum=np.zeros(Nl*L+Lh-1)
print('\n')
for i in range(Nl):
    temp=[]
    temp=np.append(temp,np.pad(yi2[i],(i*L,(Nl*L+Lh-1)-(Ll+i*L))))
    print(temp)
    sum=sum+temp
print('\n',sum)
y=np.resize(sum,LCl)
print('\ny[n]=',y)