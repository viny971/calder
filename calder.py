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
	dessin.create_oval(x3,y,x5,y3,fill=colors[i])
	dessin.create_oval(x4,y,x6,y4,fill=colors[j])
	#dessineLigne1(x1,x3,x2,x4,y,p1,p2,dessin)

def dessineLigne2(x,y,p1,p2,l,dessin):

	l1 = (p2*l)/(p1+p2)
	x1 = x - l1
	x2 = x + (l-l1)

	dessin.create_line(x,y,x,y + 50)
	dessin.create_line(x1,y+50,x2,y+50)
	dessin.create_line(x1,y+50,x1,y+100)
	dessin.create_line(x2,y+50,x2,y+100)


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

		


#t = [[1000,500],[800,1000],[400,700],[850,354],[200,600],2000]

def construitListe1(): #Permet à l'utilisateur de créer son propre mobile

	l = []
	t = []
	e = 0
	print("Combien de poids voulez-vous entrer ?")
	n = int(input())
	print("Entrez la liste des poids :");

	for i in range(n):
		e = int(input())	
		t.append(e)
		if (i+1)%2 == 0:
			l.append(t)
			t = []

	if t != []: l.append(t[0])

	return l

def construitListe2(fic): #Construit un mobile à partir de poids écrit dans un fichier. Ecrit l'arbre correspondant dans un fichier

	t, l, c = [], [], 0

	fichier1 = open(fic, "r")
	fichier2 = open("arbre2.txt", "a")

	for ligne in fichier1:
		
		t.append(int(ligne.replace('\n','')))
		c += 1
		if c%2 == 0:	
			l.append(t)
			t = []
	s = str(l)
	fichier2.write(s)
	print(l)			
	return l

def Andy(n):
	return n+1:

def construitListe3(fic): #Construit un mobile à partir d'un arbre écrit dans un fichier

	fichier = open(fic, "r")

	ligne = fichier.readlines()[0]
	print(ligne)
	l = eval(ligne)

	return l


l = construitListe2("poids.txt")

fenetre = Tk()

dessin = Canvas(fenetre, width=1000, height=800)
dessin.pack()

#fond = PhotoImage(file="pictures/p3.gif")
#dessin.create_image(0,0,image=fond,anchor=NW)

construitMobile(500,0,l,500,dessin)
fenetre.mainloop()
	
	
