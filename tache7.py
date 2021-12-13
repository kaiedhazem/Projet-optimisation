import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d.axes3d import Axes3D
from sympy import *
import sympy as sp
from past.builtins import xrange

def wolfe_rule(alpha_0,x,f,grad,f_x,grad_x,d_x,c_1,c_2): #d_x est la direction de descente  d_x . grad_x <= 0
    # test f(x_new) \leq f(x_0) + c_1 alpha ps{d_x}{grad_x} et \ps{x_new}{d_x} \geq c_2 \ps{x_0}{d_x}
    # sinon alpha <- alpha * beta
    # On cherche au fur et mesure un opt dans [minorant, majorant]
    test = 1
    iteration = 0
    alpha = alpha_0
    minorant = 0
    majorant = 1000
    while (test)&(iteration<=1000): 
        x_new = x+alpha*d_x;
        if (f(x_new)<=f_x+c_1*alpha*np.dot(grad_x,d_x))&(np.dot(grad(x_new),d_x) >= c_2*np.dot(grad_x,d_x) ):
            test = 0
        elif (f(x_new)>f_x+c_1*alpha*np.dot(grad_x,d_x)):
            majorant = alpha
            alpha = (majorant + minorant)/2
            iteration = iteration +1
        else:
            minorant = alpha
            alpha = (majorant + minorant)/2
            iteration = iteration +1
    return alpha

def conjugate_gradient_wolfe(f, grad, x0, iterations, error_point, error_grad, c_1=0.1,c_2=0.9,L=100):
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
    h = wolfe_rule(alpha_0,x,f,grad,f_x,grad_x,d_x,c_1,c_2)
    for i in xrange(iterations):
        x = x + h*d_x
        grad_x_old = grad_x
        grad_x = grad(x)
        f_x = f(x)
        kappa = np.dot(grad_x - grad_x_old, grad_x)/np.power(np.linalg.norm(grad_x),2)
        d_x = kappa*d_x -grad_x
        alpha_0 = -(1./L)*np.dot(d_x,grad_x)/np.power(np.linalg.norm(d_x),2)
        h = wolfe_rule(alpha_0,x,f,grad,f_x,grad_x,d_x,c_1,c_2)
        x_list[:,i] = x
        f_list[i] = f_x
        error_point_list[i] = np.linalg.norm(x - x_old)
        error_grad_list[i] = np.linalg.norm(grad_x)
        
        if i % 1000 == 0:
            print("iter={}, x={}, f(x)={}".format(i+1, x, f(x)))

        if (error_point_list[i] < error_point)|(error_grad_list[i] < error_grad):
            break
        x_old = x
        
    print("point error={}, grad error={}, iteration={}, f(x)={}".format(error_point_list[i], error_grad_list[i],i+1,f(x)))    
    return { 'x_list' : x_list[:,0:i], 'f_list' : f_list[0:i], 'error_point_list' : error_point_list[0:i], 'error_point_list' : error_point_list[0:i]}                

def fonction1():
  def fn1(x):
      y = np.asarray(x)
      return np.sum((y[0] - 1)**2 + (y[1] -4)**2)

  def fn1_grad(x):
      y = np.asarray(x)  #déclaration d'un tableau
      grade = np.zeros_like(y) #initialisation de tableau
      #calucle de gradient
      grade[0] = 2*y[0]-2
      grade[1] = 2*y[1]-8
      return grade

  def fn1_grad(x):
      y = np.asarray(x)  #déclaration d'un tableau
      grade = np.zeros_like(y) #initialisation de tableau
      #calucle de gradient
      grade[0] = 2*y[0]-2
      grade[1] = 2*y[1]-8
      return grade

  f = fn1
  grad = fn1_grad
  x0 = np.array([-1,2,-1])
  error_point = 0.00001
  error_grad = 10**-10
  iterations = 10000
  result = conjugate_gradient_wolfe(f, grad, x0, iterations, error_point, error_grad)

  
  a=np.linspace(-10,10,20)
  b=np.linspace(-10,10,20)

  x , y = np.meshgrid(a,b)

  z = (x - 1)**2 + (y-4)**2


  fig1,ax1 = plt.subplots()
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
def perso(function):
  

  def fctplus(x,y):
    x1=Symbol('x')
    x2=Symbol('y')
    func = lambdify([x1,x2], function,'numpy')
    return func(x,y)
  sym = set()
  s = ""

  for c in str(function):
    if (c == 'x'):
      s+="y[0]"
      sym.add(Symbol(c))
    elif (c =='y'):
      s+= "y[1]"
      sym.add(Symbol(c))
    elif (c == 'z') :
      s+= "y[2]"
      sym.add(Symbol(c))
    else:
      s+= c 

  sx = ""
  sy = ""
  sz = ""
  xinit = []
  gradient = []
  for val in sym:
      gradient.append(function.diff(val))
      xinit.append(input("saisir val init "))
  try :
    for c in str(gradient[0]):
      if c =='x':
        sx += "y[0]"
      elif c =='y':
        sx += "y[1]"
      elif c =='z':
        sx += "y[2]"
      else:
        sx += c
  except :
    pass

  try : 
    for c in str(gradient[1]):
      if c =='x':
        sy += "y[0]"
      elif c =='y':
        sy += "y[1]"
      elif c =='z':
        sy += "y[2]"
      else:
        sy += c
  except :
    pass


  try :
    for c in str(gradient[2]):
      if c =='x':
        sz += "y[0]"
      elif c =='y':
        sz += "y[1]"
      elif c =='z':
        sz += "y[2]"
      else:
        sz += c
    print()  
  except :
    pass


  def input_fn(x):
    y = np.asarray(x)
    return np.sum(eval(s))

  def input_grad(x):
      y = np.asarray(x)  #déclaration d'un tableau
      grade = np.zeros_like(y) #initialisation de tableau
      #calucle de gradient
      try :
        grade[0] = eval(sx)
      except:
        pass
      try : 
        grade[1] = eval(sy)
      except :
        pass
      try :
        grade[2] = eval(sz)
      except :
        pass
      return grade

  ## test fonction personnalisé
  f = input_fn
  grad = input_grad
  x0 = np.array(xinit,dtype='float64')
  error_point = 0.00001
  error_grad = 10**-10
  iterations = 10000
  result = conjugate_gradient_wolfe(f, grad, x0, iterations, error_point, error_grad)

  a=np.linspace(-10,10,20)
  b=np.linspace(-10,10,20)

  x , y = np.meshgrid(a,b)

  z = fctplus(x,y)


  fig1,ax1 = plt.subplots()
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
#fonction1()