from sympy import *
import sympy as sp
import numpy as np
## Fonction Calcul de gradient 
def Grad(function,nbVar,sym):
  try:  
    print("Le vecteur gradient ")
    gradient = []
    for i in range(int(nbVar)):
      gradient.append(function.diff(sym[i]))
      print(gradient[i])
  except Exception as e:
      print(e)
## Fonction Calcul de la matrice Hessienne 
def Hess(function , sym):
  try:
   print("La matrice Hessienne est = ")
   H=hessian(function, sym)
   pprint(H)
  except Exception as e:
      print(e)
''' print("Les variables sont : ")
            print(sym)
            print("La fonction f = ")
            print(function)

Grad(function,nbVar,sym)
Hess(function , sym)'''