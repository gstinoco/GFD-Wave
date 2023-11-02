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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import moviepy.editor as mpy
from moviepy.video.io.bindings import mplfig_to_npimage

def Cloud_Static_sav(p, tt, u_ap, u_ex, nom):
    """
    Cloud_Static_Sav

    This function graphs and saves the approximated and theoretical solutions of the problem being solved at three different time levels.
    Both solutions are presented side by side to help perform graphical comparisons between both solutions.
    The graphics are stored, as figures, on drive on the current path, or whatever path were provided on "nom".

    Input:
        p           m x 2           Array           Array with the coordinates of the nodes.
        tt          n x 3           Array           Array with the correspondence of the n triangles.
        u_ap        m x t           Array           Array with the computed solution.
        u_ex        m x t           Array           Array with the theoretical solution.
        nom                         String          Name of the files to be saved to drive.
    
    Output:
        None
    """
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
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,0], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,0], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '_00.png'
    plt.savefig(nok)
    plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[step])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,step], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,step], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '_05.png'
    plt.savefig(nok)
    plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')
    nok = nom + '_10.png'
    plt.savefig(nok)
    plt.close()


def Cloud_Transient(p, tt, u_ap, u_ex):
    """
    Cloud_Transient

    This function graphs and saves the approximated and theoretical solutions of the problem being solved at several time levels.
    Both solutions are presented side by side to help perform graphical comparisons between both solutions.

    Input:
        p           m x 2           Array           Array with the coordinates of the nodes.
        tt          n x 3           Array           Array with the correspondence of the n triangles.
        u_ap        m x t           Array           Array with the computed solution.
        u_ex        m x t           Array           Array with the theoretical solution.
        
    Output:
        None
    """
    if tt.min() == 1:
        tt -= 1
    t    = len(u_ex[0,:])
    step = int(np.ceil(t/50))
    min  = u_ex.min()
    max  = u_ex.max()
    T    = np.linspace(0,1,t)

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))

    for k in np.arange(0,t,step):
        
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')
        
        ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,k], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax2.set_zlim([min, max])
        ax2.set_title('Theoretical Solution')

        plt.pause(0.01)
        ax1.clear()
        ax2.clear()

    tin = float(T[-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)

    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax2.set_zlim([min, max])
    ax2.set_title('Theoretical Solution')

    plt.pause(0.1)


def Cloud_Transient_sav(p, tt, u_ap, u_ex, nom):
    """
    Cloud_Transient_sav

    This function graphs and saves the approximated and theoretical solutions of the problem being solved at several time levels.
    Both solutions are presented side by side to help perform graphical comparisons between both solutions.
    The graphics are stored, as video, on drive on the current path, or whatever path were provided on "nom".

    Input:
        p           m x 2           Array           Array with the coordinates of the nodes.
        tt          n x 3           Array           Array with the correspondence of the n triangles.
        u_ap        m x t           Array           Array with the computed solution.
        u_ex        m x t           Array           Array with the theoretical solution.
        nom                         String          Name of the files to be saved to drive.
    
    Output:
        None
    """
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

        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')
        
        ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,k], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax2.set_zlim([min, max])
        ax2.set_title('Theoretical Solution')

        frames.append(mplfig_to_npimage(fig))
        plt.close()

    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw = {"projection": "3d"}, figsize=(8, 4))
    tin = float(T[-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)

    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    ax2.plot_trisurf(p[:,0], p[:,1], u_ex[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
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
    T      = np.linspace(0,1,t)

    for k in np.arange(0,t,step):
        fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)
        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')

        plt.pause(0.1)
        plt.close()

    fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
    tin = float(T[-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)
    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
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
    T      = np.linspace(0,1,t)
    frames = []

    for k in np.arange(0,t,step):
        fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
        tin = float(T[k])
        plt.suptitle('Solution at t = %1.3f s.' %tin)

        ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,k], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax1.set_zlim([min, max])
        ax1.set_title('Approximation')

        frames.append(mplfig_to_npimage(fig))
        plt.close()

    fig, (ax1) = plt.subplots(1, 1, subplot_kw = {"projection": "3d"}, figsize = (10, 5))
    tin = float(T[-1])
    plt.suptitle('Solution at t = %1.3f s.' %tin)

    ax1.plot_trisurf(p[:,0], p[:,1], u_ap[:,-1], triangles=tt, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_zlim([min, max])
    ax1.set_title('Approximation')
    
    frames.append(mplfig_to_npimage(fig))
    plt.close()

    animation = mpy.VideoClip(lambda t: frames[int(t * 10)], duration=len(frames)/10)
    animation.write_videofile(nom, fps=10, verbose=False, logger=None)

def Error(er):
    """
    Error

    This function graphs all the Quadratic Mean Errors computed between the approximated and theoretical solutions of the problem being solved.
    
    Input:
        er          t x 1           Array           Array with the Quadratic Mean Error on each time step.
    
    Output:
        None
    """
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
    """
    Error_sav

    This function graphs and saves all the Quadratic Mean Errors computed between the approximated and theoretical solutions of the problem being solved.
    The graphic is stored, as an image, on drive on the current path, or whatever path were provided on "nom".

    Input:
        er          t x 1           Array           Array with the Quadratic Mean Error on each time step.
        nom                         String          Name of the file to be saved to drive.
    
    Output:
        None
    """
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


def Multi_Error(er1, er2, regi, cloud):
    """
    Error

    This function graphs all the Quadratic Mean Errors computed between the approximated and theoretical solutions of the problem being solved.
    
    Input:
        er          t x 1           Array           Array with the Quadratic Mean Error on each time step.
    
    Output:
        None
    """
    t = len(er1)
    T = np.linspace(0,3,t)
    fig, (ax1) = plt.subplots(1, 1, figsize=(10, 4))

    ax1.semilogy(T, er1, label=r'$\lambda = 1.00$')
    ax1.semilogy(T, er2, label=r'$\lambda = 0.50$')

    ax1.set(xlabel='Time Step', ylabel='Quadratic Mean Error')
    ax1.legend(loc='lower right')

    plt.suptitle('Region: ' + regi + '_' + cloud)
    plt.show()

def Multi_Error_sav(er1, er2, regi, cloud):
    """
    Error

    This function graphs all the Quadratic Mean Errors computed between the approximated and theoretical solutions of the problem being solved.
    
    Input:
        er          t x 1           Array           Array with the Quadratic Mean Error on each time step.
    
    Output:
        None
    """
    t = len(er1)
    T = np.linspace(0,3,t)
    fig, (ax1) = plt.subplots(1, 1, figsize=(10, 4))

    ax1.semilogy(T, er1, label=r'$\lambda = 1.00$')
    ax1.semilogy(T, er2, label=r'$\lambda = 0.50$')

    ax1.set(xlabel='Time Step', ylabel='Quadratic Mean Error')
    ax1.legend(loc='lower right')

    plt.suptitle('Region: ' + regi + '_' + cloud)

    nom = 'Results/' + regi + '_' + cloud + '.png'
    plt.savefig(nom)
    plt.close()