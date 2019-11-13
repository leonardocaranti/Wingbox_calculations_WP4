# Include all the required libraries
import decimal
import matplotlib.pyplot as plt
from math import *

# Include all functions
import WingLoadFunction

# Calculate total loading
# NOTE here the mass of the fuel is devided by 2 because else the fuel tank is bigger then the span of the wing
# NOTE the positions of the engine i could not find hence they are random numbers for now
# NOTE the wing loading takes into account the weight of the wing, the fuel, the engines and the wingtip
wingLoadAr = WingLoadFunction.WingLoad(massFuel=104790/2, xEngine1=4, xEngine2=7, accuracy=1000)
print(wingLoadAr)

totalLoad = []
xAr = []
zAr = []
for i in range(0, len(wingLoadAr)):
    # Get the span position and the total load
    b = wingLoadAr[i][0]
    F = wingLoadAr[i][1]

    # append to the total load array
    totalLoad.append([b, F])

    # For the plotting
    xAr.append(b)
    zAr.append(F)

# optionally print the result
plt.scatter(xAr, zAr)
plt.show()

