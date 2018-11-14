import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def init_window():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 4000.0)
    glTranslatef(0.0,0.0, -2000)

def render_polygon(current_vertices):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(3.0,4.0,5.0)
    for vertex in current_vertices :
        glVertex3f(vertex[0],vertex[1],vertex[2])
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-900,0,0)
    glVertex3f(900,0,0)
    glVertex3f(0,-900,0)
    glVertex3f(0,900,0)
    glEnd()
    pygame.display.flip()
    pygame.time.wait(10)