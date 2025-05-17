# -*- coding: utf-8 -*-
"""
Created on Tue May 13 04:02:34 2025

@author: liamr
"""

import numpy as np
import matplotlib.pyplot as plt

import astropy.units as u
import astropy.constants as const

from scipy.optimize import curve_fit as fit


def linear(x,m,b):
    return m*x+b

 
t,T,v=np.loadtxt("BBDATA.txt",skiprows=5,unpack=True)

T+=273.15

Tm=np.argmax(T)
tup=t[:Tm]
Tup=T[:Tm]
vup=v[:Tm]
xup=Tup**4-T[0]**4

td=t[Tm:]
Td=T[Tm:]
vd=v[Tm:]
xd= Td**4-T[0]**4

plt.plot(xup,vup)
plt.plot(xd,vd)
plt.show()

parup,covup=fit(linear,xup,vup)

plt.plot(xup,linear(xup,parup[0],parup[1]),label=f"{parup[0]:2g}$(T^4-T_0^4)$ + {parup[1]:2f}")

pard,covd=fit(linear,xd,vd)

plt.plot(xd,linear(xd,pard[0],pard[1]),label=f"{pard[0]:2g}$(T^4-T_0^4)$ + {pard[1]:2f} ")

plt.xlabel("$T^4-T_0^4$")
plt.ylabel("$mV$")
plt.ylabel

plt.legend()




x=T**4-T[0]**4


'''plt.plot(x,v)
plt.plot(x,0.6/2e10*x-0.03)
plt.plot(x,0.6/2e10*x+0.05)
plt.plot(x,0.6/2e10*x+0.12)
#plt.plot(x,0.45/3e8*x+0.32)'''

