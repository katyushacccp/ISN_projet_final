from tkinter import *
from modules.affichage import *

def reboot(cube,can):
	newCube=[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]

	for face in range(6):
		for carre in range(9):
			cube[face][carre]=newCube[face][carre]

	actualise(cube,can)

def changeCouleur(cube,bouton,face,carre):
	fenetre = Tk()
	fenetre.title("Couleur")
	fenetre.iconbitmap("Rubik-Cube.ico")

	Button(fenetre, width=25, pady=5, bg=couleurAffiche("red"), text="Rouge", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"red")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("blue"), text="Bleu", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"blue")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("green"), text="Vert", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"green")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("white"), text="Blanc", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"white")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("orange"), text="Orange", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"orange")).pack()
	Button(fenetre, width=25, pady=5, bg=couleurAffiche("yellow"), text="Jaune", \
		command=lambda:confirmeCouleur(fenetre,cube,bouton,face,carre,"yellow")).pack()

def confirmeCouleur(fenetre,cube,bouton,face,carre,couleur):
	bouton.config(bg=couleurAffiche(couleur))
	cube[face][carre]=couleur
	fenetre.destroy()

def configurationCube(cube,can,state=""):
	cubeConfig = Tk()
	cubeConfig.title("Configuration personnalisée")
	cubeConfig.iconbitmap("Rubik-Cube.ico")

	if state == "new":
		reboot(cube,can)

	face=[]
	facePosition=[[2,1], [2,2], [2,3], [2,4], [1,2], [3,2]]
	carre=[[]]*6
	carrePosition=[[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

	for i in range(6):
		face.append(Frame(cubeConfig, padx=5, pady=5))
		face[i].grid(row=facePosition[i][0], column=facePosition[i][1])

		for y in range(9):
			carre[i].append(Button(face[i],bg=couleurAffiche(cube[i][y]), width=6, height=3))
			carre[i][y].config(command=lambda:changeCouleur(cube,carre[i][y],i,y))
			carre[i][y].grid(row=carrePosition[y][0], column=carrePosition[y][1])

	

	Button(cubeConfig,text="Ok !",command=lambda:finCubeConfig(cube,can,cubeConfig)).grid(row=4,columnspan=5)

def finCubeConfig(cube,can,fen):
	fen.destroy()
	actualise(cube,can)

def licence(nom):
	fenetre = Tk()
	fenetre.title("Licence")
	fenetre.iconbitmap("Rubik-Cube.ico")

	if nom == "icone":
		Label(fenetre,text=rFile("licenceIcone","txt")).pack()

	elif nom == "programme":
		Label(fenetre,text=rFile("licenceProgramme","txt")).pack()

	Button(fenetre,text="Ok",command=fenetre.destroy).pack()

def changeTimeur():
	fenetre = Tk()
	fenetre.title("Réglage")
	fenetre.iconbitmap("Rubik-Cube.ico")

	Label(fenetre,text="Réglez le temps entre chaque coup en millisecondes :").pack()
	newTimeur = StringVar(fenetre)
	newTimeur.set(rFile("timeur","cub"))
	spin = Spinbox(fenetre, justify="center", from_=0, to=10000, increment=50, textvariable=newTimeur)
	spin.pack()

	Button(fenetre, text="Ok", command=lambda:finChangeTimeur(fenetre, newTimeur.get())).pack()

def finChangeTimeur(fenetre,newTimeur):
	wFile("timeur","cub",int(newTimeur))
	fenetre.destroy()

def changeNombreMelange():
	fenetre = Tk()
	fenetre.title("Réglage")
	fenetre.iconbitmap("Rubik-Cube.ico")

	Label(fenetre,text="Réglez le nombre de coups pour mélanger :").pack()
	newNombreMelange = StringVar(fenetre)
	newNombreMelange.set(rFile("nombreMelange","cub"))
	spin = Spinbox(fenetre, justify="center", from_=0, to=500, increment=1, textvariable=newNombreMelange)
	spin.pack()

	Button(fenetre, text="Ok", command=lambda:finChangeNombreMelange(fenetre, newNombreMelange.get())).pack()

def finChangeNombreMelange(fenetre,newNombreMelange):
	wFile("nombreMelange","cub",int(newNombreMelange))
	fenetre.destroy()