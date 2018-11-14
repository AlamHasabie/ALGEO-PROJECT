from coba import *
from graphic import *
import numpy as np

START_VERTICES = []
CURRENT_VERTICES = []



def animate_translate_2d(dx,dy) :
	global CURRENT_VERTICES
	a_dx = dx/60
	a_dy = dy/60
	i=1
	while i<=60 :
		matrix = np.matrix(CURRENT_VERTICES)
		matrix = translate(matrix,a_dx,a_dy,0)
		CURRENT_VERTICES = matrix.tolist()
		render_polygon(CURRENT_VERTICES)
		i=i+1
def animate_dilate(factor) :
	global CURRENT_VERTICES
	matrix = np.matrix(CURRENT_VERTICES)
	output_matrix = dilate(matrix,factor)
	diff= output_matrix - matrix
	diff = diff/10
	print(diff)
	i=1
	while i<=10:
		matrix = matrix + diff
		CURRENT_VERTICES = matrix.tolist()
		render_polygon(CURRENT_VERTICES)
		i=i+1
def animate_rotate(command) :
	global CURRENT_VERTICES
	i = 1
	while i < int(command[1]) :
		matrix = np.matrix(CURRENT_VERTICES)
		matrix = rotate2D(matrix,1,float(command[2]),float(command[3]))
		CURRENT_VERTICES = matrix.tolist()
		render_polygon(CURRENT_VERTICES)
		i=i+1
def animate_shear(command) :
	global CURRENT_VERTICES
	CURRENT_VERTICES = shear(np.matrix(CURRENT_VERTICES),command[1],float(command[2]),0).tolist()
	render_polygon(CURRENT_VERTICES)
def animate_stretch(command) :
	global CURRENT_VERTICES
	CURRENT_VERTICES = stretch(np.matrix(CURRENT_VERTICES),command[1],float(command[2])).tolist()
	render_polygon(CURRENT_VERTICES)
def animate_reflect(command) :
	global CURRENT_VERTICES
	CURRENT_VERTICES = reflect(np.matrix(CURRENT_VERTICES),command[1],2).tolist()
	render_polygon(CURRENT_VERTICES)
def animate_custom(command) :
	global CURRENT_VERTICES
	CURRENT_VERTICES = custom(np.matrix(CURRENT_VERTICES),command,2).tolist()
	render_polygon(CURRENT_VERTICES)
def multiple(n_iterations) :
	i=1
	while(i<=n_iterations) :
		command = input()
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
		else :
			print('Perintah salah. Masukkan perintah kembali :')
		i=i+1





def main():
	global CURRENT_VERTICES
	global START_VERTICES
	START_VERTICES = input_vertices()
	CURRENT_VERTICES = START_VERTICES
	init_window()
	render_polygon(CURRENT_VERTICES)
	is_running = True
	while is_running :
		command = input('Masukkan perintah : ')
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
			multiple(int(command[1]))
		elif(command[0]=='reset'):
			CURRENT_VERTICES = START_VERTICES
			render_polygon(CURRENT_VERTICES)
		elif command[0]=='exit' :
			is_running = False
		else :
			print('Perintah salah. Masukkan perintah kembali :')

main()