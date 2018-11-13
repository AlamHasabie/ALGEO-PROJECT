import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

verticies = (
    (1,1),
    (1,-1),
    (-1,-1),
    (-1,1)
    )

edges = (
    (0,1),
    (0,3),
    (1,2),
    (2,3)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(verticies[vertex])
    glEnd()


def main():
    while True:
        user_input = input(":")
        if user_input == "rotate-90-cc" :
            i = 0
            while i<90:
                glRotatef(1, 0, 0, 1)
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                Cube()
                pygame.display.flip()
                i=i+1
                pygame.time.wait(5)
        elif user_input =="rotate-90-c" :
            i = 0
            while i<90 :
                glRotatef(-1, 0, 0, 1)
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                Cube()
                pygame.display.flip()
                i=i+1
                pygame.time.wait(5)

def init():
    pygame.init()
    display = (1200,1200)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

def render(current_vertex):
    glBegin(GL_LINES)
    i = 0
    while i < (current_vertex.size-1) :
        glVertex2fv(current_vertex[i])
        glVertex2fv(current_vertex[i+1])
        i = i+1
    glVertex2fv(current_vertex[i])
    glVertex2fv(current_vertex[0])
    glEnd()

