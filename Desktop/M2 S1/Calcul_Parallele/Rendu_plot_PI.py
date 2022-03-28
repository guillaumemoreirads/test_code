# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:18:01 2022

@author: Guillaume
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# =============================================================================
# # Calcul parallèle // Plan d'experience
# =============================================================================
# =============================================================================

'''
REDUCTION
'''
x = np.linspace(0,18,18)
y = x

# =============================================================================
# # N1 = 30 000 000 #
# =============================================================================

# Temps elapsed

Threads_1  = 1
Threads_2  = 3.5/1.859
Threads_4  = 3.5/9.600E-01
Threads_6  = 3.5/7.050E-01
Threads_8  = 3.5/5.250E-01
Threads_10 = 3.5/4.200E-01
Threads_13 = 3.5/3.680E-01
Threads_16 = 3.5/3.740E-01

Threads_N1 = [Threads_1,Threads_2,Threads_4,Threads_6,Threads_8,Threads_10,Threads_13,Threads_16]

# =============================================================================
# # 2N1 = 60 000 000 #
# =============================================================================

Threads_1_1  = 1
Threads_2_1  = 4/1.858
Threads_4_1  = 4/9.910E-01
Threads_6_1  = 4/6.510E-01
Threads_8_1  = 4/5.130E-01
Threads_10_1 = 4/4.200E-01
Threads_13_1 = 4/3.740E-01
Threads_16_1 = 4/3.310E-01

Threads_2N1 = [Threads_1_1,Threads_2_1,Threads_4_1,Threads_6_1,Threads_8_1,Threads_10_1,Threads_13_1,Threads_16_1]


# =============================================================================
# # 4N1 = 120 000 000 #
# =============================================================================

Threads_1_2  = 1
Threads_2_2  = 3.5/1.903
Threads_4_2  = 3.5/9.670E-01
Threads_6_2  = 3.5/6.930E-01
Threads_8_2  = 3.5/5.250E-01
Threads_10_2 = 3.5/4.150E-01
Threads_13_2 = 3.5/3.580E-01
Threads_16_2 = 3.5/3.020E-01

Threads_4N1 = [Threads_1_2,Threads_2_2,Threads_4_2,Threads_6_2,Threads_8_2,Threads_10_2,Threads_13_2,Threads_16_2]

nb_threads = [1,2,4,6,8,10,13,16]

plt.figure(1)
plt.plot(x,y, label = 'Speed idéal')
plt.plot(nb_threads,Threads_N1, label = 'N1')
plt.plot(nb_threads,Threads_2N1, label = '2N1')
plt.plot(nb_threads,Threads_4N1, label = '4N1')

plt.title(' SpeedUp (en fonction du nombre de Threads) pour REDUCTION ')
plt.xlabel('Threads')
plt.ylabel('SpeedUP')
plt.legend()
plt.show()

## pour affiner les courbes on peut faire des moyennes des temps pour une même simulation
## abel peut être surchagé si tout le monde run en même temps

'''
SCHEDULE (RUNTIME) (à prendre en compte à chaque version ou non)
'''


'''
ATOMIC
'''
x = np.linspace(0,18,18)
y = x

# =============================================================================
# # N1 = 30 000 000 #
# =============================================================================

# Temps elapsed

Threads_1_b  = 1
Threads_2_b  = 3.741/1.874
Threads_4_b  = 3.887/9.740E-01
Threads_6_b  = 4.203/7.190E-01
Threads_8_b  = 4.179/5.250E-01
Threads_10_b = 4.388/4.950E-01
Threads_13_b = 4.640/4.080E-01
Threads_16_b = 5.261/3.550E-01

Threads_N1 = [Threads_1_b,Threads_2_b,Threads_4_b,Threads_6_b,Threads_8_b,Threads_10_b,Threads_13_b,Threads_16_b]

# =============================================================================
# # 2N1 = 60 000 000 #
# =============================================================================

Threads_1_a  = 1
Threads_2_a  = 3.827/1.941
Threads_4_a  = 3.857/9.670E-01
Threads_6_a  = 4.006/6.710E-01
Threads_8_a  = 4.265/5.430E-01
Threads_10_a = 4.553/4.810E-01
Threads_13_a = 5.119/4.240E-01
Threads_16_a = 5.160/3.370E-01

Threads_2N1 = [Threads_1_a,Threads_2_a,Threads_4_a,Threads_6_a,Threads_8_a,Threads_10_a,Threads_13_a,Threads_16_a]


# =============================================================================
# # 4N1 = 120 000 000 #
# =============================================================================

Threads_1_c  = 1
Threads_2_c  = 3.792/1.901
Threads_4_c  = 3.859/9.780E-01
Threads_6_c  = 3.950/6.620E-01
Threads_8_c  = 4.096/5.130E-01
Threads_10_c = 4.512/4.580E-01
Threads_13_c = 4.505/3.490E-01
Threads_16_c = 4.704/3.010E-01

Threads_4N1 = [Threads_1_c,Threads_2_c,Threads_4_c,Threads_6_c,Threads_8_c,Threads_10_c,Threads_13_c,Threads_16_c]

nb_threads = [1,2,4,6,8,10,13,16]

plt.figure(2)
plt.plot(x,y, label = 'Speed idéal')
plt.plot(nb_threads,Threads_N1, label = 'N1')
plt.plot(nb_threads,Threads_2N1, label = '2N1')
plt.plot(nb_threads,Threads_4N1, label = '4N1')

plt.title(' SpeedUp (en fonction du nombre de Threads) pour ATOMIC ')
plt.xlabel('Threads')
plt.ylabel('SpeedUP')
plt.legend()
plt.show()

'''
CRITICAL
'''
x = np.linspace(0,18,18)
y = x

# =============================================================================
# # N1 = 30 000 000 #
# =============================================================================

# Temps elapsed

Threads_1_e  = 1
Threads_2_e  = 3.772/1.887
Threads_4_e  = 4.180/1.117
Threads_6_e  = 4.163/7.100E-01
Threads_8_e  = 4.194/5.270E-01
Threads_10_e = 4.633/4.830E-01
Threads_13_e = 4.437/3.440E-01
Threads_16_e = 4.704/2.960E-01

Threads_N1 = [Threads_1_e,Threads_2_e,Threads_4_e,Threads_6_e,Threads_8_e,Threads_10_e,Threads_13_e,Threads_16_e]

# =============================================================================
# # 2N1 = 60 000 000 #
# =============================================================================

Threads_1_f  = 1
Threads_2_f  = 3.778/1.894
Threads_4_f  = 3.888/9.730E-01
Threads_6_f  = 4.053/6.840E-01
Threads_8_f  = 4.102/5.140E-01
Threads_10_f = 4.503/4.690E-01
Threads_13_f = 4.629/3.680E-01
Threads_16_f = 4.700/2.950E-01

Threads_2N1 = [Threads_1_f,Threads_2_f,Threads_4_f,Threads_6_f,Threads_8_f,Threads_10_f,Threads_13_f,Threads_16_f]


# =============================================================================
# # 4N1 = 120 000 000 #
# =============================================================================

Threads_1_g  = 1
Threads_2_g  = 3.712/1.901
Threads_4_g  = 3.964/1.000
Threads_6_g  = 4.066/6.880E-01
Threads_8_g  = 4.273/5.350E-01
Threads_10_g = 4.304/4.400E-01
Threads_13_g = 4.471/3.480E-01
Threads_16_g = 5.540/3.480E-01

Threads_4N1 = [Threads_1_g,Threads_2_g,Threads_4_g,Threads_6_g,Threads_8_g,Threads_10_g,Threads_13_g,Threads_16_g]

nb_threads = [1,2,4,6,8,10,13,16]

plt.figure(3)
plt.plot(x,y, label = 'Speed idéal')
plt.plot(nb_threads,Threads_N1, label = 'N1')
plt.plot(nb_threads,Threads_2N1, label = '2N1')
plt.plot(nb_threads,Threads_4N1, label = '4N1')

plt.title(' SpeedUp (en fonction du nombre de Threads) pour CRITICAL ')
plt.xlabel('Threads')
plt.ylabel('SpeedUP')
plt.legend()
plt.show()


