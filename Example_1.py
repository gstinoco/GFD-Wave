"""
All the codes presented below were developed by:
    Dr. Gerardo Tinoco Guerrero
    Universidad Michoacana de San Nicolás de Hidalgo
    gerardo.tinoco@umich.mx

With the funding of:
    National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT). México.
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
c = np.sqrt(1/2)

# Approximation Type
cho = 1

# Names of the regions
regions = ['CUA','ENG','HAB','PAT']

# Sizes of the clouds
sizes = ['2']

# Boundary conditions
# The boundary conditions are defined as
#     f = \cos{\pi t}\sin{\pi(x + y)}
#
# And its derivative
#     g = -\pi\sin{\pi t}\sin{\pi(x + y)}

def fWAV(x, y, t, c, cho, r):
    fun = np.cos(np.pi*t)*np.sin(np.pi*(x+y))
    return fun

def gWAV(x, y, t, c, cho, r):
    fun = 0
    return fun

for reg in regions:
    regi = reg
    print('Region:', regi)

    r = np.array([0, 0])
    
    for me in sizes:
        cloud = me

        # Number of Time Steps
        t = 1000
        
        # All data is loaded from the file
        mat = loadmat('Data/Clouds/' + regi + '_' + cloud + '.mat')

        # Node data is saved
        p   = mat['p']
        tt  = mat['tt']
        if tt.min() == 1:
            tt -= 1
        
        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=1.00)
        er1 = Errors.Cloud_size(p, vec, u_ap, u_ex)
        #Graph.Cloud_Transient(p, tt, u_ap, u_ex)
 
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.75)
        er2 = Errors.Cloud_size(p, vec, u_ap, u_ex)

        tt  += 1
        mdic = {'u_ap': u_ap, 'u_ex': u_ex, 'p': p, 'tt': tt}
        savemat('Results/' + regi + '_1.mat', mdic)
        tt  -= 1

        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.50)
        er3 = Errors.Cloud_size(p, vec, u_ap, u_ex)
        
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.25)
        er4 = Errors.Cloud_size(p, vec, u_ap, u_ex)
        
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.00)
        er5 = Errors.Cloud_size(p, vec, u_ap, u_ex)
        
        print('\tThe mean square error with the explicit scheme (1.00) is: ', er1.mean())
        print('\tThe mean square error with the implicit scheme (0.75) is: ', er2.mean())
        print('\tThe mean square error with the implicit scheme (0.50) is: ', er3.mean())
        print('\tThe mean square error with the implicit scheme (0.25) is: ', er4.mean())
        print('\tThe mean square error with the implicit scheme (0.00) is: ', er5.mean())
        print('\n')
        print('\tThe last square error with the explicit scheme (1.00) is: ', er1[-1])
        print('\tThe last square error with the implicit scheme (0.75) is: ', er2[-1])
        print('\tThe last square error with the implicit scheme (0.50) is: ', er3[-1])
        print('\tThe last square error with the implicit scheme (0.25) is: ', er4[-1])
        print('\tThe last square error with the implicit scheme (0.00) is: ', er5[-1])