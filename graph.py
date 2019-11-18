#graph calculation

import matplotlib.pyplot as plt

def force_diagrams(graph_name, force, xspan, moment=0):

    plt.suptitle(graph_name)

    plt.subplot(121)
    plt.plot(xspan,force)
    plt.title("Shear force diagram")
    plt.xlabel("x-coordinate span (m)")
    plt.ylabel("Shear force (N)")
    plt.grid()
    plt.axhline(y=min(force), lw=1 ,ls='dashed' ,color='#d62728')

    if not moment ==0:
        plt.subplot(122)
        plt.plot(xspan,moment)
        plt.title("Bending moment diagram")
        plt.xlabel("x-coordinate span (m)")
        plt.ylabel("Bending moment (Nm)")
        plt.grid()
        plt.axhline(y=max(moment), lw=1 ,ls='dashed' ,color='#d62728')

    plt.show()
