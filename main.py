from formula_transformasi import *
from graphic import *

global start_vertex
global current_vertex

def main():
    start_vertex = input_vertices()
    current_vertices = start_vertex
    print(current_vertices)
    init_window()
    render_polygon(current_vertices)
    while True :
        get_command()
    #start_vertex = ft.input_vertices()
    #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #graphic.render(start_vertex)
    #pygame.display.flip()
    #while True :
    #    ft.get_command()
    #    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #    graphic.render(current_vertex)
    #    pygame.display.flip()
    #    pygame.time.wait(5)
main()