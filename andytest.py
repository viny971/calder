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

def construitMobile(x,y,t,l):
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
		construitMobile(x1,y+50,t1,l/2)
		construitMobile(x2,y+50,t2,l/2)
        
		
def construitListe1(): #Permet à l'utilisateur de créer son propre mobile
	l = []
	tn = entPdsAlea.get().split(" ")
	e = []
	n = int(entPdsNum.get())
	t = [0]*n
	for i in range(n):
		t[i]=int(tn[i])
	for i in range(n):
		e.append(t[i])
		if (i+1)%2 == 0:
			l.append(e)
			e = []
	if e != []:
		l.append(e[0])
	return l

def construitListe2(fic): #Construit un mobile à partir de poids écrit dans un fichier. Ecrit l'arbre correspondant dans un fichier
	t, l, c = [], [], 0
	fichier1 = open(fic, "r")
	l1 = fichier1.readlines()
	lg =len(l1)
	print(l1)
	fichier2 = open("arbre2.txt", "w")
	l1 = l1[:lg-1:]
	for el in l1:
		el.replace('\n','')
		t.append(int(el))
		c += 1
		if c%2 == 0:	
			l.append(t)
			t = []
	s = str(l)
	fichier2.write(s)
	print(l)			
	return l
	
def construitListe3(fic): #Construit un mobile à partir d'un arbre écrit dans un fichier
	fichier = open(fic, "r")
	ligne = fichier.readlines()[0]
	print(ligne)
	l = eval(ligne)
	return l

def construit_arbre():
	dessin.delete("all")
	dessin.create_image(500,500,image=fond)
	text = entArbre.get()
	l = construitListe3(text)
	construitMobile(500,0,l,500)
	
def construit_poidsAlea():
	dessin.delete("all")
	dessin.create_image(500,500,image=fond)
	l = construitListe1()
	construitMobile(500,0,l,500)

def construit_poidsCol():
	dessin.delete("all")
	dessin.create_image(500,500,image=fond)
	poids=entPdsCol.get()
	l = construitListe2(poids)
	construitMobile(500,0,l,500)

fenetre = Tk()
fenetre.title("Projet TacoLimmois de LS4")

labArbre= Label(fenetre,text="Fichier contenant un arbre listé", fg="red")
labPdsCol= Label(fenetre,text="Fichier contenant des poids", fg="red")
labPdsNum=Label(fenetre,text="Entrez le nombre de poids", fg="red")
labPdsAlea=Label(fenetre,text="Entrez chacun des poids suivi d'un espace", fg="red")

buttArbre= Button(fenetre, text = "Créer", command=construit_arbre)
buttPdsCol= Button(fenetre, text = "Créer", command=construit_poidsCol)
buttPdsAlea =Button(fenetre, text = "Créer", command=construit_poidsAlea)

dessin = Canvas(fenetre, width=1000, height=800,bg="white")

entArbre= Entry(fenetre)
entPdsCol=Entry(fenetre)
entPdsNum=Entry(fenetre)
entPdsAlea=Entry(fenetre)

labArbre.grid(row=1,column=0)
entArbre.grid(row=1,column=1)
buttArbre.grid(row=1,column = 4)

labPdsCol.grid(row=2,column=0)
entPdsCol.grid(row=2,column=1)
buttPdsCol.grid(row=2, column =4)

labPdsNum.grid(row=3,column=0)
labPdsAlea.grid(row=3,column=2)
entPdsNum.grid(row=3,column=1)
entPdsAlea.grid(row=3,column=3)
buttPdsAlea.grid(row=3,column=4)

fond = PhotoImage(file="image3.gif")
dessin.create_image(500,500,image=fond)
dessin.grid(row=4,columnspan=5)
fenetre.mainloop()
