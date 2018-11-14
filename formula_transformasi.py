import math

import numpy as np

start_vertex = []

def dilate(current_vertex,k):
	current_vertex  = (i*k for i in current_vertex)
	return current_vertex

def translate(current_vertex,dx,dy):
	for a in current_vertex:
		a += (dx,dy)
	return current_vertex

def custom_translate(current_vertex,command):
	custom_matrix = []
	command = np.delete(command,0)
	for i in range(len(command)):
		custom_matrix = np.append(custom_matrix,float(command[i]))
	custom_matrix = np.resize(custom_matrix,(2,2))
	current_vertex = np.dot(current_vertex,custom_matrix)
	return current_vertex

def rotate(current_vertex,command):
	rotate_matrix = []
	command = np.delete(command,0)
	for i in range(len(command)):
		rotate_matrix = np.append(rotate_matrix,math.radians(float(command[i])))
	rotate_matrix = np.resize(rotate_matrix,(2,2))
	rotate_matrix[0][0] = math.cos(rotate_matrix[0][0])
	rotate_matrix[0][1] = -math.sin(rotate_matrix[0][1])
	rotate_matrix[1][0] = math.sin(rotate_matrix[1][0])
	rotate_matrix[1][1] = math.cos(rotate_matrix[1][1])
	current_vertex = np.dot(current_vertex,rotate_matrix)
	return current_vertex

def shear(current_vertex,command):
	factor = float(command[2])
	param = command[1]
	if(param == 'x'):
		current_vertex[:,0] += factor * current_vertex[:,1]
	else:
		current_vertex[:,1] += factor * current_vertex[:,0]
	return current_vertex

def stretch(current_vertex,command):
	factor = float(command[2])
	param = command[1]
	if(param == 'x'):
		current_vertex[:,0] *= factor
	else:
		current_vertex[:,1] *= factor
	return current_vertex

def reflect(current_vertex,param):
	if(param == 'x'):
		current_vertex[:,1] *= -1
	elif(param == 'y'):
		current_vertex[:,0] *= -1
	elif(param == 'y=x'):
		current_vertex[:,0],current_vertex[:,1] = current_vertex[:,1],current_vertex[:,0] 
	elif(param == 'y=-x'):
		current_vertex[:,0],current_vertex[:,1] = (-1*current_vertex[:,1]),(-1*current_vertex[:,0])


def action_command(current_vertex,command):
	if(command[0] == 'dilate'):
		current_vertex = dilate(current_vertex,float(command[1]))
	elif(command[0] == 'translate'):
		current_vertex = translate(current_vertex,float(command[1]),float(command[2]))
	elif(command[0] == 'custom'):
		current_vertex = custom_translate(current_vertex,command)
	elif(command[0] == 'rotate'):
		current_vertex = rotate(current_vertex,command)
	elif(command[0] == 'shear'):
		current_vertex = shear(current_vertex,command)
	elif(command[0] == 'stretch'):
		current_vertex = stretch(current_vertex,command)
	elif(command[0] == 'reflect'):
		current_vertex = reflect(current_vertex,command[1])

def get_command():
	command = input('Masukkan command :')
	parse_command = command.split(" ")
	if(parse_command[0] == 'multiple'):
		for i in range(int(parse_command[1])):
			while True:
				list_command = input()
				parse_list = list_command.split(" ")
				if((parse_list[0] == 'dilate') or (parse_list[0] == 'translate') or (parse_list[0] == 'custom') or (parse_list[0] == 'rotate') or (parse_list[0] == 'shear') or (parse_list[0] == 'stretch') or (parse_list[0] == 'reflect')):
					action_command(current_vertex,parse_list)
					break	
				else:
					print("Input salah, masukkan kembali : ")
	else:
		action_command(current_vertex,parse_command)

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
