import numpy as np

def dilate(current_vertex,k):
	print(311)
	current_vertex *= k
	return current_vertex

def translate(current_vertex,dx,dy,dz):
	for a in current_vertex:
		a += (dx,dy,dz)
	return current_vertex

def shear(current_vertex,axis,k):
	## Inisialisation Zero Matrix
	s = (3,3)
	shear_matrix = np.zeros(s)
	if(dimensi == 2):
		if(axis == 'x'):
			shear_matrix[0][0] = 1
			shear_matrix[0][1] = 0
			shear_matrix[1][0] = k
			shear_matrix[1][1] = 1
		else 
			
	current_vertex = np.dot(current_vertex,shear_matrix)
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
			current_vertex = shear(current_vertex,command[1],float(command[2]))
			print(current_vertex)
	return current_vertex

#Membaca masukan
def get_command():
	command = input()
	parse_command = command.split(" ")
	# if(parse_command[0] == 'multiple'):
	# 	for i in range(int(parse_command[1])):
	# 		while True:
	# 			list_command = raw_input()
	# 			parse_list = list_command.split(" ")
	# 			if((parse_list[0] == 'dilate') or (parse_list[0] == 'translate') or (parse_list[0] == 'custom') or (parse_list[0] == 'rotate') or (parse_list[0] == 'shear') or (parse_list[0] == 'stretch') or (parse_list[0] == 'reflect')):
	# 				# action_command(current_vertex,parse_list)
	# 				break	
	# 			else:
	# 				print "Input salah, masukkan kembali : "
	# else:
	current_vertex = np.matrix(start_vertex[0])
	print(current_vertex)
	current_vertex = action_command(current_vertex,parse_command)
	print(current_vertex)

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
get_command()