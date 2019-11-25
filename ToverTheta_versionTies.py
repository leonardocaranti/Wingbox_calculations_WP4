from math import *
from matplotlib import pyplot as plt
import numpy as np



def TandTheta():
    
    from AeroMomentDistribution import Momentvectors
    from torsionalstiffnesscoefficient import torsionalstiffness

    # Internal torque distribution
    (x,y) = Momentvectors()

    summationtorques = []
    totaltorque = sum(y)
    (span_tab, t_stiffness_tab, t_stiffness_tab2) = torsionalstiffness()
    Theta_tab = []
    totaltheta = 0
    totaltorsionalstiffness = sum(t_stiffness_tab)
    print(len(t_stiffness_tab))
    
    for i in range(len(t_stiffness_tab)):
    
        summationtorques.append(totaltorque - y[i])
        totaltorque = totaltorque - y[i]    
        totaltorsionalstiffness = totaltorsionalstiffness - t_stiffness_tab[i]
        dthetas = []
        # Twist distribution over the span
        for n in range(i):

            dthetas.append(totaltorque/t_stiffness_tab[n])
    
        Theta = sum(dthetas)
        totaltheta = totaltheta + Theta
        Theta_tab.append(totaltheta)
        
            
        
    plt.plot(span_tab, summationtorques)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Total internal torque [Nm]")
    plt.show()

    plt.plot(span_tab, Theta_tab)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Angle of twist Theta [rad]")
    plt.show()
    
j = TandTheta()

