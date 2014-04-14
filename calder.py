#!/usr/bin/python3.2

from math import *
from tkinter import *
from couleur import *
from random import *
def dessineLigne(x1,x2,x3,x4,y,p1,p2,dessin):
	
	X1 = x1 + (x2-x1)/2
	X2 = x3 + (x4-x3)/2
	l1 = (p2*(X2-X1))/(p1+p2)
	X = X1 + l1
	#print("X1 = ",X1,"X2 = ",X2,"l1 = ",l1,"X = ",X)
	dessin.create_line(X1,y,X1,y-50)
	dessin.create_line(X2,y,X2,y-50)
	dessin.create_line(X1,y-50,X2,y-50)
	dessin.create_line(X,y-50,X,y-100)

def dessineCercle(x1,x2,y,p1,p2,dessin):

	x3 = x1 + 2*sqrt(p1)
	x4 = x2 + 2*sqrt(p2)
	y3 = y + 2*sqrt(p1)
	y4 = y + 2*sqrt(p2)
	i = randrange(len(colors))
	j = randrange(len(colors))
	print("colors[",i,"] = ",colors[i],"colors[",j,"] = ",colors[j])
	dessin.create_oval(x1,y,x3,y3,fill=colors[i])
	dessin.create_oval(x2,y,x4,y4,fill=colors[j])
	dessineLigne(x1,x3,x2,x4,y,p1,p2,dessin)

fenetre = Tk()

dessin = Canvas(fenetre, width =500, height=500)

dessin.pack()
#dessin.create_oval(50,100,150,200,fill='blue')
#dessin.create_oval(250,100,350,200,fill='red')
dessineCercle(50,250,100,500,2000,dessin)
#dessineLigne(50,150,250,350,100,200,200,dessin)

fenetre.mainloop()
	
	
