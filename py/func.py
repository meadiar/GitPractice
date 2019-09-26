#
def pdmelt(tcurr):
    t1 = 1604. # solidus T
    t2 = 1650. # liquidus T
#
    fb = (tcurr - t1)/(t2 - t1)
    fr = 1. - fb
    return fb, fr
