from formula_transformasi import *
from graphic import *





def main():
    start_vertex = input_vertices()
    CURRENT_VERTICES = start_vertex
    print(CURRENT_VERTICES)
    init_window()
    render_polygon(CURRENT_VERTICES)
    while True :
        i = 1
main()