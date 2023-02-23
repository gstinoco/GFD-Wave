# All the codes presented below were developed by:
#   Dr. Gerardo Tinoco Guerrero
#   Universidad Michoacana de San Nicolás de Hidalgo
#   gerardo.tinoco@umich.mx
#
# With the funding of:
#   National Council of Science and Technology, CONACyT (Consejo Nacional de Ciencia y Tecnología, CONACyT). México.
#   Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH). México
#   Aula CIMNE-Morelia. México
#
# Date:
#   November, 2022.
#
# Last Modification:
#   January, 2023.

# Graphics
# Some routines are defined in here in order to correctly Graph different kinds of results.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import moviepy.editor as mpy
from moviepy.video.io.bindings import mplfig_to_npimage

def Mesh_Static_sav(x, y, u_ap, u_ex, nom):
    t    = len(u_ex[0,0,:])
    step = int(np.ceil(t/2))
    min  = u_ex.min()
    max  = u_ex.max()
    T    = np.linspace(0,1,t)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[0])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_surface(x, y, u_ap[:,:,0], cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_surface(x, y, u_ex[:,:,0], cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '00.png'
    plt.savefig(nok)
    plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[step])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_surface(x, y, u_ap[:,:,step], cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_surface(x, y, u_ex[:,:,step], cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '05.png'
    plt.savefig(nok)
    plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_surface(x, y, u_ap[:,:,t-1], cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_surface(x, y, u_ex[:,:,t-1], cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '10.png'
    plt.savefig(nok)
    plt.close()


def Mesh_Transient(x, y, u_ap, u_ex):
    t    = len(u_ex[0,0,:])
    step = int(np.ceil(t/50))
    min  = u_ex.min()
    max  = u_ex.max()
    T    = np.linspace(0,1,t)
    
    for k in np.arange(0,t,step):
        fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)
        
        ax1.plot_surface(x, y, u_ap[:,:,k], cmap=cm.coolwarm)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')

        ax2.plot_surface(x, y, u_ex[:,:,k], cmap=cm.coolwarm)
        ax2.set_zlim([min, max])
        ax2.set_title('Theoretical Solution')

        plt.pause(0.01)
        plt.close()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    
    ax1.plot_surface(x, y, u_ap[:,:,t-1], cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')

    ax2.plot_surface(x, y, u_ex[:,:,t-1], cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')

    plt.pause(0.1)


def Mesh_Transient_sav(x, y, u_ap, u_ex, nom):
    t      = len(u_ex[0,0,:])
    step   = int(np.ceil(t/50))
    min    = u_ex.min()
    max    = u_ex.max()
    T      = np.linspace(0,1,t)
    frames = []
    
    for k in np.arange(0,t,step):
        fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)
        
        ax1.plot_surface(x, y, u_ap[:,:,k], cmap=cm.coolwarm)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')

        ax2.plot_surface(x, y, u_ex[:,:,k], cmap=cm.coolwarm)
        ax2.set_zlim([min, max])
        ax2.set_title('Theoretical Solution')

        frames.append(mplfig_to_npimage(fig))
        plt.close()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    
    ax1.plot_surface(x, y, u_ap[:,:,t-1], cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')

    ax2.plot_surface(x, y, u_ex[:,:,t-1], cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')

    frames.append(mplfig_to_npimage(fig))
    plt.close()

    animation = mpy.VideoClip(lambda t: frames[int(t * 10)], duration=len(frames)/10)
    animation.write_videofile(nom, fps=10, verbose=False, logger=None)


def Cloud_Static_sav(p, tt, u_ap, u_ex, nom):
    if tt.min() == 1:
        tt -= 1
    t    = len(u_ex[0,:])
    step = int(np.ceil(t/2))
    min  = u_ex.min()
    max  = u_ex.max()
    T    = np.linspace(0,1,t)

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[0])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,0], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,0], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '00.png'
    plt.savefig(nok)
    plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[step])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,step], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,step], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '05.png'
    plt.savefig(nok)
    plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '10.png'
    plt.savefig(nok)
    plt.close()


def Cloud_Transient(p, tt, u_ap, u_ex):
    if tt.min() == 1:
        tt -= 1
    t    = len(u_ex[0,:])
    step = int(np.ceil(t/50))
    min  = u_ex.min()
    max  = u_ex.max()
    T    = np.linspace(0,1,t)

    for k in np.arange(0,t,step):
        fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')
        
        ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,k], triangles=tt, cmap=cm.coolwarm)
        ax2.set_zlim([min, max])
        ax2.set_title('Theoretical Solution')

        plt.pause(0.01)
        plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)

    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')

    plt.pause(0.1)


def Cloud_Transient_sav(p, tt, u_ap, u_ex, nom):
    if tt.min() == 1:
        tt -= 1
    t      = len(u_ex[0,:])
    step   = int(np.ceil(t/50))
    min    = u_ex.min()
    max    = u_ex.max()
    T      = np.linspace(0,1,t)
    frames = []

    for k in np.arange(0,t,step):
        fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize = (8, 4))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')
        
        ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,k], triangles=tt, cmap=cm.coolwarm)
        ax2.set_zlim([min, max])
        ax2.set_title('Theoretical Solution')

        frames.append(mplfig_to_npimage(fig))
        plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)

    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    
    frames.append(mplfig_to_npimage(fig))
    plt.close()

    animation = mpy.VideoClip(lambda t: frames[int(t * 10)], duration=len(frames)/10)
    animation.write_videofile(nom, fps=10, verbose=False, logger=None)


def Cloud_Transient_1(p, tt, u_ap):
    if tt.min() == 1:
        tt -= 1
    t      = len(u_ap[0,:])
    step   = int(np.ceil(t/50))
    min    = u_ap.min()
    max    = u_ap.max()
    T      = np.linspace(0,3,t)

    for k in np.arange(0,t,step):
        fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)
        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')

        plt.pause(0.1)
        plt.close()

    fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    plt.pause(0.1)

def Cloud_Transient_sav_1(p, tt, u_ap, nom):
    if tt.min() == 1:
        tt -= 1
    t      = len(u_ap[0,:])
    step   = int(np.ceil(t/50))
    min    = u_ap.min()
    max    = u_ap.max()
    T      = np.linspace(0,3,t)
    frames = []

    for k in np.arange(t):
        fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')

        frames.append(mplfig_to_npimage(fig))
        plt.close()

    fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
    tin = float(T[t-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)

    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,t-1], triangles=tt, cmap=cm.coolwarm)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    frames.append(mplfig_to_npimage(fig))
    plt.close()

    animation = mpy.VideoClip(lambda t: frames[int(t*10)], duration=len(frames)/100)
    animation.write_videofile(nom, fps=10, verbose=False, logger=None)


def Error(er):
    t = len(er)
    T = np.linspace(0,1,t)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(T, er)
    ax1.set_title('Linear')
    ax1.set(xlabel='Time Step', ylabel='Error')

    ax2.semilogy(T, er)
    ax2.set_title('Logarithmic')
    ax2.set(xlabel='Time Step', ylabel='Error')

    plt.suptitle('Quadratic Mean Error')
    plt.show()


def Error_sav(er,nom):
    t = len(er)
    T = np.linspace(0,1,t)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    ax1.plot(T, er)
    ax1.set_title('Linear')
    ax1.set(xlabel='Time Step', ylabel='Error')

    ax2.semilogy(T, er)
    ax2.set_title('Logarithmic')
    ax2.set(xlabel='Time Step', ylabel='Error')

    plt.suptitle('Quadratic Mean Error')

    plt.savefig(nom)
    plt.close()