import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d.axes3d import Axes3D
from sympy import *
import sympy as sp


def fct1(x,y):
    print(x)
    print(y)
    return (x-1)**2+(y-4)**2
def fct2(x,y):
    return x**2+y**2
def fct3(x,y):
    return (1-x)**2+100*(y-x**2)**2
def fct4(x,y):
    return (x-y)**2
def fct5(x,y):
    return np.cos(x)
def fct6(x,y):
    return np.exp(x)*np.cos(y)
def fctplus(x,y):
    s=input("entrer une fonction")
    f=sp.sympify(s)
    x1=Symbol('x')
    x2=Symbol('y')
    func = lambdify([x1,x2], f,'numpy')
    return func(x,y)


'''print('Choisir la focntion dont vous souhaite afficher le graphe et les lignes de niveaux \n 1: Fonction 1 = (𝑥1 − 1)² + (𝑥2 − 4)² \n 2: Fonction 2 =(x1)² + (𝑥2)^4 \n 3: Fonction 3 =  (1 − 𝑥1)² + 100(𝑥2 − 𝑥1²)²\n 4: Fonction supplémentaire (de votre choix)  \n')
nb=input('Choisir une option  \n')
choix=int(nb)'''

a=np.linspace(-10,10,20)
b=np.linspace(-10,10,20)

x , y = np.meshgrid(a,b)

def afficheFct1():
    z = fct1(x,y)
    affichage(x,y,z)
def afficheFct2():
    z = fct2(x,y)
    affichage(x,y,z)
def afficheFct3():
    z = fct3(x,y)
    affichage(x,y,z)
def afficheFctplus():
    z = fctplus(x,y)
    affichage(x,y,z)

def affichage(x,y,z):
    fig1,ax1 = plt.subplots()
    print(type(x))
    print(type(y))
    print(type(z))
    ax1.contourf(x,y,z)
    ax1.set_title('Figure ligne de niveaux  coloré')
    plt.show()


    fig2, ax2 = plt.subplots()
    cnt = ax2.contour(z, cmap=matplotlib.cm.RdBu, vmin=abs(z).min(), vmax=abs(z).max(), extent=[-10, 10, -10, 10])
    ax2.set_title('Figure ligne de niveaux')

    fig3 = plt.figure(figsize=(14,14))
    fig4 = plt.figure(figsize=(14,14))
    ax3 = fig3.add_subplot(1, 2, 1, projection='3d')
    ax3.set_title('Figure graphe 3D de la fonction ')
    p = ax3.plot_surface(x, y, z, rstride=1, cstride=1)


    ax4 = fig4.add_subplot(1, 2, 1, projection='3d')
    ax4.set_title('Figure graphe 3D de la fonction avc couleur degradé')
    p = ax4.plot_surface(x, y, z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, antialiased=False)
    cb = fig4.colorbar(p, shrink=0.5)  

    fig5 = plt.figure(figsize=(14,14))
    ax5 = fig5.add_subplot(1, 2, 1, projection='3d')
    ax5.set_title('Figure graphe 3D de la fonction avec un autre angle de vue ')
    p = ax5.plot_wireframe(x, y, z, rstride=1, cstride=1, alpha=0.5)
    ax5.view_init(25, 50)

#afficheFctplus()