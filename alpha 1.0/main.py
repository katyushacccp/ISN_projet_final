# Dans tout le programme le numéro des faces et des cases restent identique : c'est un repère en coordonnées absolue

from time import *
from tkinter import *
from random import *
from modules.affichage import *
from modules.mouvements import *



# initialisation de la liste, les faces vont de 1 à 5 (selon leur indice) et chaque case d'une face est numéroté de 0 à 8
cube=[["green"]*9,["red"]*9,["blue"]*9,["orange"]*9,["white"]*9,["yellow"]*9]

root=Tk()

can=Canvas(root,bg="white",height=450,width=600)
can.pack()

actualise(cube,can)
bou1=Button(root, text="mélanger", command=lambda:melangeur(cube,can,5), fg='blue')
bou1.pack()

# pour que tu puisses tester tes trucs. Pour utiliser mes fonctions ensuite il faudra que tu prennes "cube" et "can" en argument
bou2=Button(root, text="gauche face centre", command=lambda:rotation(cube,can,1,"droite"), fg='blue')
bou2.pack()

root.mainloop()
root.destroy()