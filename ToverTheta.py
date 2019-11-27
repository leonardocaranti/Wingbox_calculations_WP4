from math import *
from matplotlib import pyplot as plt
import numpy as np

L = 28.74 	#[m]
fus_diam = 6.01 #[m]

def TandTheta():
    from AeroMomentDistribution import Momentvectors
    from torsionalstiffnesscoefficient import torsionalstiffness

    # Internal torque distribution
    (x, y) = Momentvectors()

    summationtorques, t_over_theta = [], []
    totaltorque = sum(y)
    (span_tab, t_stiffness_tab) = torsionalstiffness()
    Theta_tab = []
    totaltheta = 0
    t_dz = 0
    for i in range(len(y)):
        summationtorques.append(totaltorque - y[i])

        if i == 0:
            t_dz = 0

        else:
            t_dz += (totaltorque - y[i]) * (x[i] - x[i - 1])

        # Twist distribution over the span
        Theta = t_dz / (t_stiffness_tab[i])
        Theta_tab.append(Theta*180/pi)

        if Theta == 0:
            t_over_theta.append(0)

        if not Theta ==0:
            t_over_theta.append((totaltorque - y[i])/Theta)

        totaltorque = totaltorque - y[i]

    x_from_fus, t_over_theta_from_fus = [], []
    for i in range(len(x)):
        if x[i] > fus_diam:
            x_from_fus.append(x[i])
            t_over_theta_from_fus.append(t_over_theta[i])


    # Plots
    plt.subplot(221)
    plt.plot(x, summationtorques)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Total internal torque [Nm]")
    plt.grid()
    if abs(max(summationtorques))>abs(min(summationtorques)):
        crit_val = max(summationtorques)
    else:
        crit_val = min(summationtorques)
    plt.axhline(y=crit_val, lw=1 ,ls='dashed' ,color='#d62728')

    plt.subplot(222)
    plt.plot(x, Theta_tab)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Angle of twist Theta [deg]")
    plt.grid()
    if abs(max(Theta_tab))>abs(min(Theta_tab)):
        crit_val = max(Theta_tab)
    else:
        crit_val = min(Theta_tab)
    plt.axhline(y=crit_val, lw=1 ,ls='dashed' ,color='#d62728')

    plt.subplot(223)
    plt.plot(span_tab, t_stiffness_tab)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Torsional stiffness per unit length [Nm/(rad/m)]")
    plt.grid()
    if abs(max(t_stiffness_tab))>abs(min(t_stiffness_tab)):
        crit_val = max(t_stiffness_tab)
    else:
        crit_val = min(t_stiffness_tab)
    plt.axhline(y=crit_val, lw=1 ,ls='dashed' ,color='#d62728')

    plt.subplot(224)
    plt.plot(x_from_fus, t_over_theta_from_fus)
    plt.xlabel("Spanwise location from root (fuselage integration) [m]")
    plt.ylabel("Torsional stiffness [Nm/rad]")
    plt.grid()
    if abs(max(t_over_theta_from_fus))>abs(min(t_over_theta_from_fus)):
        crit_val = max(t_over_theta_from_fus)
    else:
        crit_val = min(t_over_theta_from_fus)
    plt.axhline(y=crit_val, lw=1 ,ls='dashed' ,color='#d62728')
    plt.show()

TandTheta()
