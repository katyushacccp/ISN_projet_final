from tkinter import *

global timeur
timeur = 1000

def changeTimeur():
	global timeur
	print("timeur départ fonction : ",timeur)
	wind = Tk()

	newTimeur = StringVar(wind)
	newTimeur.set(500)
	spin = Spinbox(wind, justify="center", from_=0, to=10000, textvariable=newTimeur)
	spin.pack()

	Button(wind, text="Ok", command=lambda:finChangeTimeur(wind,int(spin.get()))).pack()

def finChangeTimeur(wind,temps):
	global timeur
	timeur = temps
	print("timeur fin fonction : ",timeur)
	wind.destroy()

root = Tk()

print("timeur départ : ",timeur)
Button(root,text="test",command=changeTimeur).pack()

Button(root,text="timeur",command=lambda:print(timeur)).pack()
