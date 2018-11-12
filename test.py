import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()

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
main()