import numpy as np
from func import *

fthermo = open('thermohis.dat','r')
l1 = fthermo.readline()
l2 = fthermo.readline()
tm1 = float(l1.split()[0]) # time of 1st line
tm2 = float(l2.split()[0]) # time of 2nd line
tstart = float(l1.split()[1]) # temperature 1st
tend = float(l2.split()[1]) # temperature 2nd


fal = 0.
fbe = 0.
fma = 0. # vol fraction of alpha prime
fraw = 1. # powder
flg = True # first time powder melt

ms = 650.
tmt = 410. # critical heat or cooling rate
tsol = 1604. # solidus T
tliq = 1650. # liquidus T

dt = 0.1
rate = (tend - tstart) /(tm2 - tm1)
Tinc = abs(dt*rate)
while Tinc >= abs(tliq-tsol)*0.4:
    print('too large time increment, divide by 2')
    dt = dt/2
    Tinc = dt*rate

tn0 = tm1 # the temperature before increment
tn1 = tm1 + dt*rate # the temperature after increment

# from powder to liquid or beta
if flg:
   print(dt)
   fraw0 = 0.
   fbe0 = 0.
   while tn1 < tliq + Tinc:
     if tn1 < tsol:
         fraw0, feb0 = 1., 0.
         tn1 = tsol
         print(tn1, fraw0, fbe0)
         tn1 += Tinc
         continue
     elif tn1 >= tliq:
         fraw0,fbe0 = 0., 1.0
         tn1 = tliq
         print(tn1, fraw0, fbe0)
         tn1 += Tinc
         continue
     else:
         fraw0, fbe0 = pdmelt(tn1)
         print(tn1, fraw0, fbe0)
         tn1 += Tinc
         continue
#
# without powder
else:

   if rate >= 0. :
       tn1 = 0.

   else:
       tn1 = 0.

def pdmelt(tcurr):
    t1 = 1604. # solidus T
    t2 = 1650. # liquidus T
#
    if tcurr >= t2:
        fr = 0.
        fb = 1.
    elif tcurr <= t1:
        fr = 1.
        fb = 0.
    else:
        fb = (tcurr - t1)/(t2 - t1)
        fr = 1. - fb
    return fr,fb

