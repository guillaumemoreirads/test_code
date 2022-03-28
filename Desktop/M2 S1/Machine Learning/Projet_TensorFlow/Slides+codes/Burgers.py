# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:14:14 2021

@author: Guillaume
"""

import numpy as np
import matplotlib.pyplot as plt 
import sciann as sn
from numpy import pi
from sciann.utils.math import diff, sign, sin

x = sn.Variable('x')
t = sn.Variable('t')
u = sn.Functional('u', [t,x], 8*[20], 'tanh')

L1 = diff(u, t) + u*diff(u,x) - (0.01/pi)*diff(u, x, order=2)

#Inviscid Burgers eq_conservation#
# L1 = diff(u, t) + u*diff(u,x)

#Burgers advection form#
# L1 = diff(u, t) + 0.5*diff(u**2,x)

TOL = 0.001
C1 = (1-sign(t - TOL)) * (u + sin(pi*x))
C2 = (1-sign(x - (-1+TOL))) * (u)
C3 = (1+sign(x - ( 1-TOL))) * (u)

m = sn.SciModel([x, t], [L1, C1, C2, C3], loss_func = "mse")

x_data, t_data = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(0, 1, 100))

m.train([x_data, t_data], 4*['zero'], learning_rate=0.002, epochs=100, verbose=0)

x_test, t_test = np.meshgrid(np.linspace(-1, 1, 200), np.linspace(0, 1, 200))

u_pred = u.eval(m, [x_test, t_test])

fig = plt.figure(figsize=(3, 4))
plt.pcolor(x_test, t_test, u_pred, cmap='plasma')
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar()