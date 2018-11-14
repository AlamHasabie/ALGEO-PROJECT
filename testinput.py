from formula_transformasi import *
from graphic import *





def main():
    start_vertex = input_vertices()
    current_vertices = start_vertex
    print(current_vertices)
    init_window()
    render_polygon(current_vertices)
    while True :
        i = 1
main()