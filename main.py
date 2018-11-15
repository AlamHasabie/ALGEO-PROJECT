from coba import *
from graphic import *
import numpy as np

START_VERTICES = []
CURRENT_VERTICES = []
EDGES = []
dimension = 0



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
	output_matrix = dilate(np.matrix(CURRENT_VERTICES),factor)
	current_matrix = np.matrix(CURRENT_VERTICES)
	CURRENT_VERTICES = output_matrix.tolist()
	diff_matrix = output_matrix - current_matrix
	diff_matrix = diff_matrix/60
	i=0
	while i<60:
		current_matrix = current_matrix + diff_matrix
		render_polygon(current_matrix.tolist())
		i=i+1
	render_polygon(CURRENT_VERTICES)
def animate_rotate(command) :
	global CURRENT_VERTICES
	i = 0
	while i < int(command[1]) :
		matrix = np.matrix(CURRENT_VERTICES)
		matrix = rotate2D(matrix,1,float(command[2]),float(command[3]))
		CURRENT_VERTICES = matrix.tolist()
		render_polygon(CURRENT_VERTICES)
		i=i+1
	
def animate_shear(command) :
	global CURRENT_VERTICES
	matrix_current = np.matrix(CURRENT_VERTICES)
	matrix_output = shear(matrix_current,command[1],float(command[2]),0)
	CURRENT_VERTICES = matrix_output.tolist()
	diff_matrix = matrix_output-matrix_current
	diff_matrix=diff_matrix/120
	i=0
	while i<120 :
		matrix_current = matrix_current + diff_matrix
		render_polygon(matrix_current.tolist())
		i=i+1
	#CURRENT_VERTICES = shear(np.matrix(CURRENT_VERTICES),command[1],float(command[2]),0).tolist()
	render_polygon(CURRENT_VERTICES)
def animate_stretch(command) :
	global CURRENT_VERTICES
	output_matrix = stretch(np.matrix(CURRENT_VERTICES),command[1],float(command[2]))
	current_matrix = np.matrix(CURRENT_VERTICES)
	CURRENT_VERTICES = output_matrix.tolist()
	diff_matrix = output_matrix - current_matrix
	diff_matrix = diff_matrix/60
	i=0
	while i<60 :
		current_matrix = current_matrix + diff_matrix
		render_polygon(current_matrix.tolist())
		i=i+1
	render_polygon(CURRENT_VERTICES)
def animate_reflect(command) :
	global CURRENT_VERTICES
	output_matrix = reflect(np.matrix(CURRENT_VERTICES),command[1],2)
	current_matrix = np.matrix(CURRENT_VERTICES)
	CURRENT_VERTICES = output_matrix.tolist()
	diff_matrix = output_matrix-current_matrix 
	diff_matrix = diff_matrix/60
	i=0
	while i<60 :
		current_matrix = current_matrix +diff_matrix
		render_polygon(current_matrix.tolist())
		i=i+1
	render_polygon(CURRENT_VERTICES)


def animate_custom(command) :
	global CURRENT_VERTICES
	output_matrix = custom(np.matrix(CURRENT_VERTICES),command,2)
	current_matrix = np.matrix(CURRENT_VERTICES)
	diff_matrix = output_matrix - current_matrix
	CURRENT_VERTICES = output_matrix.tolist()
	i=0
	diff_matrix = diff_matrix/60
	while i<60 :
		current_matrix = current_matrix + diff_matrix
		render_polygon(current_matrix.tolist())
		i = i+1
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


def dimension3() :
	global dimension
	global START_VERTICES
	global CURRENT_VERTICES
	global EDGES
	init_window_3d()
	START_VERTICES = [
		[-100.0,100.0,-100.0],
		[100.0,100.0,-100.0],
		[100.0,100.0,100.0],
		[-100.0,100.0,100.0],
		[-100.0,-100.0,-100.0],
		[100.0,-100.0,-100.0],
		[100.0,-100.0,100.0],
		[-100.0,-100.0,100.0]
	]
	CURRENT_VERTICES = START_VERTICES
	EDGES = [
		[0,1],
		[1,2],
		[2,3],
		[3,0],
		[4,5],
		[5,6],
		[6,7],
		[7,4],
		[0,4],
		[1,5],
		[2,6],
		[3,7]
	]
	render_cube(CURRENT_VERTICES,EDGES)
	while True:
		i=1
	return 0


def main():
	global dimension
	global CURRENT_VERTICES
	global START_VERTICES
	while dimension!=2 and dimension !=3 :
		dimension = int(input("Masukkan dimensi : "))
		if dimension!=2 and dimension !=3 :
			print("Saat ini program belum mampu menerima dimensi di luar nalar anda. Masukkan ulang : ")
	if dimension ==3 :
		dimension3()
		is_running_2d = False
	else :
		is_running_2d = True
		START_VERTICES = input_vertices()
		CURRENT_VERTICES = START_VERTICES
		init_window()
		render_polygon(CURRENT_VERTICES)
	while is_running_2d :
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