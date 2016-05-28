from time import *
from tkinter import *
from random import *
import webbrowser
from modules.affichage import *
from modules.mouvements import *
from modules.recherche import *
from modules.menu import *
from modules.gestionnaire import *

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

def test(cube,can):
	print(verificateur(cube,1))
