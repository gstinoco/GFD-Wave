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

# Region data is loaded.
# Triangulation or unstructured cloud of points to work in.
regi = 'GIB'
cloud = '1'
# This region can be changed for any other triangulation or unstructured cloud of points on Regions/ or with any other region with the same file data structure.

# All data is loaded from the file
#mat = loadmat('Data/Clouds/' + region + '_' + cloud + '.mat')
mat = loadmat('Data/Clouds_Holes/' + regi + '_' + cloud + '.mat')

# Node data is saved
p   = mat['p']
tt  = mat['tt']
if tt.min() == 1:
    tt -= 1

# Number of Time Steps
t = 2000

# Wave coefficient
c = 1

# Approximation Type
cho = 0

# Boundary conditions
# The boundary conditions are defined as
#     f = \cos(\pi ct\sqrt{2})\sin(\pi x)\sin(\pi y)
#
# And its derivative
#     g = -(\pi c\sqrt{2})\sin(\pi x)\sin(\pi y)\sin(\pi ct\sqrt{2})

def fWAV(x, y, t, c, cho):
    if cho == 1:
        fun = np.cos(np.sqrt(2)*np.pi*c*t)*np.sin(np.pi*x)*np.sin(np.pi*y)
    else:
        fun = 0.2*np.exp((-(x - 0.5 - c*t)**2 - (y - 0.2 - c*t)**2)/.001)
    return fun

def gWAV(x, y, t, c, cho):
    if cho == 1:
        fun = -np.sqrt(2)*np.pi*c*np.sin(np.pi*x)*np.sin(np.pi*y)*np.sin(np.sqrt(2)*np.pi*c*t)
    else:
        fun = 0.2*np.exp((-(x - 0.5 - c*t)**2 - (y - 0.2 - c*t)**2)/.001)
    return fun

# Wave Equation in 2D computed on a unstructured cloud of points.
u_ap, u_ex, vec = Wave_2D.Cloud(p, fWAV, gWAV, t, c, cho)
#er = Errors.Cloud_Transient(p, vec, u_ap, u_ex)
#print('The maximum mean square error in the unstructured cloud of points is: ', er.max())
#Graph.Cloud_Transient(p, tt, u_ap, u_ex)
Graph.Cloud_Transient_1(p, tt, u_ap)
#Graph.Cloud_Transient_sav_1(p, tt, u_ap, regi + '_3_cloud.mp4')

u_ap, u_ex, vec = Wave_2D.Triangulation(p, tt, fWAV, gWAV, t, c, cho)
#er = Errors.Cloud_Transient(p, vec, u_ap, u_ex)
#print('The maximum mean square error in the triangulation is: ', er.max())
#Graph.Cloud_Transient(p, tt, u_ap, u_ex)
Graph.Cloud_Transient_1(p, tt, u_ap)
#Graph.Cloud_Transient_sav_1(p, tt, u_ap, regi + '_3_tri.mp4')

#Graph.Error(er)
#Graph.Cloud_Transient_Vid(p, tt, u_ap, u_ex, 'CAB1')