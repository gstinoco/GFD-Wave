"""
All the codes presented below were developed by:
    Dr. Gerardo Tinoco Guerrero
    Universidad Michoacana de San Nicolás de Hidalgo
    gerardo.tinoco@umich.mx

With the funding of:
    National Council of Humanities, Sciences and Technologies, CONAHCyT (Consejo Nacional de Humanidades, Ciencias y Tecnologías, CONAHCyT). México.
    Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
    Aula CIMNE-Morelia. México

Date:
    November, 2022.

Last Modification:
    November, 2023.
"""

import os
import numpy as np
import tarfile
from scipy.io import loadmat
from scipy.io import savemat
import Scripts.Graph as Graph
import Scripts.Errors as Errors
import Wave_2D

# Wave coefficient
c = 1

# Approximation Type
cho = 0

# Names of the regions
regions = ['CAB', 'CUA', 'CUI', 'DOW', 'ENG', 'GIB', 'HAB', 'MIC', 'PAT', 'ZIR']

# Sizes of the clouds
sizes = [1, 2, 3]

# Boundary conditions
# The boundary conditions are defined as
#     f = \cos(\pi ct\sqrt{2})\sin(\pi x)\sin(\pi y)
#
# And its derivative
#     g = -(\pi c\sqrt{2})\sin(\pi x)\sin(\pi y)\sin(\pi ct\sqrt{2})

fWAV = lambda x, y, t, c, cho, r: 0.2*np.exp((-(x - r[0] - c*t)**2 - (y - r[1] - c*t)**2)/.0005)
gWAV = lambda x, y, t, c, cho, r: 0.2*np.exp((-(x - r[0] - c*t)**2 - (y - r[1] - c*t)**2)/.0005)

# Clouds or Holes
Holes = False

def make_tarfile(output_filename, source_file):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_file)

for reg in regions:

    # Initial Drop
    if reg == 'CAB':
        r = np.array([0.5, 0.6])
    if reg == 'CUA':
        r = np.array([0.7, 0.5])
    if reg == 'CUI':
        r = np.array([0.4, 0.6])
    if reg == 'DOW':
        r = np.array([0.4, 0.6])
    if reg == 'ENG':
        r = np.array([0.7, 0.3])
    if reg == 'GIB':
        r = np.array([0.2, 0.4])
    if reg == 'HAB':
        r = np.array([0.8, 0.8])
    if reg == 'MIC':
        r = np.array([0.3, 0.3])
    if reg == 'PAT':
        r = np.array([0.8, 0.8])
    if reg == 'ZIR':
        r = np.array([0.7, 0.5])

    for me in sizes:
        cloud = str(me)

        print('Region: ' + reg + ', with size: ' + cloud)

        # Number of Time Steps
        t = 1000
        
        # All data is loaded from the file
        if Holes:
            mat = loadmat('Data/Holes/' + reg + '_' + cloud + '.mat')
        else:
            mat = loadmat('Data/Clouds/' + reg + '_' + cloud + '.mat')

        # Node data is saved
        p   = mat['p']
        tt  = mat['tt']
        if tt.min() == 1:
            tt -= 1

        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.75)
        mdic = {'u_ap': u_ap, 'p': p, 'tt': tt}

        if Holes:
            folder = 'Results/Example 3/Holes/' + reg
            if not os.path.exists(folder):
                os.makedirs(folder)
            Graph.Cloud_Transient_sav_1(p, tt, u_ap, folder + '/' + reg + '_' + cloud + '.mp4')
            #file_n = folder + '/' + reg + '_' + cloud + '.mat'
            #savemat(file_n, mdic)
            #make_tarfile(file_n + '.tar.gz', file_n)
        else:
            folder = 'Results/Example 3/Clouds/' + reg
            if not os.path.exists(folder):
                os.makedirs(folder)
            Graph.Cloud_Transient_sav_1(p, tt, u_ap, folder + '/' + reg + '_' + cloud + '.mp4')
            #file_n = folder + '/' + reg + '_' + cloud + '.mat'
            #savemat(file_n, mdic)
            #make_tarfile(file_n + '.tar.gz', file_n)

# Clouds or Holes
Holes = True

def make_tarfile(output_filename, source_file):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_file)

for reg in regions:

    # Initial Drop
    if reg == 'CAB':
        r = np.array([0.5, 0.6])
    if reg == 'CUA':
        r = np.array([0.7, 0.5])
    if reg == 'CUI':
        r = np.array([0.4, 0.6])
    if reg == 'DOW':
        r = np.array([0.4, 0.6])
    if reg == 'ENG':
        r = np.array([0.7, 0.3])
    if reg == 'GIB':
        r = np.array([0.2, 0.4])
    if reg == 'HAB':
        r = np.array([0.8, 0.8])
    if reg == 'MIC':
        r = np.array([0.3, 0.3])
    if reg == 'PAT':
        r = np.array([0.8, 0.8])
    if reg == 'ZIR':
        r = np.array([0.7, 0.5])

    for me in sizes:
        cloud = str(me)

        print('Region: ' + reg + ', with size: ' + cloud)

        # Number of Time Steps
        t = 1000
        
        # All data is loaded from the file
        if Holes:
            mat = loadmat('Data/Holes/' + reg + '_' + cloud + '.mat')
        else:
            mat = loadmat('Data/Clouds/' + reg + '_' + cloud + '.mat')

        # Node data is saved
        p   = mat['p']
        tt  = mat['tt']
        if tt.min() == 1:
            tt -= 1

        # Wave Equation in 2D computed on a unstructured cloud of points.
        u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho, r, implicit=True, triangulation=True, tt=tt, lam=0.75)
        mdic = {'u_ap': u_ap, 'p': p, 'tt': tt}

        if Holes:
            folder = 'Results/Example 3/Holes/' + reg
            if not os.path.exists(folder):
                os.makedirs(folder)
            Graph.Cloud_Transient_sav_1(p, tt, u_ap, folder + '/' + reg + '_' + cloud + '.mp4')
            #file_n = folder + '/' + reg + '_' + cloud + '.mat'
            #savemat(file_n, mdic)
            #make_tarfile(file_n + '.tar.gz', file_n)
        else:
            folder = 'Results/Example 3/Clouds/' + reg
            if not os.path.exists(folder):
                os.makedirs(folder)
            Graph.Cloud_Transient_sav_1(p, tt, u_ap, folder + '/' + reg + '_' + cloud + '.mp4')
            #file_n = folder + '/' + reg + '_' + cloud + '.mat'
            #savemat(file_n, mdic)
            #make_tarfile(file_n + '.tar.gz', file_n)