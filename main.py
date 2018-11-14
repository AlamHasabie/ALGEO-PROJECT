from coba import *
from graphic import *

global start_vertices
global current_vertices



#def animate_translate(dx,dy) :
#def animate_dilate(factor) :
#def animate_rotate(command) :
#def animate_shear(command) :
#def animate_stretch(command) :
#def animate_reflect(command) :
#def animate_custom(command) :
#def multiple(n_iterations) :




def main():
	start_vertices = input_vertices()
	current_vertices = start_vertices
	init_window()
	render_polygon(current_vertices)
	while True :
		command = input('Masukkan perintah :')
		command = command.split(" ")
		if command[0] == 'dilate' :
			animate_dilate(float(command[1]))
		elif(command[0] == 'translate'):
			animate_translate(float(command[1]),float(command[2]))
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
			current_vertices = start_vertices
			render_polygon(current_vertices)
		else :
			print('Perintah salah. Masukkan perintah kembali :')

main()