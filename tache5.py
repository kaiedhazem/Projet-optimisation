## les membres de l'équipes: Chouichi Ghada,El Abed Imene , Ben Ahmed Syrine , Belhadj Aya
## importations
import random as r
import numpy as np
import math as m
import scipy.linalg as spl # in order to solve Ax=b
import matplotlib.pyplot as plt 
from scipy.sparse import csr_matrix

# # Creation of a positive definite matrix (SDP matrix)
    # n : size of the matrix
    # nb_extra_diag: number of extra-diagonal not equal to zero 
def matrice_SDP(n, nb_extra_diag):
    A = np.zeros([n, n])
    coord = []
    for i in range(0, n, 1):
        for j in range(0, i, 1):
            coord.append([i, j])
    for i in range(0, nb_extra_diag, 1):
        c = r.randint(0, len(coord)-1)
        val = r.randint(0,50)
        A[coord[c][0]][coord[c][1]] = val
        A[coord[c][1]][coord[c][0]] = val
        del coord[c]
    for i in range(0, n, 1):
        s = 0
        for j in range(0, n, 1):
            s = s + A[i][j]
        A[i][i] = r.randint(s + 1, 2 * s +1)
    return A
def matriceA_SDP(n, nb_extra_diag):
    A = np.zeros([n, n])
    
    for i in range(0,n) :
        
        if i < n :
            A[i - 1, i] = -1
            A[(i-n) + 1, i] = -1
            A[0,n-1] =0
            A[n-1,0] =0
    print("\n Entrer les élements du diagonal :\n ")
    for i in range(0, nb_extra_diag, 1):
        A[i][i]= int(input(""))
  
    return A
    ## Creation of a n-sized random vector, with value between 0 and 50. 
def random_vector(n):
    B = np.zeros((n,1))
    for i in range(0,n,1):
        B[i][0] = r.randint(0,50)
    return B
## check if matrix is positive definite 
def is_symdefpos(M):
    # check if M is symmetric : if AT = A
    for i in range(np.shape(M)[0]):
        for j in range(np.shape(M)[1]):
            if (M[i][j] != M[j][i]):
                return False

    # check if M is defined positive :if all its eigenvalues are strictly positive.
    if not (  np.all(np.linalg.eigvals(M) > 0)):
      return False

    # check if M is invertible : if det !=0
    if spl.det(M) == 0:
        return False

    return True

def conjgrad(A,b,X,imax,p):
    if (is_symdefpos(A) == False):
        # check if A is sdp
        print("\n A n'est pas symétrique définie positive")
        return np.zeros((np.shape(A)[0],1))
    R = b - A.dot(X)
    P = R
    rs_old = np.transpose(R).dot(R)
    for i in range(1, imax + 1):
        Ap = A.dot(P)
        alpha = rs_old / np.transpose(P).dot(Ap)
        X = X + (alpha * P)
        R = R - (alpha * Ap)
        rs_new = np.transpose(R).dot(R)
        if (m.sqrt(rs_new) < p):
            break
        P = R + (rs_new/rs_old) * P
        rs_old = rs_new
    print("\n R = \n", R)
    print("\n X = \n", X)
    return X
    
def test_conjgrad():
        # initialized first test matrix
    A = np.array([[3.,-1.,0.,0.,0.],[-1.,12.,-1.,0.,0.],[0.,-1.,24.,-1.,0.],[0.,0.,-1.,48.,-1.],[0.,0.,0.,-1.,96.]])
    print("A= \n", A, "\n Dimension de A: ", np.shape(A))
    b = np.array([[1.],[2.],[3.],[4.],[5.]])
    print("B = \n", b, "\n Dimension de b: ", np.shape(b))
    Xzero = np.array([[0.],[0.],[0.],[0.],[0.]]) # initialized null 5-dimensioned vector
    imax = 10**3
    p = 10**(-5)
    print("\n Précision à ",p," près \n")
    X_sol = conjgrad(A, b, Xzero, imax, p)
    print("\n Avec la méthode du gradient conjugué on a \n X = \n", X_sol)
    
    #on va vérifier notre solution
    X_solve = spl.solve(A, b)
    print("\n Avec la fonction solve de la biliothèque scipy.linalg on a \n X = \n", X_solve) 
    print("\n Test avec une matrice générée par la fonction matrice_SDP : \n")

    print(" - Entrer 1 si vous voulez de saisir une fonction quadratique \n - Entrer 2 si vous voulez un matrice aléatoire avec taille et nombre d'elements extra-diagonaux saisies (Default)") 
    choix = int(input())
    matrix_size = int(input("Entrer la taille de la matrice A: "))
    nbr_extra_diag = int(input("Ainsi que le nombre d'elements extra-diagonaux de A: "))
    if (choix==1):
      A = matriceA_SDP(matrix_size, nbr_extra_diag)
    else:
      A = matrice_SDP(matrix_size, nbr_extra_diag)
        
    b = random_vector(matrix_size)
    Xzero = np.zeros((matrix_size,1))
    X_sol = conjgrad(A, b, Xzero, imax, p)

     #on va vérifier notre solution
    X_solve = spl.solve(A, b)
    print("\n Avec la fonction solve de la biliothèque scipy.linalg on a \n X = \n", X_solve) 

    print("\n A = \n", A)
    print("\n b = \n", b)
    print("\n Xzero = \n", Xzero)
    print("\n X_solve = \n", X_sol)
#test_conjgrad()