from math import *
#engine bending diagram
Mint=[]
A=1
x=0
abcd=[]
zxcv=[]

span= 27.313
sweepgrad=15
sweeprad=sweepgrad*pi/180
Eg1_thrust=1000
Eg2_thrust=1000
Eg1_width_posit=7.
Eg2_width_posit=15.
Eg1_height_posit=0.
Eg1_height_posit=0.

Eg1Fx=sin(sweeprad)*Eg1_thrust
Eg2Fx=sin(sweeprad)*Eg2_thrust
Eg1Fy=cos(sweeprad)*Eg1_thrust
Eg2Fy=cos(sweeprad)*Eg1_thrust
#to test use these values
#Eg1Fy=10
#Eg2Fy=10

Xloclist=[]

while A==1:
    if x>=7:
        Eg1Fy=0
    if x>=15:
        Eg1Fy=0
        Eg2Fy=0
        
    lst=[]
    L1=Eg1_width_posit - x
    L2=Eg2_width_posit - x
    Me1=L1*Eg1Fy
    Me2=L2*Eg2Fy
    Mtemp=Me1+Me2

    abcd.append(Mtemp)
    zxcv.append(x)
    
    x=round(x,3)
    Mtemp=round(Mtemp,3)
    lst.append(Mtemp)
    lst.append(x)
    x=x+0.100000
    Mint.append(lst)
    if x>=27.313:
        break
print (Mint)

from matplotlib import pyplot as plt


plt.plot(zxcv,abcd,color='r')
plt.xlabel("Distance [m]")
plt.ylabel("Internal bending moment [Nm]")

plt.show()



