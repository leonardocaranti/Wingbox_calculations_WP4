from moment_of_inertia import *
from AeroMomentDistribution import Momentvectors
from matplotlib import pyplot as plt


L = 28.74 	#[m]
G = 28000000000

def newT():

    t_theta = []
    s_factor = 1.1
    (x, y) = Momentvectors()
    y = [b*s_factor for b in y]

    summationtorques, theta_tab, theta = [], [], 0
    totaltorque = sum(y)

    for i in range(len(y)):
        T = totaltorque - y[i]
        #summationtorques.append(T)
        if i == 0:
            theta = 0
        else:
            theta += T/(G*J(x[i]))*(x[i]-x[i-1])
        theta_tab.append(theta*180/pi)

        t_theta.append(G*J(x[i]))

        totaltorque = T

    print(theta_tab)
    print(x)

    plt.title("Twist angle distribution")
    plt.plot(x, theta_tab)
    plt.xlabel("Spanwise location from root [m]")
    plt.ylabel("Twist angle [deg]")
    plt.grid()
    if abs(max(theta_tab))>abs(min(theta_tab)):
        crit_val = max(theta_tab)
    else:
        crit_val = min(theta_tab)
    ind = theta_tab.index(crit_val)
    plt.axhline(y=crit_val, lw=1, ls='dashed', color='#d62728')
    plt.text(x[ind], crit_val, str(round(crit_val, 3)) + " [deg]")
    plt.show()

newT()