import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLU import *


def main():
    verticies = []
    edges = []
    s =  input("number of vertices :")
    i = int(s)
    j = 0
    while j<i :
        X = float(input())
        Y = float(input())
        verticies.append((X,Y,0))
        if j<(i-1):
            edges.append((j,j+1))
        j=j+1
    edges.append((j-1,0))
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 4000.0)
    glTranslatef(0.0,0.0, -2000)
    i=0
    while True:
        s = input("Perintah : ")
        if s=="Translate" :
            i=0
            while i<90 : 
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                verticies = translate(verticies,1,1,1)
                glBegin(GL_LINES)
                for edge in edges:
                    for vertex in edge:
                        glVertex3fv(verticies[vertex])
                glVertex3f(-900,0,0)
                glVertex3f(900,0,0)
                glVertex3f(0,-900,0)
                glVertex3f(0,900,0)
                glEnd()
                pygame.display.flip()
                pygame.time.wait(10)
                i=i+1
        else :
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(verticies[vertex])
            glVertex3f(-900,0,0)
            glVertex3f(900,0,0)
            glVertex3f(0,-900,0)
            glVertex3f(0,900,0)
            glEnd()
            pygame.display.flip()
            pygame.time.wait(10)
def translate(CURRENT_VERTICES,dx,dy,dz):
    output_vertice = []
    for vertice in CURRENT_VERTICES :
        x = dx + vertice[0]
        y = dy + vertice[1]
        output_vertice.append((x,y,0))
    return output_vertice

main()