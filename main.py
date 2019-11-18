from VectorlistLiftplane import *
from internal_force_calculations import *
from graph import *
import time

"""
# Include all functions
import WingLoadFunction

xAr, zAr, M_Y = WingLoadFunction.WingLoad(massFuel=104790*0.588, accuracy=10000)

# optionally print the result
plt.plot(xAr, zAr, xAr, M_Y)
plt.show()
"""

t0 = time.time()
# Analysing the wingbox on the x-z plane
positions, forces = Liftplaneforce()
#force_diagrams(forces, positions)

pos_list, sh_load, bend_mom = int_load(forces, positions)

t1 = time.time()
print("Took", round(t1-t0,1), "seconds")

force_diagrams("Internal force diagrams in the lift-plane", sh_load, pos_list, bend_mom)

# Analysing the wingbox on the y-z plane

