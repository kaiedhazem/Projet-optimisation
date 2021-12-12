from tkinter import *
import sys
import fonctions
window = Tk()
window.geometry('500x500+300+150')
window.title("test")
photo  = PhotoImage(file=('1.png'))
l=Label(text='label', fg='red',bg='blue').place(x=220,y=5)
#b = Button(text='hello',relief=SUNKEN,cursor="hand2",activebackground="green",width=10,bd=10).grid(row = 0 , column=0) # can use .place(x= , y= ) or .pack(pady=10)
#b = Button(text='hello',bitmap="error" , image=photo).grid(row = 0 , column=1) # can use .place(x= , y= ) or .pack(pady=10)

window.mainloop()