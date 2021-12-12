from tkinter import *
from tkinter import ttk
from sympy import *
window = Tk()
window.geometry('900x600')
window.title("Mini projet")
window.configure(bg='#EAE1DF')

def tache_2():
    b =IntVar()
    c=StringVar()
    d=StringVar()
    sym = []
    frame = ttk.Frame(window)
    frame.place(x=250,y=400)
    frame.config(height =150,width=400)
    frame.config(relief= RIDGE)  
    ttk.Label(frame ,text='nombres de variables:',  font=("Cooper Black", 10)).place(x=150,y=10)
    ttk.Entry(frame,textvariable=b).place(x=150,y=30) 
    ttk.Button(frame, text='ok').place(x=290, y=30)
    print(b.get())    
'''def fctl3():
    for i in range(int(b.get())):
           ttk.Label(frame ,text='Entrez la variable numéro ' + str(i+1) + ':',  font=("Cooper Black", 10)).place(x=150,y=60)
           ttk.Entry(frame,textvariable=c).place(x=150,y=80)
           sym.append(Symbol(c))
    ttk.Label(frame ,text='Entrez la fonction: ',  font=("Cooper Black", 10)).place(x=150,y=10)
    ttk.Entry(frame,textvariable=d).place(x=150,y=30)
    funct= sympify(d)
    tache2.Grad(funct,b,sym)
    tache2.Hess(funct,sym)
    ttk.Button(frame, text='Generer',command=fctl3).place(x=175, y=110)'''

l=Label(text='Bienvenue ^_^', fg='black',bg='#EAE1DF', width=20, font=("Cooper Black", 25)).place(x=230,y=5)
l1=Button(text='Vecteur gradient et Matrice Hessienne',activebackground="#B6FBE0", fg='black',bg='#DCD2D0', width=30, height=2, relief="raised" ,font=("Cooper Black", 12),command=tache_2).place(x=20,y=100)
l2=Button(text='Gradient à pas fixe', fg='black',bg='#DCD2D0', width=30,height=2,relief="raised" ,font=("Cooper Black", 12)).place(x=20,y=170)
l22=Button(text='Gradient à pas variable décroissant', fg='black',bg='#DCD2D0',width=30,height=2,relief="raised" , font=("Cooper Black", 12)).place(x=20,y=240)
l3=Button(text='Gradient à pas optimal', fg='black',bg='#DCD2D0', width=30,height=2,relief="raised" ,font=("Cooper Black", 12)).place(x=550,y=100)
l11=Button(text='Gradient conjugué standard', fg='black',bg='#DCD2D0',width=30, height=2,relief="raised" ,font=("Cooper Black", 12)).place(x=550,y=170)
l2=Button(text='Gradient pas d’Armijo', fg='black',bg='#DCD2D0',width=30, height=2,relief="raised" ,font=("Cooper Black", 12)).place(x=550,y=240)
l3=Button(text='Gradient pas de Wolfe', fg='black',bg='#DCD2D0',width=30, height=2,relief="raised" ,font=("Cooper Black", 12)).place(x=550,y=310)
l4=Button(text='Gradient conjugué pour les fonctions\n non linéaires', fg='black',bg='#DCD2D0',width=30,height=2, relief="raised" ,font=("Cooper Black", 12)).place(x=20,y=310)

window.mainloop()
