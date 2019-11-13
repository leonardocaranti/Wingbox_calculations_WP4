def Momentvectors

    from LiftDistribution import Liftvectors()

    (xspan,lvec) = Liftvectors()

    centpos = somefunction

    mvec = []

    def cppos(x):
        xcp = .37 - x*(.37-.15)/28.74
        return xcp
        

    for i in len(xspan):
        lloc = lvec[i]
        span = xspan[i]

        marm = centpos - cppos(span)
        mloc = lloc * marm

        mvec.append(mloc)

    return(xspan,mvec)

    
    
    
