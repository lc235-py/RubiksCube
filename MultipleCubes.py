import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -10)
glRotatef(0, 0, 0, 0)

y1 = 1
y2 = 3

for i in range(3):

    y1 -= 2
    y2 -= 2

    vertices = [
        [1, y1, -1],
        [1, y2, -1],
        [-1, y2, -1],
        [-1, y1, -1],
        [1, y1, 1],
        [1, y2, 1],
        [-1, y1, 1],
        [-1, y2, 1], ######
        [3.1, y1, -1],
        [3.1, y2, -1],
        [1.1, y2, -1],
        [1.1, y1, -1],
        [3.1, y1, 1],
        [3.1, y2, 1],
        [1.1, y1, 1],
        [1.1, y2, 1], ######
        [5.2, y1, -1],
        [5.2, y2, -1],
        [3.2, y2, -1],
        [3.2, y1, -1],
        [5.2, y1, 1],
        [5.2, y2, 1],
        [3.2, y1, 1],
        [3.2, y2, 1] ######
    ]

    edges = [
        [0, 1],
        [0, 3],
        [0, 4],
        [2, 1],
        [2, 3],
        [2, 7],
        [6, 3],
        [6, 4],
        [6, 7],
        [5, 1],
        [5, 4],
        [5, 7], ####
        [8, 9],
        [8, 1],
        [8, 1],
        [10, 9],
        [10, 11],
        [10, 15],
        [14, 11],
        [14, 12],
        [14, 15],
        [13, 9],
        [13, 12],
        [13, 15],
        [16, 17], ######
        [16, 19],
        [16, 20],
        [18, 17],
        [18, 19],
        [18, 23],
        [22, 19],
        [22, 20],
        [22, 23],
        [21, 17],
        [21, 20],
        [21, 23]
    ]

    surfaces = [
        [1, 5, 7, 2],
        [4, 0, 3, 6],
        [0, 1, 2, 3],
        [3, 2, 7, 6],
        [6, 7, 5, 4],
        [4, 5, 1, 0], ##
        [9, 13, 15, 10],
        [12, 8, 11, 14],
        [8, 9, 10, 11],
        [11, 10, 15, 14],
        [14, 15, 13, 12],
        [12, 13, 9, 8], ############# \/\/ VVV
        [17, 21, 23, 18],
        [20, 16, 19, 22],
        [16, 17, 18, 19],
        [19, 18, 23, 22],
        [22, 23, 21, 20],
        [20, 21, 17, 16]

    ]

    colors = [
        (1, 1, 1),  # white
        (0, 1, 0),  # green
        (0, 0, 1),  # blue
        (1, 0.5, 0),  # orange
        (1, 1, 0),  # yellow
        (1, 0, 0),  # red
        (1, 1, 1),
        (0, 1, 0),
        (0, 0, 1),
        (1, 0.5, 0),
        (1, 1, 0),
        (1, 0, 0),
        (1, 1, 1),  # white
        (0, 1, 0),  # green
        (0, 0, 1),  # blue
        (1, 0.5, 0),  # orange
        (1, 1, 0),  # yellow
        (1, 0, 0),  # red
        (1, 1, 1),
        (0, 1, 0),
        (0, 0, 1),
        (1, 0.5, 0),
        (1, 1, 0),
        (1, 0, 0)

    ]


    def Cube():
        glBegin(GL_QUADS)
        x = 0
        for surface in surfaces:
            x += 1

            for vertex in surface:
                glColor3fv(colors[x])
                glVertex3fv(vertices[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    Cube()
    pygame.display.flip()
while True:
            pygame.time.wait(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        glTranslatef(0.5, 0, 0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(-0.5, 0, 0)

                    if event.key == pygame.K_UP:
                        glTranslatef(0, -0.5, 0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0, 0.5, 0)



                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0, 0, 1.0)
                    if event.button == 5:
                        glTranslatef(0, 0, -1.0)


            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            Cube()

            pygame.display.flip()
            pygame.time.wait(10)


