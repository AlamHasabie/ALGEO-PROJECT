import formula_transformasi as ft
import graphic
import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *


global start_vertex
global current_vertex

def main():
    graphic.init()
    start_vertex = ft.input_vertices()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    graphic.render(start_vertex)
    pygame.display.flip()
    while True :
        ft.get_command()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        graphic.render(current_vertex)
        pygame.display.flip()
        pygame.time.wait(5)
main()