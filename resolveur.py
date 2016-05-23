from time import *
from tkinter import *
from random import *
import webbrowser
from modules.affichage import *
from modules.mouvements import *
from modules.recherche import *
from modules.menu import *
from modules.gestionnaire import *


def dec(cube,can,faceT):
	if faceT[0]==0:
		if faceT[1]==2: faceT[1]=0
		elif faceT[1]==5: faceT[1]=1
		elif faceT[1]==8: faceT[1]=2
		elif faceT[1]==1: faceT[1]=3
		elif faceT[1]==7: faceT[1]=5
		elif faceT[1]==0: faceT[1]=6
		elif faceT[1]==3: faceT[1]=7
		elif faceT[1]==6: faceT[1]=8
	if faceT[0]==2:
		if faceT[1]==6: faceT[1]=0
		elif faceT[1]==3: faceT[1]=1
		elif faceT[1]==0: faceT[1]=2
		elif faceT[1]==7: faceT[1]=3
		elif faceT[1]==1: faceT[1]=5
		elif faceT[1]==8: faceT[1]=6
		elif faceT[1]==5: faceT[1]=7
		elif faceT[1]==2: faceT[1]=8
	if faceT[0]==4:
	 	if faceT[1]==8: faceT[1]=0
	 	elif faceT[1]==7: faceT[1]=1
	 	elif faceT[1]==6: faceT[1]=2
	 	elif faceT[1]==5: faceT[1]=3
	 	elif faceT[1]==3: faceT[1]=5
	 	elif faceT[1]==2: faceT[1]=6
	 	elif faceT[1]==1: faceT[1]=7
	 	elif faceT[1]==0: faceT[1]=8
	return faceT

def verificateur(cube,etape):
	i=0
	if etape==1:
		if cube[1][1]=="red":
			i=i+1
		if cube[1][3]=="red":
			i=i+1
		if cube[1][5]=="red":
			i=i+1
		if cube[1][7]=="red":
			i=i+1
		if cube[0][5]=="green":
			i=i+1
		if cube[5][1]=="yellow":
			i=i+1
		if cube[2][3]=="blue":
			i=i+1
		if cube[4][7]=="white":
			i=i+1
		if i==8:
			return 1
		else:
			return 0

	if etape==2:
		if cube[1][0]=="red":
			i=i+1
		if cube[1][6]=="red":
			i=i+1
		if cube[1][8]=="red":
			i=i+1
		if cube[1][2]=="red":
			i=i+1
		if cube[0][2]=="green":
			i=i+1
		if cube[0][8]=="green":
			i=i+1
		if cube[2][0]=="blue":
			i=i+1
		if cube[2][6]=="blue":
			i=i+1
		if i==8:
			return 2
		else:
			return 0

	if etape==3:
		if cube[0][1]=="green":
			i=i+1
		if cube[0][7]=="green":
			i=i+1
		if cube[2][1]=="blue":
			i=i+1
		if cube[2][7]=="blue":
			i=i+1
		if cube[4][3]=="white":
			i=i+1
		if cube[4][5]=="white":
			i=i+1
		if cube[5][3]=="yellow":
			i=i+1
		if cube[5][5]=="yellow":
			i=i+1
		if i==8:
			return 3
		else:
			return 0

	if etape==4:
		if cube[3][1]=="orange":
			i=i+1
		if cube[3][3]=="orange":
			i=i+1
		if cube[3][5]=="orange":
			i=i+1
		if cube[3][7]=="orange":
			i=i+1
		if i==4:
			return 4
		else:
			return 0
	if etape==5:
		if cube[0][1]=="green":
			i=i+1
		if cube[2][5]=="blue":
			i=i+1
		if cube[4][1]=="white":
			i=i+1
		if cube[5][7]=="yellow":
			i=i+1
		if i==4:
			return 5
		else:
			return 0
	if etape==6:
		if cube[3][1]=="orange":
			i=i+1
		if cube[3][3]=="orange":
			i=i+1
		if cube[3][5]=="orange":
			i=i+1
		if cube[3][7]=="orange":
			i=i+1
		if i==4:
			return 6
		else:
			return 0
	if etape==7:
		if cube[4][0]=="white":
			i=i+1
		elif cube[4][0]=="green":
			i=i+1
		elif cube[4][0]=="orange":
			i=i+1
		if cube[0][0]=="white":
			i=i+1
		elif cube[0][0]=="green":
			i=i+1
		elif cube[0][0]=="orange":
			i=i+1
		if cube[3][2]=="white":
			i=i+1
		elif cube[3][2]=="green":
			i=i+1
		elif cube[3][2]=="orange":
			i=i+1
		if cube[2][2]=="white":
			i=i+1
		elif cube[2][2]=="blue":
			i=i+1
		elif cube[2][2]=="orange":
			i=i+1
		if cube[3][0]=="white":
			i=i+1
		elif cube[3][0]=="blue":
			i=i+1
		elif cube[3][0]=="orange":
			i=i+1
		if cube[4][2]=="white":
			i=i+1
		elif cube[4][2]=="blue":
			i=i+1
		elif cube[4][2]=="orange":
			i=i+1
		if i==6:
			return i
		else:
			return 0
	if etape==8:
		if cube==[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]:
			return 8
		else:
			return 0

def test(cube,can):
	print(verificateur(cube,8))

def step1(cube,can):
	if verificateur(cube,1)==1:
		step2(cube,can)

	ct=dec(cube,can,findArrete(cube,can,coul2))
	if ct[1]==7:
		while ct[0]!=coul2:
			rotative(cube,can,ct[])




def step1m(cube,can,face,indice):
	
	if indice==1: 
		rotative (cube,can,face,"red","F")
		rotative (cube,can,face,"red","F")
	elif indice==2:
		rotative (cube,can,face,"red","D")
		if face=="blue":
			face="white"
		elif face=="white":
			face="green"
		elif face=="green":
			face="yellow"
		elif face=="yellow":
			face="blue"
		rotative (cube,can,face,"red","F")
		rotative (cube,can,face,"red","L'")
		rotative (cube,can,face,"red","F'")		
def step2m(cube,can,face,indice):
	if indice==1: #en desous a gauche
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","L")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","L'")
	elif indice==12: # en dessous a droite
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","R'")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","R")
	elif indice==2: #au dessus a gauche
		rotative (cube,can,face,"red","L")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","L'")
		step2m(cube,can,face,1)
	elif indice==21: #au dessis a droite
		rotative (cube,can,face,"red","R'")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","R")
		step2m(cube,can,face,11)
	elif indice==3: #en dessous a gauche
		rotative (cube,can,face,"red","L")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","L'")
		rotative (cube,can,face,"red","F'")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","F")
	elif indice==31: #en dessous a droite
		rotative (cube,can,face,"red","R'")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","R")
		rotative (cube,can,face,"red","F")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","F'")
def step3m(cube,can,face,indice):
	if indice==1: #belge a gauche
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","L")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","L'")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","F'")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","F")
	elif indice==2: #belge a droite
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","R'")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","R")
		rotative (cube,can,face,"red","D")
		rotative (cube,can,face,"red","F")
		rotative (cube,can,face,"red","D'")
		rotative (cube,can,face,"red","F'"