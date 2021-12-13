from sympy import *
import numpy as np

#bloc pour importation des fonctions pour chaque tache
import tache1
import tache2
import tache3Fct2
import tache3Fct3
import tache4Fct2
import tache4Fct3
import tache5
import tache6
import tache7
import tache8

#Menu principal
while (1):
    print("\nBienvenue dans la bibliothéque de 2 ING 2")
    print("Choisissez :\n"+"1) Soumettre votre propre fonction \n"+"2) Visualiser des fonctions prédefinies \n"
    +"3) Gradient conjugué standard\n"+"4) Quitter le programme \n")
    choix=input("Entrez votre choix: ")
    print(choix)
    if choix == '1':
          #Fonction entrée par l'utilisateur
          print("\n-------------------------------------------------------------------------------------------------------\n")
          sym = []
          nbVar = input('Nombre de variables: ')
          for i in range(int(nbVar)):
             var = input("Entrez la variable numéro " + str(i+1) + ": ")
             sym.append(Symbol(var))
          function= sympify(input("Entrez la fonction: "))
          if (int(nbVar)) == 2:
            while(1):  
              print ("\n1) Graphe et lignes de niveaux \n"
                    +"2) Vecteur gradient et matrice hessienne\n"
                    +"3) Méthode du gradient conjugué avec le critère de Wolfe\n"
                    +"4) Quitter")
              choice=input("Tapez votre choix SVP: ")  
              match choice:
                  case '1':
                      a=np.linspace(-10,10,20)
                      b=np.linspace(-10,10,20)
                      x , y = np.meshgrid(a,b)
                      x1=Symbol('x')
                      x2=Symbol('y')
                      func = lambdify([x1,x2], function,'numpy')
                      z= func(x,y) 
                      print("\n resultat:\n")
                      tache1.affichage(x,y,z)
                  case '2':
                      print("\n resultat:\n")
                      tache2.Grad(function,nbVar,sym)
                      tache2.Hess(function , sym) 
                  case '3':
                      print("\n resultat:\n")
                      tache7.perso(function)     
                  case '4':
                      print("\nRetour au menu précedent")
                      break 
                  case _: 
                      print("!! verifiez votre choix SVP !!")
                                         
          elif (int(nbVar)) > 2 : 
            while(1):   
              print ("\n1) Vecteur gradient et matrice hessienne\n"
                    +"2) Méthode du gradient conjugué avec le critère de Wolfe\n"
                    +"3) Quitter")
              choice2=input("Tapez votre choix SVP: ")
              match choice2:
                  case '1':
                      print("\n resultat:\n")
                      tache2.Grad(function,nbVar,sym)
                      tache2.Hess(function , sym) 
                  case '2':
                      print("\n resultat:\n")
                      tache7.perso(function)
                      
                  case '3':
                      print("\nRetour au menu précedent")
                      break  
                  case _: 
                      print("!! verifiez votre choix SVP !!")
        

    elif choix == '2':
        #Fonctions prédéfinies
      while(1):  
        print("\n-------------------------------------------------------------------------------------------------------")  
        print("\nLes fonctions prédefinies: \n1) Fct 1 = (x1 - 1)² + (x2 - 4)² \n2) Fct 2 =(x1)² + (x2)^4 \n3) Fct 3 = (1 - x1)² + 100(x2 - x1²)²\n"+
        "4) Fct4 = <Ax,x> - <b, x>   ---  avec:\n\n"
                                           +"    | 3   -1   0    0   0  |        | 1 |\n"+
                                            "    | -1  12   -1   0   0  |        | 2 |\n"+
                                            "A = | 0   -1   24   -1  0  |  et b =| 3 |\n"+
                                            "    | 0   0    -1   48  -1 |        | 4 |\n"+  
                                            "    | 0   0    0    -1  96 |        | 5 |\n"+
        "5) Quitter")
        function=input("\nChoisissez une fonction :")
        match function:
            case '1' : 
              while(1):  
                print ("\n1) Méthode du gradient conjugué avec le critère d’Armijo \n"
                    +"2) Méthode du gradient conjugué avec le critère de Wolfe\n"
                    +"3) Graphe et Lignes de niveaux\n"
                    +"4) Quitter")
                choix1=input("Entrez votre choix SVP : ")
                if choix1 == '1':
                    print("\n resultat:\n")
                    tache6.affichageFct1()
                elif choix1 == '2':
                    print("\n resultat:\n")
                    tache7.fonction1()
                elif choix1 == '3':
                    print("\n resultat:\n")
                    tache1.afficheFct1()
                elif choix1 == '4':
                    print("\nRetour au menu précedent")
                    break
            case '2' : 
                print ("\n1) Méthode de gradient à pas fixe décroissant \n"
                    +"2) Méthode du gradient à pas optimal\n"
                    +"3) Graphe et Lignes de niveaux\n "
                    +"4) Quitter")
                choix2=input("Entrez votre choix SVP : ")
                if choix2 == '1':
                    print("\n resultat:\n")
                    tache3Fct2.affichageFct2()
                elif choix2 == '2':
                    print("\n resultat:\n")
                    print(tache4Fct2.Gradient_PasOpt([1,0], 0.00001))    
                elif choix2 == '3':
                    print("\n resultat:\n")
                    tache1.afficheFct2()
                elif choix2 == '4':
                    print("\nRetour au menu précedent")
                    break
            case '3' :
                print ("\n1) Méthode de gradient à pas fixe décroissant\n"
                    +"2) Méthode du gradient à pas optimal\n"
                    +"3) Méthode du gradient conjugué pour les fonctions non linéaires\n"
                    +"4) Méthode du gradient conjugué avec le critère d’Armijo \n"
                    +"5) Graphe et Lignes de niveaux \n"
                    +"6) Quitter") 
                choix3=input("Entrez votre choix SVP : ")
                if choix3 == '1':
                    print("\n resultat:\n")
                    tache3Fct3.affichageFct3()
                elif choix3 == '2':
                    print("\n resultat:\n")
                    print(tache4Fct3.Gradient_PasOpt([1,2], 0.00001)) 
                elif choix3 == '3':
                    print("\n resultat:\n")
                    tache8.affichageFct3()      
                elif choix3 == '4':
                    print("\n resultat:\n")
                    tache6.affichageFct3()
                elif choix3 == '5':
                    print("\n resultat:\n")
                    tache1.afficheFct3()
                elif choix3 == '6':
                    print("\nRetour au menu précedent")
                    break 
            case '4' :
                print ("\n1) Méthode du gradient conjugué pour les fonctions non linéaires\n"
                    +"2) Quitter\n")
                choix4=input("Entrez votre choix SVP : ")
                if choix4 == '1':
                    print("\n resultat:\n")
                    tache8.affichageFct4()  
                elif choix4 == '2':
                    print("\nRetour au menu précedent")
                    break
            case '5' : 
                print("\nRetour au menu prinicipale")
                break        
            case _ : print ("\n!! Vérifiez votre choix !!")      

    elif choix == '3': 
        #Gradient conjugué standard
        print("\n resultat:\n") 
        tache5.test_conjgrad()  
    elif choix == '4': 
        #Quitter
        print("Merci pour votre visite")
        exit()                                                                                                                                                           
    