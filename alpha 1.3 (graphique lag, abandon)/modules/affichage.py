from modules.recherche import *

global timeur
timeur = 4000

def rotationAnimal(cube,can,i=0,cent=0,cinquante=0):
	global timeur

	can.create_rectangle(200,40, 350,190, fill="#F0F0F0", width=0)

	if i%3 == 0:
		cinquante += 1
		cent += 2

	can.create_polygon(250,140-cinquante, 300-cinquante,140, 300-cent,190-cinquante, 250-cinquante,190-cent, width=2,fill="green")

	if i<150:
		i += 1
		can.after(int(timeur/150), lambda:rotationAnim(cube,can,i,cent,cinquante))

def clear(cube,can):
	can.create_polygon(0,190, 190,190, 190,30, 360,30, 360,190, 680,190, 680,360, 360,360, 360,520, 190,520, 190,360, 30,360, 30,190, \
	0,190, 0,560, 720,560, 720,0, 0,0, fill="#F0F0F0", width=0)

	can.create_rectangle(70,177,160,190,width=1,fill=cube[4][4])
	can.create_rectangle(70,360,160,373,width=1,fill=cube[5][4])
	can.create_rectangle(390,177,480,190,width=1,fill=cube[4][4])
	can.create_rectangle(390,360,480,373,width=1,fill=cube[5][4])
	can.create_rectangle(550,177,640,190,width=1,fill=cube[4][4])
	can.create_rectangle(550,360,640,373,width=1,fill=cube[5][4])
	can.create_rectangle(230,17,320,30,width=1,fill=cube[3][4])
	can.create_rectangle(230,520,320,533,width=1,fill=cube[3][4])
	can.create_rectangle(17,230,30,320,width=1,fill=cube[3][4])
	can.create_rectangle(693,230,680,320,width=1,fill=cube[0][4])
	can.create_rectangle(177,70,190,160,width=1,fill=cube[0][4])
	can.create_rectangle(360,70,373,160,width=1,fill=cube[2][4])
	can.create_rectangle(177,390,190,480,width=1,fill=cube[0][4])
	can.create_rectangle(360,390,373,480,width=1,fill=cube[2][4])

def actualise(cube,can):
	for i in range(3): # la hauteur
		for j in range(3): # la longueur
			can.create_rectangle(20+180+50*j,20+20+50*i,20+230+50*j,20+70+50*i,width=2,fill=cube[4][3*i+j])

	for z in range(4):
		for i in range(3):
			for j in range(3):
				can.create_rectangle(20+20+160*z+50*j,20+180+50*i,20+70+160*z+50*j,20+230+50*i,width=2,fill=cube[z][3*i+j])


	for i in range(3):
		for j in range(3):
			can.create_rectangle(20+180+50*j,20+340+50*i,20+230+50*j,20+390+50*i,width=2,fill=cube[5][3*i+j])

	can.create_rectangle(20+170,20+10,20+180,20+500,width=0,fill="black")
	can.create_rectangle(20+330,20+10,20+340,20+500,width=0,fill="black")
	can.create_rectangle(20+10,20+170,20+20,20+340,width=0,fill="black")
	can.create_rectangle(20+490,20+170,20+500,20+340,width=0,fill="black")
	can.create_rectangle(20+650,20+170,20+660,20+340,width=0,fill="black")
	can.create_rectangle(20+10,20+170,20+660,20+180,width=0,fill="black")
	can.create_rectangle(20+10,20+330,20+660,20+340,width=0,fill="black")
	can.create_rectangle(20+170,20+10,20+330,20+20,width=0,fill="black")
	can.create_rectangle(20+170,20+490,20+330,20+500,width=0,fill="black")

	clear(cube,can)


def pixel(face,carre):
	if face == 0:
		return [40+50*(carre%3),200+50*(carre//3), 90+50*(carre%3),250+50*(carre//3)]
	if face == 1:
		return [200+50*(carre%3),200+50*(carre//3), 250+50*(carre%3),250+50*(carre//3)]
	if face == 2:
		return [360+50*(carre%3),200+50*(carre//3), 410+50*(carre%3),250+50*(carre//3)]
	if face == 3:
		return [520+50*(carre%3),200+50*(carre//3), 570+50*(carre%3),250+50*(carre//3)]
	if face == 4:
		return [200+50*(carre%3),40+50*(carre//3), 250+50*(carre%3),90+50*(carre//3)]
	if face == 5:
		return [200+50*(carre%3),360+50*(carre//3), 250+50*(carre%3),410+50*(carre//3)]

def setAnimCompteur(animCompteur):
	animCompteur[0] += 1

def rotationAnim(lowCube,cube,can,face,sens):
	animCompteur = [0]

	if face == 0:
		if sens == "droite":
			for i in range(150):
				can.after(i*int(timeur/150), lambda:setAnimCompteur(animCompteur))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,4,0,"bas"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,1,0,"bas"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,5,0,"bas"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,3,0,"haut"))
				can.after(i*int(timeur/150), lambda:clear(cube,can))
			can.after(timeur,lambda:actualise(cube,can))

		if sens == "gauche":
			for i in range(150):
				can.after(i*int(timeur/150), lambda:setAnimCompteur(animCompteur))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,4,0,"haut"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,1,0,"haut"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,5,0,"haut"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,3,0,"bas"))
				can.after(i*int(timeur/150), lambda:clear(cube,can))
			can.after(timeur,lambda:actualise(cube,can))

	if face == 1:
		if sens == "droite":
			for i in range(150):
				can.after(i*int(timeur/150), lambda:setAnimCompteur(animCompteur))
				can.after(i*int(timeur/150), lambda:ligne(lowCube,cube,can,animCompteur,4,6,"droite"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,2,0,"bas"))
				can.after(i*int(timeur/150), lambda:ligne(lowCube,cube,can,animCompteur,5,0,"gauche"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,0,2,"haut"))
				can.after(i*int(timeur/150), lambda:clear(cube,can))
			can.after(timeur,lambda:actualise(cube,can))

		if sens == "gauche":
			for i in range(150):
				can.after(i*int(timeur/150), lambda:setAnimCompteur(animCompteur))
				can.after(i*int(timeur/150), lambda:ligne(lowCube,cube,can,animCompteur,4,6,"gauche"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,2,0,"haut"))
				can.after(i*int(timeur/150), lambda:ligne(lowCube,cube,can,animCompteur,5,0,"droite"))
				can.after(i*int(timeur/150), lambda:colonne(lowCube,cube,can,animCompteur,0,2,"bas"))
				can.after(i*int(timeur/150), lambda:clear(cube,can))
			can.after(timeur,lambda:actualise(cube,can))


	

def colonne(lowCube,cube,can,animCompteur,face,carre,sens):
	if sens == "bas":
		for i in range(3):
			can.create_rectangle(pixel(face,carre)[0], pixel(face,carre)[1]+50*i+animCompteur[0], \
			pixel(face,carre)[2], pixel(face,carre)[3]+50*i+animCompteur[0], width=2,fill=cube[face][carre+3*i])

			can.create_rectangle(pixel(face,carre)[0], pixel(face,carre)[1]+50*i+animCompteur[0]-160, \
			pixel(face,carre)[2], pixel(face,carre)[3]+50*i+animCompteur[0]-160, width=2,fill=lowCube[face][carre+3*i])

	if sens == "haut":
		for i in range(3):
			can.create_rectangle(pixel(face,carre)[0], pixel(face,carre)[1]+50*i-animCompteur[0], \
			pixel(face,carre)[2], pixel(face,carre)[3]+50*i-animCompteur[0], width=2,fill=cube[face][carre+3*i])

			can.create_rectangle(pixel(face,carre)[0], pixel(face,carre)[1]+50*i-animCompteur[0]+160, \
			pixel(face,carre)[2], pixel(face,carre)[3]+50*i-animCompteur[0]+160, width=2,fill=lowCube[face][carre+3*i])

def ligne(lowCube,cube,can,animCompteur,face,carre,sens):
	if sens == "droite":
		for i in range(3):
			can.create_rectangle(pixel(face,carre)[0]+50*i+animCompteur[0], pixel(face,carre)[1], \
			pixel(face,carre)[2]+50*i+animCompteur[0], pixel(face,carre)[3], width=2,fill=cube[face][carre+i])

			can.create_rectangle(pixel(face,carre)[0]+50*i+animCompteur[0]-160, pixel(face,carre)[1], \
			pixel(face,carre)[2]+50*i+animCompteur[0]-160, pixel(face,carre)[3], width=2,fill=lowCube[face][carre+i])

	if sens == "gauche":
		for i in range(3):
			can.create_rectangle(pixel(face,carre)[0]+50*i-animCompteur[0], pixel(face,carre)[1], \
			pixel(face,carre)[2]+50*i-animCompteur[0], pixel(face,carre)[3], width=2,fill=cube[face][carre+i])

			can.create_rectangle(pixel(face,carre)[0]+50*i-animCompteur[0]+160, pixel(face,carre)[1], \
			pixel(face,carre)[2]+50*i-animCompteur[0]+160, pixel(face,carre)[3], width=2,fill=lowCube[face][carre+i])