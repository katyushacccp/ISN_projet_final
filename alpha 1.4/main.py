from time import *
from tkinter import *
from random import *
import webbrowser
from modules.affichage import *
from modules.mouvements import *
from modules.menu import *

def test():
	rotative(cube,can,1,4,"u")

def melange(root,cube,can,nombre):
	global timeur
	root.config(cursor="wait")
	melangeur(cube,can,nombre)
	root.after(nombre*timeur,lambda:root.config(cursor="gumby"))


cube=[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]

root=Tk()
root.config(cursor="gumby")
root.title("Rubik's Solveur")
root.iconbitmap("Rubik-Cube.ico")

menuBar = Menu(root)

menuFichier = Menu(menuBar, tearoff=0)
menuFichier.add_command(label="Réinitialiser le cube",command=lambda:reboot(cube,can))
menuFichier.add_command(label="Entrer une nouvelle configuration",command=lambda:configurationCube(cube,can,"new"))
menuFichier.add_command(label="Modifier la configuration",command=lambda:configurationCube(cube,can))
menuFichier.add_separator()
menuFichier.add_command(label="Quitter",command=root.destroy)
menuBar.add_cascade(label="Fichier",menu=menuFichier)

menuAide = Menu(menuBar, tearoff=0)
menuAide.add_command(label="Consulter le site web",command=lambda:webbrowser.open('https://www.google.fr/search?hl=fr&site=imghp&tbm=isch&source=hp&biw=1366&bih=643&q=pretty+kittens&oq=pretty+kittens&gs_l=img.3..0i19l2j0i30i19j0i8i30i19l5.2527.5907.0.6304.14.13.0.1.1.0.159.1511.0j12.12.0....0...1ac.1.64.img..1.13.1521.qbq-0Gvw6NM'))
menuAide.add_command(label="Consulter la licence de l'icone",command=lambda:licence("icone"))
menuAide.add_command(label="Consulter la licence du programme",command=lambda:licence("programme"))
menuBar.add_cascade(label="Aide",menu=menuAide)

root.config(menu=menuBar)

can=Canvas(root,bg="#F0F0F0",height=550,width=710)
can.grid(row=0, column=0)
actualise(cube,can)