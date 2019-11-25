#TORSIONAL STIFFNESS COEFFICIENT

from math import *
from matplotlib import pyplot as plt
import numpy as np

def torsionalstiffness():

    import moment_of_inertia as moi 
    from AeroMomentDistribution import Momentvectors
    # Tip
    rear_spar_h_tip = 0.2324
    front_spar_h_tip = 0.2534
    tip_dist = 0.891

    # Root
    rear_spar_h_root = 0.8606
    front_spar_h_root = 0.9386
    root_dist = 3.3

    #span_position

    G = 28000000000             # Shear modulus of aluminium
    b_2 = 28.74 		#[m]

    span_tab =[]
    t_stiffness_tab = []

    (x,y) = Momentvectors()

    for span_position in x:
            t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness = moi.initial_values(span_position)
        
            A_m = ((rear_spar_h+front_spar_h)/2)*dist
            intdst = (front_spar_h/t + rear_spar_h/t + sqrt((front_spar_h - rear_spar_h)**2 + (dist*dist)) + dist)/t
            t_stiffness = (4*A_m*A_m*G)/(b_2*intdst)
            span_tab.append(span_position)
            t_stiffness_tab.append(t_stiffness)

    return(span_tab, t_stiffness_tab)

(span_tab, t_stiffness_tab) = torsionalstiffness()
plt.plot(span_tab,t_stiffness_tab)
plt.title("Torsional stiffness")
plt.xlabel("Spanwise location from root [m]")
plt.ylabel("Torsional stiffness T/Theta")
plt.show()
