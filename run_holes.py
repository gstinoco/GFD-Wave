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
import Wave_2D

# Wave coefficient
c = 1

# Number of Time Steps
t = 2000

# Approximation Type
cho = 0

# Names of the regions
regions = ['CANAL']#['CAB','CUA','CUI','DOW','ENG','GIB','HAB','MIC','PAT','ZIR']

# Sizes of the clouds
sizes = ['1', '2', '3','4']

# Boundary conditions

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
    if regi == 'CANAL':
        r = np.array([0.3, 0.8])

    for me in sizes:
        cloud = me

        # Number of Time Steps
        if cloud == '1':
            t = 1000
        elif cloud == '2':
            t = 5000
        elif cloud == '3':
            t = 10000
        elif cloud == '4':
            t = 15000
        else:
            t = 20000
        
        # All data is loaded from the file
        #mat = loadmat('Data/Clouds/' + region + '_' + cloud + '.mat')
        mat = loadmat('Data/Clouds_Holes/' + regi + '_' + cloud + '.mat')
        noc = 'Results/Clouds_Holes/' + regi + '_' + cloud + '.mp4'
        nob = 'Results/Triangulations_Holes/' + regi + '_' + cloud + '.mp4'

        # Node data is saved
        p   = mat['p']
        tt  = mat['tt']
        if tt.min() == 1:
            tt -= 1

        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r)
        #Graph.Cloud_Transient_1(p, tt, u_ap)
        Graph.Cloud_Transient_sav_1(p, tt, u_ap, noc)

        u_ap, u_ex, vec = Wave_2D.Triangulation(p, tt, fWAV, gWAV, t, c, cho, r)
        #Graph.Cloud_Transient_1(p, tt, u_ap)
        Graph.Cloud_Transient_sav_1(p, tt, u_ap, nob)