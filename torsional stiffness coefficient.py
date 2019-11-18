#TORSIONAL STIFFNESS COEFFICIENT

from math import *
from matplotlib import pyplot as plt
import numpy as np

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

span_tab =[]
t_stiffness_tab = []


for span_position in np.arange(0,b_2,0.01):
        rear_spar_h = -span_position*(rear_spar_h_root-rear_spar_h_tip)/b_2 + rear_spar_h_root
        front_spar_h = -span_position*(front_spar_h_root-front_spar_h_tip)/b_2 + front_spar_h_root
        dist = -span_position*(root_dist-tip_dist)/b_2 + root_dist

        A_m = ((rear_spar_h+front_spar_h)/2)*dist
        intdst = (front_spar_h/spar_thickness + rear_spar_h/spar_thickness + sqrt((front_spar_h - rear_spar_h)**2 + (dist*dist)) + dist)/t
        t_stiffness = (4*A_m*A_m*G)/(b_2*intdst)
        span_tab.append(span_position)
        t_stiffness_tab.append(t_stiffness)

plt.plot(span_tab,t_stiffness_tab)
plt.xlabel("Spanwise location from root [m]")
plt.ylabel("Torsional Stiffness T/Theta")
plt.show()

