# Wingbox_calculations_WP4
#graph calculation

import numpy as np
import matplotlib.pyplot as plt

def force_diagrams(force, xspan):
    plt.plot(xspan,force)
    plt.xlabel("x-coordinate span (m)")
    plt.ylabel("shear force (kN)")
    plt.show()
