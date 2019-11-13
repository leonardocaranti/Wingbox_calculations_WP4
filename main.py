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
xAr, zAr, M_Y = WingLoadFunction.WingLoad(massFuel=104790*0.588, accuracy=10000)

# optionally print the result
plt.plot(xAr, zAr, xAr, M_Y)
plt.show()

