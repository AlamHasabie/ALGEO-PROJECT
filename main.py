from coba import *
from graphic import *

START_VERTICES = []
CURRENT_VERTICES = []



def animate_translate_2d(dx,dy) :
	global CURRENT_VERTICES
	a_dx = dx/60
	a_dy = dy/60
	i=1
	while i<=60 :
		CURRENT_VERTICES = translate(CURRENT_VERTICES,a_dx,a_dy,0)
		render_polygon(CURRENT_VERTICES)
		i=i+1
	render_polygon([[200,0,0],[0,200,0],[0,0,0]])

#def animate_dilate(factor) :
#def animate_rotate(command) :
#def animate_shear(command) :
#def animate_stretch(command) :
#def animate_reflect(command) :
#def animate_custom(command) :
#def multiple(n_iterations) :




def main():
	global CURRENT_VERTICES
	global START_VERTICES
	START_VERTICES = input_vertices()
	CURRENT_VERTICES = START_VERTICES
	init_window()
	render_polygon(CURRENT_VERTICES)
	while True :
		command = input('Masukkan perintah :')
		command = command.split(" ")
		if command[0] == 'dilate' :
			animate_dilate(float(command[1]))
		elif(command[0] == 'translate'):
			animate_translate_2d(float(command[1]),float(command[2]))
		elif(command[0] == 'custom'):
			animate_custom(command)
		elif(command[0] == 'rotate'):
			animate_rotate(command)
		elif(command[0] == 'shear'):
			animate_shear(command)
		elif(command[0] == 'stretch'):
			animate_stretch(command)
		elif(command[0] == 'reflect'):
			animate_reflect(command)
		elif(command[0]== 'multiple') :
			multiple()
		elif(command[0]=='reset'):
			CURRENT_VERTICES = START_VERTICES
			render_polygon(CURRENT_VERTICES)
		else :
			print('Perintah salah. Masukkan perintah kembali :')

main()