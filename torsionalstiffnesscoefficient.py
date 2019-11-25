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
    

    (x,y) = Momentvectors()
    span_tab = []
    t_stiffness_tab = []
    t_stiffness_tab2 = []
    x1 = 0
    for span_position in x:

        if span_position > 0:
            t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness = moi.initial_values(span_position)
            
            A_m = ((rear_spar_h+front_spar_h)/2)*dist
            intdst = (front_spar_h/t + rear_spar_h/t + sqrt((front_spar_h - rear_spar_h)**2 + (dist*dist)) + dist)/t
            t_stiffness = (4*A_m*A_m*G)/(abs(span_position-x1)*intdst)
            span_tab.append(span_position)
            t_stiffness_tab.append(t_stiffness)
            x1 = span_position


            t_stiffness2 = (4*A_m*A_m*G)/(intdst)
            t_stiffness_tab2.append(t_stiffness2/b_2)
    return(span_tab, t_stiffness_tab, t_stiffness_tab2)

(span_tab, t_stiffness_tab, t_stiffness_tab2) = torsionalstiffness()
plt.plot(span_tab,t_stiffness_tab2)
plt.title("Sectional torsional stiffness")
plt.xlabel("Spanwise location from root [m]")
plt.ylabel("Torsional stiffness T/Theta [N/rad]")
plt.show()

