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

# Analysing the wingbox on the x-z plane
t0 = time.time()
positions, forces = Liftplaneforce()
#force_diagrams(forces, positions)

pos_list, sh_load, bend_mom = int_load(forces, positions)
sh_load, bend_mom = list(sh_load[0]), list(bend_mom[0])

print(positions[0], positions[-1:-3])
print(sh_load[0], sh_load[-1:-3])
print(bend_mom[0], bend_mom[-1:-3])
t1 = time.time()
print("Took", round(t1-t0,1), "seconds")

force_diagrams(sh_load, positions, bend_mom)
