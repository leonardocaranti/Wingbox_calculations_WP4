# Include all the required libraries
import decimal
import matplotlib.pyplot as plt
from math import *

# Include all functions
import WingLoadFunction

xAr, zAr, M_Y = WingLoadFunction.WingLoad(massFuel=104790*0.588, accuracy=10000)

# optionally print the result
plt.plot(xAr, zAr, xAr, M_Y)
plt.show()

