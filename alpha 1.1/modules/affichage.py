
# pour l'affichage graphique
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