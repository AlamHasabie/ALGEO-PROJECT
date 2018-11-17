from coba import *
from graphic import *
import numpy as np

START_VERTICES = []
CURRENT_VERTICES = []
EDGES = []
dimension = 0



def animate_translate(dx,dy,dz) :
	global CURRENT_VERTICES
	global EDGES
	a_dx = dx/60
	a_dy = dy/60
	a_dz = dz/60
	i=1
	while i<=60 :
		matrix = translate(np.matrix(CURRENT_VERTICES),a_dx,a_dy,a_dz)
		CURRENT_VERTICES = matrix.tolist()
		if dimension==2 :
			render_polygon(CURRENT_VERTICES)
		else :
			render_cube(CURRENT_VERTICES,EDGES)
		i=i+1
def animate_dilate(factor) :
	global CURRENT_VERTICES
	global EDGES
	output_matrix = dilate(np.matrix(CURRENT_VERTICES),factor)
	current_matrix = np.matrix(CURRENT_VERTICES)
	CURRENT_VERTICES = output_matrix.tolist()
	diff_matrix = output_matrix - current_matrix
	diff_matrix = diff_matrix/60
	i=0
	while i<60:
		current_matrix = current_matrix + diff_matrix
		if dimension==2 :
			render_polygon(current_matrix.tolist())
		else :
			render_cube(current_matrix.tolist(),EDGES)
		i=i+1
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
	global EDGES
	global dimension
	matrix_current = np.matrix(CURRENT_VERTICES)
	matrix_output = shear(matrix_current,command[1],float(command[2]),0)
	CURRENT_VERTICES = matrix_output.tolist()
	diff_matrix = matrix_output-matrix_current
	diff_matrix=diff_matrix/60
	i=0
	while i<60 :
		matrix_current = matrix_current + diff_matrix
		if dimension==2 :
			render_polygon(matrix_current.tolist())
		else :
			render_cube(matrix_current.tolist(),EDGES)
		i=i+1
	#CURRENT_VERTICES = shear(np.matrix(CURRENT_VERTICES),command[1],float(command[2]),0).tolist()
	render_polygon(CURRENT_VERTICES)
def animate_stretch(command) :
	global CURRENT_VERTICES
	global EDGES
	output_matrix = stretch(np.matrix(CURRENT_VERTICES),command[1],float(command[2]))
	current_matrix = np.matrix(CURRENT_VERTICES)
	CURRENT_VERTICES = output_matrix.tolist()
	diff_matrix = output_matrix - current_matrix
	diff_matrix = diff_matrix/60
	i=0
	while i<60 :
		current_matrix = current_matrix + diff_matrix
		if dimension==2 :
			render_polygon(current_matrix.tolist())
		else :
			render_cube(current_matrix.tolist(),EDGES)
		i=i+1

def animate_reflect(command) :
	global CURRENT_VERTICES
	global EDGES
	current_matrix = np.matrix(CURRENT_VERTICES)
	output_matrix = reflect(np.matrix(CURRENT_VERTICES),command[1],dimension)
	CURRENT_VERTICES = output_matrix.tolist()
	diff_matrix = output_matrix-current_matrix 
	print(diff_matrix)
	diff_matrix = diff_matrix/60
	i=0
	while i<60 :
		current_matrix = current_matrix +diff_matrix
		if dimension==2 :
			render_polygon(current_matrix.tolist())
		else :
			render_cube(current_matrix.tolist(),EDGES)
		i=i+1


def animate_custom(command) :
	global CURRENT_VERTICES
	global EDGES
	current_matrix = np.matrix(CURRENT_VERTICES)
	output_matrix = custom(np.matrix(CURRENT_VERTICES),command,dimension)
	diff_matrix = output_matrix - current_matrix
	CURRENT_VERTICES = output_matrix.tolist()
	i=0
	diff_matrix = diff_matrix/60
	while i<60 :
		current_matrix = current_matrix + diff_matrix
		if dimension==2 :
			render_polygon(current_matrix.tolist())
		else :
			render_cube(current_matrix.tolist(),EDGES)
		i = i+1


def multiple_2d(n_iterations) :
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
def multiple_3d(n_iterations) :
	i=0
	while i<n_iterations :
		command = input()
		command = command.split(" ")
		if command[0] == "rotate" :
			animate_rotate_3d(command)
		elif command[0] == "translate" :
			animate_translate(float(command[1]),float(command[2]),float(command[3]))
		elif command[0] == "dilate" :
			animate_dilate(float(command[1]))
		elif command[0] == "reflect" :
			animate_reflect(command)
		elif command[0] == "custom" :
			animate_custom(command)
		elif command[0] == "stretch" :
			animate_stretch(command)
		i=i+1


def animate_rotate_3d(command) :
	global CURRENT_VERTICES
	global EDGES
	i=0
	output_matrix = np.matrix(CURRENT_VERTICES)
	while i<int(command[2]) :
		output_matrix = rotate3D(output_matrix,command[1],1)
		render_cube(output_matrix.tolist(),EDGES)
		i=i+1
	CURRENT_VERTICES = output_matrix.tolist()
	render_cube(CURRENT_VERTICES,EDGES)
	
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
	is_running_3d = True
	while is_running_3d:
		command = input("Masukkan perintah : ")
		command = command.split(" ")
		if command[0] == "rotate" :
			animate_rotate_3d(command)
		elif command[0] == "translate" :
			animate_translate(float(command[1]),float(command[2]),float(command[3]))
		elif command[0] == "dilate" :
			animate_dilate(float(command[1]))
		elif command[0] =="reset" :
			CURRENT_VERTICES = START_VERTICES
			render_cube(CURRENT_VERTICES,EDGES)
		elif command[0] == "reflect":
			animate_reflect(command)
		elif command[0] == "custom" :
			animate_custom(command)
		elif command[0] == "stretch" :
			animate_stretch(command)
		elif command[0] == "exit" :
			is_running_3d = False
		elif command[0] == "multiple" :
			multiple_3d(int(command[1]))
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
			animate_translate(float(command[1]),float(command[2]),0)
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
			multiple_2d(int(command[1]))
		elif(command[0]=='reset'):
			CURRENT_VERTICES = START_VERTICES
			render_polygon(CURRENT_VERTICES)
		elif command[0]=='exit' :
			is_running_2d = False
		else :
			print('Perintah salah. Masukkan perintah kembali :')
main()