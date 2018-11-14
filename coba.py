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
			shear_matrix[0][0] = 1
			shear_matrix[0][1] = k
			shear_matrix[1][0] = 0
			shear_matrix[1][1] = 1
	current_vertex = np.dot(current_vertex,shear_matrix)
	return current_vertex

def input_vertices():
	start_vertex = []

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
	return start_vertex