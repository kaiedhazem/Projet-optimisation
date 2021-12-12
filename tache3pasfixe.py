## ## Fonction pour la méthode de gradient à pas fixe pour 𝑓𝑐𝑡3 :

import numpy as np  #importer  numpy en tant que np(alias)  
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d.axes3d import Axes3D
from sympy import *
import sympy as sp

def fct2(x1, x2):
    return x1**2+x2**4

def gradfct2(x10, x20, err):
    x=np.array([x10,x20]) #tableau d'éléments qui sont tous du même type et indexés par un tuple d'entiers positifs
                           #ici x est un tableau  : array[x10,x20]
    for e in range(0,err):
        k=np.array([2*x[0]+4*x[1]**3])
        w=-k
        direction=0.00001*w
        print ("direction: "+str(direction))
        print ("norm: "+str(np.linalg.norm(direction))) #pour obtenir l'une des huit normes matricielles ou normes vectorielles différentes. Cela dépend de la valeur du paramètre donné.
        x = x+direction
        print("newx: "+str(x))
        g=fct2(x[0],x[1])
        print ("f(newx): " +str(g))
    return x
def fct3(x1, x2): 
    return (1-x1)**2+100*(x2-x1**2)**2

def gradfct3(x10, x20, err):
    x=np.array([x10,x20]) #tableau d'éléments qui sont tous du même type et indexés par un tuple d'entiers positifs
                           #ici x est un tableau : array[x10,x20]
    for e in range(0,err):
        k=np.array([2*x[0]+4*x[1]**3])
        w=-k
        direction=0.00001*w
        print ("direction: "+str(direction))
        print ("norm: "+str(np.linalg.norm(direction))) #pour obtenir l'une des huit normes matricielles ou normes vectorielles différentes. Cela dépend de la valeur du paramètre donné.
        x = x+direction
        print("newx: "+str(x))
        g=fct3(x[0],x[1])
        print ("f(newx): " +str(g))
    return x

#print (gradfct3(1,0,10))
