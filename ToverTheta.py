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
    (span_tab, t_stiffness_tab) = torsionalstiffness()
    Theta_tab = []
    totaltheta = 0
    for i in range(len(y)):
        summationtorques.append(totaltorque - y[i])
        totaltorque = totaltorque - y[i]
        
    
        # Twist distribution over the span
        Theta = totaltorque/t_stiffness_tab[i]
        totaltheta = totaltheta + Theta
        Theta_tab.append(totaltheta)

        
    plt.plot(x, summationtorques)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Total internal torque [Nm]")
    plt.show()

    plt.plot(x, Theta_tab)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Angle of twist Theta [rad]")
    plt.show()
    print(totaltorque)
j = TandTheta()

