from time import *
from tkinter import *
from random import *
from modules.affichage import *
from modules.mouvements import *

def melange(root,cube,can,nombre):
	global timeur
	root.config(cursor="wait")
	melangeur(cube,can,nombre)
	root.after(nombre*timeur,lambda:root.config(cursor="gumby"))

def test():
	"""ceci est un test, lol"""
	start()
	rotative(cube,can,1,4,"u")
	rotative(cube,can,1,4,"u")
	rotative(cube,can,1,4,"u")
	rotative(cube,can,1,4,"u'")
	rotative(cube,can,1,4,"l")


cube=[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]

root=Tk()
root.config(cursor="gumby")
root.title("Rubik's Solveur")
root.iconbitmap("Rubik-Cube.ico")

can=Canvas(root,bg="#F0F0F0",height=550,width=710)
can.pack()
actualise(cube,can)

bou1=Button(root, text="mélanger", command=lambda:melange(root,cube,can,5), fg='blue')
bou1.pack()

bou2=Button(root, text="test", command=lambda:test(), fg='blue')
bou2.pack()

root.mainloop()