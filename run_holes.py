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
c = 1

# Approximation Type
cho = 1

# Names of the regions
regions = ['CAB','CUA','CUI','DOW','ENG','GIB','HAB','MIC','PAT','ZIR']

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
        fun = np.cos(np.sqrt(2)*np.pi*c*t)*np.sin(np.pi*x)*np.sin(np.pi*y)
    else:
        fun = 0.2*np.exp((-(x - r[0] - c*t)**2 - (y - r[1] - c*t)**2)/.001)
    return fun

def gWAV(x, y, t, c, cho, r):
    if cho == 1:
        fun = -np.sqrt(2)*np.pi*c*np.sin(np.pi*x)*np.sin(np.pi*y)*np.sin(np.sqrt(2)*np.pi*c*t)
    else:
        fun = 0.2*np.exp((-(x - r[0] - c*t)**2 - (y - r[1] - c*t)**2)/.001)
    return fun

for reg in regions:
    regi = reg
    print('Region:', regi)

    # Initial Drop
    if regi == 'CAB':
        r = np.array([0.7, 0.2])
    if regi == 'CUA':
        r = np.array([0.7, 0.7])
    if regi == 'CUI':
        r = np.array([0.7, 0.3])
    if regi == 'DOW':
        r = np.array([0.6, 0.2])
    if regi == 'ENG':
        r = np.array([0.3, 0.5])
    if regi == 'GIB':
        r = np.array([0.7, 0.3])
    if regi == 'HAB':
        r = np.array([0.8, 0.8])
    if regi == 'MIC':
        r = np.array([0.8, 0.45])
    if regi == 'PAT':
        r = np.array([0.8, 0.8])
    if regi == 'ZIR':
        r = np.array([0.7, 0.4])

    for me in sizes:
        print('\tSize:', me)
        cloud = me

        # Number of Time Steps
        if cloud == '1' or cloud == '2' or cloud == '3':
            t = 1000
        else:
            t = 1000
        
        # All data is loaded from the file
        mat = loadmat('Data/Holes/' + regi + '_' + cloud + '.mat')
        nce = 'Results/Clouds_Holes/Explicit/' + regi + '_' + cloud + '.mp4'
        nci = 'Results/Clouds_Holes/Implicit/' + regi + '_' + cloud + '.mp4'
        nte = 'Results/Triangulations_Holes/Explicit/' + regi + '_' + cloud + '.mp4'
        nti = 'Results/Triangulations_Holes/Implicit/' + regi + '_' + cloud + '.mp4'
        nom = 'Results/' + regi + '_' + cloud

        # Node data is saved
        p   = mat['p']
        tt  = mat['tt']
        if tt.min() == 1:
            tt -= 1

        print('\t\tCloud')
        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=False, tt=tt, lam=1.00)
        er = Errors.Cloud(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the explicit scheme (1.00) is: ', er.max())
        Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nce)

        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=False, tt=tt, lam=0.50)
        er = Errors.Cloud(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the implicit scheme (0.50) is: ', er.max())
        Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nci)

        print('\t\tTriangulation')
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=1.00)
        er = Errors.Cloud(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the explicit scheme (1.00) is: ', er.max())
        Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nte)
 
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.50)
        er = Errors.Cloud(p, vec, u_ap, u_ex)
        print('\t\t\tThe maximum mean square error with the implicit scheme (0.50) is: ', er.max())
        Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nti)