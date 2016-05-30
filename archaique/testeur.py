# Dans tout le programme le numéro des faces et des cases restent identique : c'est un repère en coordonnées absolue

from tkinter import *
from random import *
from time import *

# pour l'affichage graphique, tu t'en fou
def actualise(cube,can):
	for i in range(3):
		for j in range(3):
			can.create_rectangle(150+50*j,50*i,200+50*j,50+50*i,width=2,fill=cube[4][3*i+j])

	for z in range(4):
		for i in range(3):
			for j in range(3):
				can.create_rectangle(150*z+50*j,150+50*i,150*z+50+50*j,200+50*i,width=2,fill=cube[z][3*i+j])


	for i in range(3):
		for j in range(3):
			can.create_rectangle(150+50*j,300+50*i,200+50*j,350+50*i,width=2,fill=cube[5][3*i+j])

# Fonction très utile. Tu lui envoie le numéro d'une face et elle te renvoie une liste sous la forme :
# [faceAuDessus[numéroFaceDessus,coin adjacent à la face principal en partant de la droite,arrete adjacente,coin adjacent gauche],numéroFaceDroite[...],numéroFaceGauche[...],nméroFaceOppose]
def posRelative(face):
	if face==0:
		return [[4,0,3,6],[1,0,3,6],[5,6,3,0],[3,2,5,8],2]
	elif face==1:
		return [[4,6,7,8],[2,0,3,6],[5,0,1,2],[0,2,5,8],3]
	elif face==2:
		return [[4,8,5,2],[3,0,3,6],[5,2,5,8],[1,2,5,8],0]
	elif face==3:
		return [[4,2,1,0],[0,0,3,6],[5,8,7,6],[2,2,5,8],1]
	elif face==4:
		return [[3,2,1,0],[2,2,1,0],[1,0,1,2],[0,0,1,2],5]
	elif face==5:
		return [[1,6,7,8],[2,6,7,8],[3,8,7,6],[0,8,7,6],4]

# sert à la rotation d'une face. 
def rotation(cube,can,face,sens):
	if sens=="droite":
		cube[face][0],cube[face][1],cube[face][2],cube[face][5],cube[face][8],cube[face][7],cube[face][6],cube[face][3] = cube[face][6],cube[face][3],cube[face][0],cube[face][1],cube[face][2],cube[face][5],cube[face][8],cube[face][7]
		pos=posRelative(face)
		cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]], cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]], cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]] = cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]], cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]], cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]]

	elif sens=="gauche":
		cube[face][0],cube[face][1],cube[face][2],cube[face][5],cube[face][8],cube[face][7],cube[face][6],cube[face][3] = cube[face][2],cube[face][5],cube[face][8],cube[face][7],cube[face][6],cube[face][3],cube[face][0],cube[face][1]
		pos=posRelative(face)
		cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]], cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]], cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]] = cube[pos[1][0]][pos[1][1]], cube[pos[1][0]][pos[1][2]], cube[pos[1][0]][pos[1][3]], cube[pos[2][0]][pos[2][3]], cube[pos[2][0]][pos[2][2]], cube[pos[2][0]][pos[2][1]], cube[pos[3][0]][pos[3][3]], cube[pos[3][0]][pos[3][2]], cube[pos[3][0]][pos[3][1]], cube[pos[0][0]][pos[0][1]], cube[pos[0][0]][pos[0][2]], cube[pos[0][0]][pos[0][3]]

	actualise(cube,can)
	sleep(1)

def boussole(sensChiffre):
	if sensChiffre<0:
		while sensChiffre<0:
			sensChiffre+=4
	elif sensChiffre>3:
		while sensChiffre>3:
			sensChiffre-=4
	return sensChiffre

def reconnaissanceDirection(sensChiffre):
	sensChiffre=boussole(sensChiffre)
	if sensChiffre==0:
		return "haut"
	elif sensChiffre==1:
		return "droite"
	elif sensChiffre==2:
		return "bas"
	elif sensChiffre==3:
		return "gauche"

def deReconnaissanceDirection(sens):
	if sens=="haut":
		return 0
	elif sens=="droite":
		return 1
	elif sens=="bas":
		return 2
	elif sens=="gauche":
		return 3

def arreteOppose(indice):
	if indice==1:
		return 7
	elif indice==5:
		return 3
	elif indice==7:
		return 1
	elif indice==3:
		return 5

def Axe(cube,can,face,faceSup,sens):
	sensGlobal=[]
	pos=posRelative(face)
	for i in range(4):
		if pos[i][0]==faceSup:
			sensChiffre=i

	sens=int(deReconnaissanceDirection(sens))
	sensGlobal=reconnaissanceDirection(sensChiffre+sens)

	if sensGlobal=="haut":
		cube[face][1], cube[face][4], cube[face][7], cube[posRelative(face)[2][0]][posRelative(face)[2][2]], cube[posRelative(face)[2][0]][4], cube[posRelative(face)[2][0]][arreteOppose(posRelative(face)[2][2])], cube[posRelative(face)[4]][7], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][1], cube[posRelative(face)[0][0]][arreteOppose(posRelative(face)[0][2])], cube[posRelative(face)[0][0]][4], cube[posRelative(face)[0][0]][posRelative(face)[0][2]] = cube[posRelative(face)[2][0]][posRelative(face)[2][2]], cube[posRelative(face)[2][0]][4], cube[posRelative(face)[2][0]][arreteOppose(posRelative(face)[2][2])], cube[posRelative(face)[4]][7], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][1], cube[posRelative(face)[0][0]][arreteOppose(posRelative(face)[0][2])], cube[posRelative(face)[0][0]][4], cube[posRelative(face)[0][0]][posRelative(face)[0][2]], cube[face][1], cube[face][4], cube[face][7]
	elif sensGlobal=="droite":
		cube[face][3], cube[face][4], cube[face][5], cube[posRelative(face)[1][0]][posRelative(face)[1][2]], cube[posRelative(face)[1][0]][4], cube[posRelative(face)[1][0]][arreteOppose(posRelative(face)[1][2])], cube[posRelative(face)[4]][3], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][5], cube[posRelative(face)[3][0]][arreteOppose(posRelative(face)[3][2])], cube[posRelative(face)[3][0]][4], cube[posRelative(face)[3][0]][posRelative(face)[3][2]] = cube[posRelative(face)[3][0]][arreteOppose(posRelative(face)[3][2])], cube[posRelative(face)[3][0]][4], cube[posRelative(face)[3][0]][posRelative(face)[3][2]], cube[face][3], cube[face][4], cube[face][5], cube[posRelative(face)[1][0]][posRelative(face)[1][2]], cube[posRelative(face)[1][0]][4], cube[posRelative(face)[1][0]][arreteOppose(posRelative(face)[1][2])], cube[posRelative(face)[4]][3], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][5]
	elif sensGlobal=="gauche":
		cube[face][3], cube[face][4], cube[face][5], cube[posRelative(face)[1][0]][posRelative(face)[1][2]], cube[posRelative(face)[1][0]][4], cube[posRelative(face)[1][0]][arreteOppose(posRelative(face)[1][2])], cube[posRelative(face)[4]][3], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][5], cube[posRelative(face)[3][0]][arreteOppose(posRelative(face)[3][2])], cube[posRelative(face)[3][0]][4], cube[posRelative(face)[3][0]][posRelative(face)[3][2]] = cube[posRelative(face)[1][0]][posRelative(face)[1][2]], cube[posRelative(face)[1][0]][4], cube[posRelative(face)[1][0]][arreteOppose(posRelative(face)[1][2])], cube[posRelative(face)[4]][3], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][5], cube[posRelative(face)[3][0]][arreteOppose(posRelative(face)[3][2])], cube[posRelative(face)[3][0]][4], cube[posRelative(face)[3][0]][posRelative(face)[3][2]], cube[face][3], cube[face][4], cube[face][5]
	elif sensGlobal=="bas":
		cube[face][1], cube[face][4], cube[face][7], cube[posRelative(face)[2][0]][posRelative(face)[2][2]], cube[posRelative(face)[2][0]][4], cube[posRelative(face)[2][0]][arreteOppose(posRelative(face)[2][2])], cube[posRelative(face)[4]][7], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][1], cube[posRelative(face)[0][0]][arreteOppose(posRelative(face)[0][2])], cube[posRelative(face)[0][0]][4], cube[posRelative(face)[0][0]][posRelative(face)[0][2]] = cube[posRelative(face)[0][0]][arreteOppose(posRelative(face)[0][2])], cube[posRelative(face)[0][0]][4], cube[posRelative(face)[0][0]][posRelative(face)[0][2]], cube[face][1], cube[face][4], cube[face][7], cube[posRelative(face)[2][0]][posRelative(face)[2][2]], cube[posRelative(face)[2][0]][4], cube[posRelative(face)[2][0]][arreteOppose(posRelative(face)[2][2])], cube[posRelative(face)[4]][7], cube[posRelative(face)[4]][4], cube[posRelative(face)[4]][1]

	actualise(cube,can)

def rotationHaut(cube,can,face,faceSup,sens):
	if sens=="gauche":
		rotation(cube,can,faceSup,"droite")
	elif sens=="droite":
		rotation(cube,can,faceSup,"gauche")

def rotationBas(cube,can,face,faceSup,sens):
	faceBas=posRelative(faceSup)[4]
	rotation(cube,can,faceBas,sens)

def rotationDroite(cube,can,face,faceSup,sens):
	pos=posRelative(face)
	for i in range(4):
		if pos[i][0]==faceSup:
			supChiffre=i
	faceDroite=posRelative(face)[boussole(supChiffre+1)][0]
	if sens=="haut":
		rotation(cube,can,faceDroite,"droite")
	elif sens=="bas":
		rotation(cube,can,faceDroite,"gauche")

def rotationGauche(cube,can,face,faceSup,sens):
	pos=posRelative(face)
	for i in range(4):
		if pos[i][0]==faceSup:
			supChiffre=i
	faceDroite=posRelative(face)[boussole(supChiffre-1)][0]
	if sens=="haut":
		rotation(cube,can,faceDroite,"gauche")
	elif sens=="bas":
		rotation(cube,can,faceDroite,"droite")

def melangeur(cube,can,nombre):
	for i in range(nombre):
		sens=choice(["droite","gauche"])
		face=randint(0,5)
		rotation(cube,can,face,sens)

def timer(waitingFor):
	a = clock()
	b = clock()
	while b < a + waitingFor:
		b = clock()
		

# initialisation de la liste, les faces vont de 1 à 5 (selon leur indice) et chaque case d'une face est numéroté de 0 à 8
cube=[["green","green","green","green","green","green","green","green","green"],["red","red","red","red","red","red","red","red","red"],["blue","blue","blue","blue","blue","blue","blue","blue","blue"],["orange","orange","orange","orange","orange","orange","orange","orange","orange"],["white","white","white","white","white","white","white","white","white"],["yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow"]]

main=Tk()

can=Canvas(main,bg="white",height=450,width=600)
can.pack()
actualise(cube,can)
bou1=Button(main, text="mélanger", command=lambda:melangeur(cube,can,20), fg='blue')
bou1.pack()

# pour que tu puisses tester tes trucs. Pour utiliser mes fonctions ensuite il faudra que tu prennes "cube" et "can" en argument
bou2=Button(main, text="gauche face centre", command=lambda:rentreTaFonctionIci, fg='blue')
bou2.pack()
