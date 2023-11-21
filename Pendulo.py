# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:40:13 2023

@author: hp
"""

import numpy as np
import matplotlib.pylab as plt
import math
# Código 1

def pendulo(tf,tm):
    g = 8
    L = 5
    s1 = (g/L)**(1/2)
    s2 = (g/L)**(1/2)
    c1 = 1
    c2 = 1
    tempo = [i*tm for i in range(int(tf/tm)+1)]
    theta = [c1*math.cos(s1*t)+c2*math.sin(s2*t) for t in tempo]
    plt.plot(tempo,theta)
    plt.title("Péndulo Ideal")
    plt.grid()
    plt.show()
    return(tempo,theta)
    
# Código 2

Tiempo,Resultado = pendulo(15,0.1)

g = 9.81
L = 10
s1 = (g/L)**(1/2)
s2 = (g/L)**(1/2)
c1 = 1
c2 = 1
Tempo = np.linspace(0,15,int(15/0.1+1))
Theta = c1*np.sin(s1*Tempo)+c2*np.cos(s2*Tempo)
plt.plot(Tempo,Theta)
plt.title("Solución del Péndulo con Numpy")
plt.grid()
plt.show()



