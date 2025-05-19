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
from scipy.stats import chisquare

def linear(x,m,b):
    return m*x+b

 
t,T,v=np.loadtxt("BBDATA.txt",skiprows=5,unpack=True)

T+=273.15


fig,ax=plt.subplots()
ax.plot(T,v)
ax.set_xlabel("T K")
ax.set_ylabel("Voltage mV")
fig.show()


Tm=np.argmax(T)
tup=t[:Tm]
Tup=T[:Tm]
vup=v[:Tm]
xup=Tup**4-T[0]**4

td=t[Tm:]
Td=T[Tm:]
vd=v[Tm:]
xd= Td**4-T[0]**4

fig1, ax1=plt.subplots()
ax1.plot(xup,vup)
ax1.plot(xd,vd)
fig1.show()

parup,covup=fit(linear,xup,vup)

ax1.plot(xup,linear(xup,parup[0],parup[1]),label=f"{parup[0]:2.2g}$(T^4-T_0^4)$ + {parup[1]:2.2g}")

pard,covd=fit(linear,xd,vd)

ax1.plot(xd,linear(xd,pard[0],pard[1]),label=f"{pard[0]:2.2g}$(T^4-T_0^4)$ + {pard[1]:2.2g} ")




ax1.set_xlabel("$T^4-T_0^4$")
ax1.set_ylabel("$mV$")

plt.legend()
plt.show()



print(parup,np.sqrt(np.diag(covup)))
print(chisquare(vup,linear(xup,parup[0],parup[1]),ddof=2))


print(pard,np.sqrt(np.diag(covd)))
print(chisquare(vd,linear(xd,pard[0],pard[1]),ddof=2))

