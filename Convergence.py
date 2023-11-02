"""
All the codes presented below were developed by:
    Dr. Gerardo Tinoco Guerrero
    Universidad Michoacana de San Nicolás de Hidalgo
    gerardo.tinoco@umich.mx

With the funding of:
    National Council of Humanities, Sciences and Technologies, CONACyT (Consejo Nacional de Humanidades, Ciencias y Tecnologías, CONAHCyT). México.
    Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
    Aula CIMNE-Morelia. México

Date:
    November, 2022.

Last Modification:
    March, 2023.
"""

import numpy as np
from scipy.io import loadmat
from scipy.io import savemat
import Scripts.Graph as Graph
import Scripts.Errors as Errors
import Wave_2D

# Wave coefficient
c = 1

# Approximation Type
cho = 1

# Names of the regions
regions = ['CUA','ENG','HAB','PAT']

# Sizes of the clouds
sizes = [1, 2, 3, 4]
#sizes = [2]

# Times
times = [1]
#times = [1, 2, 3, 4]

# Boundary conditions
# The boundary conditions are defined as
#     f = \cos(\pi c t\sqrt{2})\sin(\pi x)\sin(\pi y)
#
# And its derivative
#     g = -(\pi c \sqrt{2})\sin(\pi c t\sqrt{2})\sin(\pi x)\sin(\pi y)

def fWAV(x, y, t, c, cho, r):
    fun = np.cos(np.sqrt(2)*np.pi*c*t)*np.sin(np.pi*x)*np.sin(np.pi*y)
    return fun

def gWAV(x, y, t, c, cho, r):
    fun = 0
    return fun

for reg in regions:
    regi = reg
    print('Region:', regi)

    r = np.array([0, 0])
    
    for me in sizes:
        cloud = str(me)

        for ti in times:
            if ti == 1:
                t = 100
            if ti == 2:
                t = 200
            if ti == 3:
                t = 300
            if ti == 4:
                t = 400
        
            # All data is loaded from the file
            mat = loadmat('Data/Clouds/' + regi + '_' + cloud + '_n.mat')

            # Node data is saved
            p   = mat['p']
            tt  = mat['tt']
            if tt.min() == 1:
                tt -= 1
        
            # Wave Equation in 2D computed on a unstructured cloud of points.
            u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.25)
            er = Errors.Cloud(p, vec, u_ap, u_ex)
        
            print('\tThe mean square error with', len(p[:,0]), 'nodes is: ', er.mean())
            #print('\tThe mean square error with \Delta t = ', 1/t, 'is: ', er.mean())