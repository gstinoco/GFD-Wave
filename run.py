# All the codes presented below were developed by:
#   Dr. Gerardo Tinoco Guerrero
#   Universidad Michoacana de San Nicolás de Hidalgo
#   gerardo.tinoco@umich.mx
#
# With the funding of:
#   National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT). México.
#   Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
#   Aula CIMNE Morelia. México
#
# Date:
#   January, 2023.
#
# Last Modification:
#   February, 2023.

import numpy as np
from scipy.io import loadmat
import Scripts.Graph as Graph
import Scripts.Errors as Errors
import Wave_2D

# Wave coefficient
c = 1

# Number of Time Steps
t = 2000

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
        cloud = me

        # Number of Time Steps
        if cloud == '1':
            t = 400
        elif cloud == '2':
            t = 1000
        elif cloud == '3':
            t = 2000
        else:
            t = 10000
        
        # All data is loaded from the file
        mat = loadmat('Data/Clouds/' + regi + '_' + cloud + '.mat')
        #mat = loadmat('Data/Clouds_Holes/' + regi + '_' + cloud + '.mat')
        noc = 'Results/Clouds/' + regi + '_' + cloud + '.mp4'
        nob = 'Results/Triangulations/' + regi + '_' + cloud + '.mp4'

        # Node data is saved
        p   = mat['p']
        tt  = mat['tt']
        if tt.min() == 1:
            tt -= 1

        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r)
        er = Errors.Cloud_Transient(p, vec, u_ap, u_ex)
        print('The maximum mean square error in the unstructured cloud of points is: ', er.max())
        #Graph.Cloud_Transient(p, tt, u_ap, u_ex)
        Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, noc)

        u_ap, u_ex, vec = Wave_2D.Triangulation(p, tt, fWAV, gWAV, t, c, cho, r)
        er = Errors.Cloud_Transient(p, vec, u_ap, u_ex)
        print('The maximum mean square error in the triangulation is: ', er.max())
        #Graph.Cloud_Transient(p, tt, u_ap, u_ex)
        Graph.Cloud_Transient_sav(p, tt, u_ap, u_ex, nob)

        #Graph.Error(er)