#TORSIONAL STIFFNESS COEFFICIENT

from math import *
from matplotlib import pyplot as plt
import numpy as np
from moment_of_inertia import *

# Tip
rear_spar_h_tip = 0.2324
front_spar_h_tip = 0.2534
tip_dist = 0.891

# Root
rear_spar_h_root = 0.8606
front_spar_h_root = 0.9386
root_dist = 3.3

#span_position = 13 #[number of m from the root chord]
spar_thickness = 0.03 		#[m]
t = 0.005 			#[m]
G = 28000000000
L = 28.74 	#[m]
b_2 = 28.74 		#[m]



def torsionalstiffness():
        span_tab = []
        t_stiffness_tab = []
        for span_position in np.arange(0,b_2,0.01):

                t, theta, dist, front_spar_h, rear_spar_h, stringer_height, stringer_thickness = initial_values(span_position)

                A_m = ((rear_spar_h+front_spar_h)/2)*dist
                intdst = (front_spar_h/t + rear_spar_h/t + sqrt((front_spar_h - rear_spar_h)**2 + (dist*dist)) + dist)/t
                t_stiffness = (4*A_m*A_m*G)/(intdst)
                span_tab.append(span_position)
                t_stiffness_tab.append(t_stiffness)

        return span_tab, t_stiffness_tab



