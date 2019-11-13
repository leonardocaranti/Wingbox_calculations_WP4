import csv
import math
import matplotlib.pyplot as plt
import numpy as np

with open('Lift.csv', 'r') as f:
  reader = csv.reader(f)
  Lpts = list(reader)

maxload = 3.5
WTOW = 2820900
sweep = 29
sweeprad = math.radians(sweep)

Lscaled = []
Ltot = []
Lloc = []
xscaled = []
xsection = []
L2dlist = []

#print(Lpts)

i = 0
m = 0

while i in range(len(Lpts)):

    xspan = float(Lpts[i][0])
    xcorr = xspan/math.cos(sweeprad)
    xcenter = (xspan + float(Lpts[i-1][0]))/(2*math.cos(sweeprad))
    L2d = float(Lpts[i][1])
    L2dlist.append(L2d)

    #print(xspan,xcorr,xcenter)
    
    if m < 1:
        Lsec = L2d * (xcorr - 0)

    else:
        Lsec = L2d * (xcorr - float(Lpts[i-1][0])/math.cos(sweeprad))

    if xspan > 0 and xspan < 27.18:

        xscaled.append(xcenter)

        Lloc.append(Lsec)

        #xsection.append(xcorr - float(Lpts[i-1][0])/math.cos(sweeprad))

        #print(xcorr,float(Lpts[i-1][0])/math.cos(sweeprad))

        m = m + 1

    i = i + 1

scalefac = (WTOW * maxload)/sum(Lloc)

Lscaled = []

for i in range(len(Lloc)):

    lscaled = Lloc[i] * scalefac


    Lscaled.append(lscaled)

#print(sum(xsection))
print(sum(Lscaled))
plt.plot(xscaled,L2dlist)
plt.xlabel('Span')
plt.ylabel('Lift')
plt.show()
