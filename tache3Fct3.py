from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import math

#----------------------------------------------------------------------------------------#
# Function

def fonction(x1,x2):
    return x1**2+x2**4;

def partial_derivative(func, var=0, point=[]):   #calculer les dérivées partielles d'une fonction en un point par rapport au premier argument en utilisant la fonction SciPy scipy.misc.derivative
    args = point[:]
    def wraps(x):  #fct d'entré
        args[var] = x
        return func(*args)
    return misc.derivative(wraps, point[var], dx = 1e-6) #retourne dérivé n éme mete3 fct / dx : espacement

#----------------------------------------------------------------------------------------#
# Plot Function
def affichageFct3():
    x1 = np.arange(-2.0, 2.0, 0.1)  #Renvoie des valeurs régulièrement espacées dans un intervalle donné cad ta3emili l'échelle mete3 l graphe
    x2 = np.arange(-2.0, 2.0, 0.1)

    xx1,xx2 = np.meshgrid(x1,x2);  #Renvoie des matrices de coordonnées à partir de vecteurs de coordonnées.

    z = xx1**2+xx2**4;  

    h = plt.contourf(x1,x2,z)  #pour tracer des contours colorés 
    #plt.show()

    #----------------------------------------------------------------------------------------#
    # Gradient Descent

    alpha = 0.00001 # pas pour se déplacer entre le nuage des points 
    nb_max_iter = 100 # Nb max d'iteration
    eps = 0.0001 # critère d'arret 

    x1_0 = 1.0 # point de départ pour x1
    x2_0 = 1.5 # point de départ pour x2
    z0 = fonction(x1_0,x2_0) 
    plt.scatter(x1_0,x2_0)  # permet de tracer des ensembles de données à deux variables au format point

    cond = eps + 10.0 # commencer par cond supérieur à eps (car epsilone est un critere d'arret)
    nb_iter = 0  #initialisation du nbre d'itération
    tmp_z0 = z0  #retour initiale de notre fonction
    while cond > eps and nb_iter < nb_max_iter:
        tmp_x1_0 = x1_0 - alpha * partial_derivative(fonction, 0, [x1_0,x2_0])  #etape2 xk+1=xk+alpha*dk
        tmp_x2_0 = x2_0 - alpha * partial_derivative(fonction, 1, [x1_0,x2_0])
        x1_0 = tmp_x1_0
        x2_0 = tmp_x2_0
        z0 = fonction(x1_0,x2_0)
        nb_iter = nb_iter + 1
        cond = abs( tmp_z0 - z0 )   #pour voir est ce que le cond < epsilon ou nn (test d'arret)/update cond
        tmp_z0 = z0
        print ("nb_iter=",nb_iter,x1_0,x2_0,cond)
        plt.scatter(x1_0, x2_0)

    plt.title("Gradient Descent ")
    plt.savefig("gradiend_descent.png", bbox_inches='tight')
    plt.show()
#affichageFct3()