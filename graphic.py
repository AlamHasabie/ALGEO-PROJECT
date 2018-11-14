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