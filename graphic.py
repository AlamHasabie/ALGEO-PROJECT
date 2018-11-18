import pygame
import numpy as np
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def init_window():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 4000.0)
    glTranslatef(0.0,0.0, -1500)

def init_window_3d():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 4000.0)
    glTranslatef(0.0,0.0, -1500)
    glRotatef(20,1,1,0)

def render_polygon(CURRENT_VERTICES):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.5)
    for vertex in CURRENT_VERTICES :
        glVertex3f(vertex[0],vertex[1],vertex[2])
    glEnd()
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(-900,0,0)
    glVertex3f(900,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,-900,0)
    glVertex3f(0,900,0)
    glEnd()
    pygame.display.flip()

def render_cube(CURRENT_VERTICES,EDGES,randomColor):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    i = 0
    for edge in EDGES :
        glBegin(GL_POLYGON)
        glColor3f(randomColor[i][0],randomColor[i][1],randomColor[i][2])
        for vertex in edge :
            glVertex3f(CURRENT_VERTICES[vertex][0],CURRENT_VERTICES[vertex][1],CURRENT_VERTICES[vertex][2])
        glEnd()
        i = i + 1
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(-900,0,0)
    glVertex3f(900,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,-900,0)
    glVertex3f(0,900,0)
    glColor3f(0,0,1)
    glVertex3f(0,0,1800)
    glVertex3f(0,0,-1800)
    glEnd()
    pygame.display.flip()