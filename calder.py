#!/usr/bin/python3.2

from math import *
from tkinter import *
from couleur import *
from random import *


def dessineLigne1(x1,x2,x3,x4,y,p1,p2,dessin):
	
	X1 = x1 + (x2-x1)/2
	X2 = x3 + (x4-x3)/2
	l1 = (p2*(X2-X1))/(p1+p2)
	X = X1 + l1
	dessin.create_line(X1,y,X1,y-50)
	dessin.create_line(X2,y,X2,y-50)
	dessin.create_line(X1,y-50,X2,y-50)
	dessin.create_line(X,y-50,X,y-100)

def dessineCercle2(x1,x2,y,p1,p2,dessin):

	x3 = x1 - sqrt(p1)
	x5 = x1 + sqrt(p1)
	x4 = x2 - sqrt(p2)
	x6 = x2 + sqrt(p2)
	y3 = y + 2*sqrt(p1)
	y4 = y + 2*sqrt(p2)
	i = randrange(len(colors))
	j = randrange(len(colors))
	print("colors[",i,"] = ",colors[i],"colors[",j,"] = ",colors[j])
	dessin.create_oval(x3,y,x5,y3,fill=colors[i])
	dessin.create_oval(x4,y,x6,y4,fill=colors[j])
	#dessineLigne1(x1,x3,x2,x4,y,p1,p2,dessin)

def dessineLigne2(x,y,p1,p2,l,dessin):

	l1 = (p2*l)/(p1+p2)
	x1 = x - l1
	x2 = x + (l-l1)

	dessin.create_line(x,y,x,y+50)
	dessin.create_line(x1,y+50,x2,y+50)
	dessin.create_line(x1,y+50,x1,y+100)
	dessin.create_line(x2,y+50,x2,y+100)


'''def construitMobile(x,y,p1,p2,l,dessin):

	l1 = (p2*l)/(p1+p2)
	x1 = x - l1
	x2 = x + (l-l1)
	
	
	dessineLigne2(x,y,p1,p2,l,dessin)
	dessineCercle2(x1,x2,y+100,p1,p2,dessin)'''


def sum(t):
	s = 0

	for e in t:
		s += e
	
	return s

def construitMobile(x,y,t,l,dessin):

	if len(t) == 1:
		if isinstance(t[0],list):
			
			p1 = t[0][0]
			p2 = t[0][1]

			l1 = (p2*l)/(p1+p2)
			x1 = x - l1
			x2 = x + (l-l1)

			dessineLigne2(x,y,p1,p2,l,dessin)
			dessineCercle2(x1,x2,y+100,p1,p2,dessin)

		else:
			i = randrange(len(colors))

			dessin.create_line(x,y,x,y+50)
			dessin.create_oval(x-sqrt(t[0]),y+50,x+sqrt(t[0]),y + 50 + 2*sqrt(t[0]),fill=colors[i])


	else:
		p1 = 0
		p2 = 0
		n = len(t)//2
		t1 = t[:n]
		t2 = t[n:]

		for p in t1:
			if isinstance(p,list):
				p1 += sum(p)
			else:
				p1 += p

		for p in t2:
			if isinstance(p,list):
				p2 += sum(p)
			else:
				p2 += p
		
		l1 = (p2*l)/(p1+p2)
		x1 = x - l1
		x2 = x + (l-l1)

		dessineLigne2(x,y,p1,p2,l,dessin)		
		construitMobile(x1,y+50,t1,l/2,dessin)
		construitMobile(x2,y+50,t2,l/2,dessin)

		

p1 = randrange(100,2000)
p2 = randrange(100,2000)

t = [[500,300],[800,1000],[400,700]]

fenetre = Tk()

dessin = Canvas(fenetre, width =1000, height=800)

dessin.pack()
#construitMobile(500,0,p1,p2,500,dessin)
#dessineLigne2(500,0,p1,p2,500,dessin)
#dessin.create_oval(50,100,150,200,fill='blue')
#dessin.create_oval(250,100,350,200,fill='red')
#dessineCercle1(50,250,100,p1,p2,dessin)
#dessineLigne(50,150,250,350,100,200,200,dessin)
construitMobile(500,0,t,500,dessin)
fenetre.mainloop()
	
	
