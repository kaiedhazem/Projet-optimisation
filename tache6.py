#importation 
import numpy as np
import numpy.random as rnd
import scipy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Définiton de la fonction 1 ( pour le test) 

def fonction_1(x):
    y = np.asarray(x)
    return np.sum((y[0] - 1)**2 + (y[1] -4)**2)


#Calcule de gradient de la fonction 1

def grad_fonction_1(x):
    y = np.asarray(x)  #déclaration d'un tableau
    grade = np.zeros_like(y) #initialisation de tableau
    #calucle de gradient
    grade[0] = 2*y[0]-2
    grade[1] = 2*y[1]-8
    return grade


#Définiton de la fonction 3 (pour le test)

def fonction_3_rosenbrock(x): 
    y = np.asarray(x)
    return np.sum((y[0] - 1)**2 + 100*(y[1] - y[0]**2)**2)

#Calcule de gradient de la fonction 3

def grad_fonction_3(x):
    y = np.asarray(x) #déclaration d'un tableau 
    grad = np.zeros_like(y) #intialisation du tableau
    #calucle de gradient
    grad[0] = 400*y[0]*(y[0]**2-y[1]) + 2*(y[0]-1)
    grad[1] = 200*(y[1]-y[0]**2)
    return grad


#Déclaration de la régle d'armijo

def armijo_rule(alpha_0,x,f,f_x,grad_x,d_x,c,beta):
    test = 1
    alpha = alpha_0
    while test: 
        x_new = x+alpha*d_x;
        if (f(x_new)<=f_x+c*alpha*np.dot(grad_x,d_x)):
            test = 0
        else:
            alpha = alpha*beta
    return alpha

#implémentation de la méthode de calcule de gradient conjugé avec le pas d'armijo

def conjugate_gradient_armijo(f, grad, x0, iterations, error_point, error_grad, c=0.1,L=100,beta=0.5):
    dim = np.max(np.shape(x0))
    x_list = np.zeros([dim,iterations])  
    f_list = np.zeros(iterations)  
    error_point_list = np.zeros(iterations)
    error_grad_list = np.zeros(iterations)    
    x = x0
    x_old = x
    grad_x = grad(x)
    d_x = -grad_x
    f_x = f(x)
    alpha_0 = -(1./L)*np.dot(d_x,grad_x)/np.power(np.linalg.norm(d_x),2)
    h = armijo_rule(alpha_0,x,f,f_x,grad_x,d_x,c,beta)
    for i in range(iterations):
        x = x + h*d_x
        grad_x_old = grad_x
        grad_x = grad(x)
        f_x = f(x)
        kappa = np.dot(grad_x - grad_x_old, grad_x)/np.power(np.linalg.norm(grad_x),2)
        d_x = kappa*d_x -grad_x
        alpha_0 = -(1./L)*np.dot(d_x,grad_x)/np.power(np.linalg.norm(d_x),2)
        h = armijo_rule(alpha_0,x,f,f_x,grad_x,d_x,c,beta)
        x_list[:,i] = x
        f_list[i] = f_x
        error_point_list[i] = np.linalg.norm(x - x_old)
        error_grad_list[i] = np.linalg.norm(grad_x)
        
        if i % 1000 == 0:
            print ("iter={}, x={}, f(x)={}".format(i+1, x, f(x)))

        if (error_point_list[i] < error_point)|(error_grad_list[i] < error_grad):
            break
        x_old = x
        
    print ("point error={}, grad error={}, iteration={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,f(x)))
    return { 'x_list' : x_list[:,0:i], 'f_list' : f_list[0:i], 'error_point_list' : error_point_list[0:i], 'error_point_list' : error_point_list[0:i]}




def affichageFct3():
    #test pour la fonction 3

    print ("test pour la fonction 3" ) 
    f3 =fonction_3_rosenbrock
    grade =grad_fonction_3
    x1 = np.array([1.1,2.1])
    error_point = 10**-10
    error_grad = 10**-10
    iterations = 10000
    result2 = conjugate_gradient_armijo(f3, grade, x1, iterations, error_point, error_grad)


def affichageFct1():
    #test pour la fonction 1
    print ("test pour la fonction 1" ) 
    f =fonction_1
    grad = grad_fonction_1
    x0 = np.array([1.1,2.1])
    error_point = 10**-10
    error_grad = 10**-10
    iterations = 10000
    result = conjugate_gradient_armijo(f, grad, x0, iterations, error_point, error_grad)
    x_list = result['x_list']
    #affichage du graphe pour la fonction 1
    all_x_i = np.append(x0[0], x_list[0,:])
    all_y_i = np.append(x0[1], x_list[1,:])
    plt.plot(all_x_i, all_y_i, 'k+-')
    plt.plot(x0[0],x0[1],'r+')
    plt.plot([1],[1],'g+')
    plt.title(r'$\mathrm{Graphe \ : conjugate \ gradient \ + \ Armijo \ fonction 1}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.show()
    
#affichageFct1()    