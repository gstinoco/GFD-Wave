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
c = 2

# Approximation Type
cho = 1

# Names of the regions
regions = ['Compare']

# Sizes of the clouds
sizes = ['1', '2', '3']

# Boundary conditions
# The boundary conditions are defined as
#     f = \cos(\pi ct\sqrt{2})\sin(\pi x)\sin(\pi y)
#
# And its derivative
#     g = -(\pi c\sqrt{2})\sin(\pi x)\sin(\pi y)\sin(\pi ct\sqrt{2})

def fWAV(x, y, t, c, cho, r):
    if cho == 1:
        fun = np.cos(np.pi*t)*np.sin(np.pi(x+y))
    else:
        fun = 0.2*np.exp((-(x - r[0] - c*t)**2 - (y - r[1] - c*t)**2)/.001)
    return fun

def gWAV(x, y, t, c, cho, r):
    if cho == 1:
        fun = -np.pi*np.sin(np.pi*t)*np.sin(np.pi(x+y))
    else:
        fun = 0.2*np.exp((-(x - r[0] - c*t)**2 - (y - r[1] - c*t)**2)/.001)
    return fun

for reg in regions:
    regi = reg
    print('Region:', regi)

    # Initial Drop
    r = np.array([0, 0])
    
    for me in sizes:
        print('\tSize:', me)
        cloud = me

        # Number of Time Steps
        if cloud == '1':
            t = 60
        elif cloud == '2':
            t = 600
        elif cloud == '3':
            t = 30
        else:
            t = 1000
        
        # All data is loaded from the file
        mat = loadmat('Data/Clouds/' + regi + '_' + cloud + '.mat')
        nce = 'Results/Clouds/Explicit/' + regi + '_' + cloud + '.mp4'
        nci = 'Results/Clouds/Implicit/' + regi + '_' + cloud + '.mp4'
        nte = 'Results/Triangulations/Explicit/' + regi + '_' + cloud + '.mp4'
        nti = 'Results/Triangulations/Implicit/' + regi + '_' + cloud + '.mp4'
        nom = 'Results/' + regi + '_' + cloud

        # Node data is saved
        x = mat['x']
        y = mat['y']
        p = np.hstack(x,y)
        if tt.min() == 1:
            tt -= 1

        print('\t\tCloud')
        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=False, tt=tt, lam=1.00)
        er = Errors.Cloud_size(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the explicit scheme (1.00) is: ', er.max())
        #Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nce)
 
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=False, tt=tt, lam=0.50)
        er = Errors.Cloud_size(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the implicit scheme (0.50) is: ', er.max())
        #Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nci)

        print('\t\tTriangulation')
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=1.00)
        er = Errors.Cloud_size(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the explicit scheme (1.00) is: ', er.max())
        #Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nte)
 
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.50)
        er = Errors.Cloud_size(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the implicit scheme (0.50) is: ', er.max())
        #Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nti)