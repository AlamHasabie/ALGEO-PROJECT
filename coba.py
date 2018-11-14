import numpy as np
import math 

def dilate(current_vertex,k):
	current_vertex *= k
	return current_vertex

def translate(current_vertex,dx,dy,dz):
	for a in current_vertex:
		a += (dx,dy,dz)
	return current_vertex

def shear(current_vertex,axis,k1,k2):
	## Inisialisation Zero Matrix
	s = (3,3)
	shear_matrix = np.zeros(s)
	shear_matrix[0][0] = 1
	shear_matrix[1][1] = 1
	shear_matrix[2][2] = 1
	if(axis == 'x'):
		shear_matrix[1][0] = k1
		shear_matrix[2][0] = k2
	elif(axis == 'y'):
		shear_matrix[0][1] = k1
		shear_matrix[2][1] = k2
	elif(axis == 'z'):
		shear_matrix[0][2] = k1
		shear_matrix[1][2] = k2
	current_vertex = np.dot(current_vertex,shear_matrix)
	return current_vertex

def stretch(current_vertex,axis,k):
	s = (3,3)
	stretch_matrix = np.zeros(s)
	stretch_matrix[0][0] = 1
	stretch_matrix[1][1] = 1
	stretch_matrix[2][2] = 1
	if(axis == 'x'):
		stretch_matrix[0][0] = k
	elif(axis == 'y'):
		stretch_matrix[1][1] = k
	elif(axis == 'z'):
		stretch_matrix[2][2] = k
	current_vertex = np.dot(current_vertex,stretch_matrix)
	return current_vertex

def reflect(current_vertex,parameter):
	s = (3,3)
	reflect_matrix = np.zeros(s)
	if(dimensi == 2):
		if(parameter == 'x'):
			reflect_matrix[0][0] = 1
			reflect_matrix[1][1] = -1
			current_vertex = np.dot(current_vertex,reflect_matrix)
		elif(parameter == 'y'):
			reflect_matrix[0][0] = -1
			reflect_matrix[1][1] = 1
			current_vertex = np.dot(current_vertex,reflect_matrix)
		elif(parameter == 'y=x'):
			reflect_matrix[0][1] = 1
			reflect_matrix[1][0] = 1
			current_vertex = np.dot(current_vertex,reflect_matrix)
		elif(parameter == 'y=-x'):
			reflect_matrix[0][1] = -1
			reflect_matrix[1][0] = -1
			current_vertex = np.dot(current_vertex,reflect_matrix)
		else:
			parameter = parameter[1:len(parameter)-1]
			parameter = parameter.split(",")
			current_vertex = rotate2D(current_vertex,180,float(parameter[0]),float(parameter[1]))
	else:
		reflect_matrix[0][0] = 1
		reflect_matrix[1][1] = 1
		reflect_matrix[2][2] = 1
		if(parameter == 'x-y'):
			reflect_matrix[2][2] = -1
		elif(parameter == 'y-z'):
			reflect_matrix[0][0] = -1
		elif(parameter == 'x-z'):
			reflect_matrix[1][1] = -1
		current_vertex = np.dot(current_vertex,reflect_matrix)

	return current_vertex	

def rotate2D(current_vertex,angle,x,y):
	s = (3,3)
	rotate_matrix = np.zeros(s)
	if(dimensi == 2):
		rotate_matrix[0][0] = math.cos(math.radians(angle))
		rotate_matrix[0][1] = math.sin(math.radians(angle))
		rotate_matrix[1][0] = -math.sin(math.radians(angle))
		rotate_matrix[1][1] = math.cos(math.radians(angle))
	current_vertex = translate(current_vertex,-x,-y,0)
	current_vertex = np.dot(current_vertex,rotate_matrix)
	current_vertex = translate(current_vertex,x,y,0)
	return current_vertex

def rotate3D(current_vertex,axis,angle):
	s = (3,3)
	rotate_matrix = np.zeros(s)
	rotate_matrix[0][0] = 1
	rotate_matrix[1][1] = 1
	rotate_matrix[2][2] = 1
	if(axis == 'z'):
		rotate_matrix[0][0] = math.cos(math.radians(angle))
		rotate_matrix[0][1] = math.sin(math.radians(angle))
		rotate_matrix[1][0] = -math.sin(math.radians(angle))
		rotate_matrix[1][1] = math.cos(math.radians(angle))
	elif(axis == 'y'):
		rotate_matrix[0][0] = math.cos(math.radians(angle))
		rotate_matrix[0][2] = -math.sin(math.radians(angle))
		rotate_matrix[2][0] = math.sin(math.radians(angle))
		rotate_matrix[2][2] = math.cos(math.radians(angle))
	elif(axis == 'x'):
		rotate_matrix[1][0] = math.cos(math.radians(angle))
		rotate_matrix[1][2] = math.sin(math.radians(angle))
		rotate_matrix[2][1] = -math.sin(math.radians(angle))
		rotate_matrix[2][2] = math.cos(math.radians(angle))
	current_vertex = np.dot(current_vertex,rotate_matrix)
	return current_vertex

def custom(current_vertex,command):
	s = (3,3)
	custom_matrix = np.zeros(s)
	if(dimensi == 2):
		custom_matrix[0][0] = command[1]
		custom_matrix[0][1] = command[2]
		custom_matrix[1][0] = command[3]
		custom_matrix[1][1] = command[4]
	else:
		idx = 1
		for i in custom_matrix:
			i = command[idx]
			idx = idx + 1
	current_vertex = np.dot(current_vertex,custom_matrix)
	return current_vertex

def action_command(current_vertex,command):
	if(command[0] == 'dilate'):
		current_vertex = dilate(current_vertex,float(command[1]))
	elif(command[0] == 'translate'):
		if(dimensi == 2):
			current_vertex = translate(current_vertex,float(command[1]),float(command[2]),float(0))
		else:
			current_vertex = translate(current_vertex,float(command[1]),float(command[2]),float(command[3]))
	elif(command[0] == 'shear'):
		if(dimensi == 2):
			current_vertex = shear(current_vertex,command[1],float(command[2]),0)
		else:
			current_vertex = shear(current_vertex,command[1],float(command[2]),float(command[3]))
	elif(command[0] == 'stretch'):
		current_vertex = stretch(current_vertex,command[1],float(command[2]))
	elif(command[0] == 'reflect'):
		current_vertex = reflect(current_vertex,command[1])
	elif(command[0] == 'rotate'):
		if(dimensi == 2):
			current_vertex = rotate2D(current_vertex,float(command[1]),float(command[2]),float(command[3]))
		else:
			current_vertex = rotate3D(current_vertex,command[1],float(command[2]))
	elif(command[0] == 'custom'):
		current_vertex = custom(current_vertex,command)
	return current_vertex

#Membaca masukan
def get_command():
	command = input()
	parse_command = command.split(" ")
	if(parse_command[0] == 'multiple'):
		current_vertex = np.matrix(start_vertex[0])
		for i in range(int(parse_command[1])):
			while True:
				list_command = input()
				parse_list = list_command.split(" ")
				if((parse_list[0] == 'dilate') or (parse_list[0] == 'translate') or (parse_list[0] == 'custom') or (parse_list[0] == 'rotate') or (parse_list[0] == 'shear') or (parse_list[0] == 'stretch') or (parse_list[0] == 'reflect')):
					current_vertex = action_command(current_vertex,parse_list)
					break	
				else:
					print ("Input salah, masukkan kembali : ")
	else:
		current_vertex = np.matrix(start_vertex[0])
		print(current_vertex)
		current_vertex = action_command(current_vertex,parse_command)
	return current_vertex.tolist()

def input_vertices():
	start_vertex = []
	edge_list = []
	vertices_edges = []
	print ("Masukkan Banyaknya Sisi : ")
	n_vertices = input()
	for x in range(int(n_vertices)):
		get_Avertex = input()
		tmp = list(get_Avertex.split(","))
		while len(tmp)!=2 : 
			print("Input salah , masukkan kembali :")
			get_Avertex = input()
			tmp = list(get_Avertex.split(","))
		for n in range(len(tmp)) :
			tmp[n] = float(tmp[n])
		tmp.append(0)
		start_vertex.append(tmp)
		#Added edge_list for 
		if x<int(n_vertices)-1 :
			edge_list.append([x,x+1])
		else :
			edge_list.append([x,0])
	vertices_edges.append(start_vertex)
	vertices_edges.append(edge_list)
	return vertices_edges

dimensi = 2
start_vertex = input_vertices()
print(get_command())