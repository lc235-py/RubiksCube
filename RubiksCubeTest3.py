import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, -1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, 1],  ######
    [3.1, -1, -1],
    [3.1, 1, -1],
    [1.1, 1, -1],
    [1.1, -1, -1],
    [3.1, -1, 1],
    [3.1, 1, 1],
    [1.1, -1, 1],
    [1.1, 1, 1],  ######
    [5.2, -1, -1],
    [5.2, 1, -1],
    [3.2, 1, -1],
    [3.2, -1, -1],
    [5.2, -1, 1],
    [5.2, 1, 1],
    [3.2, -1, 1],
    [3.2, 1, 1]  ######
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
    [5, 7],  ####
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
    [16, 17],  ######
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
    [4, 5, 1, 0],  ##
    [9, 13, 15, 10],
    [12, 8, 11, 14],
    [8, 9, 10, 11],
    [11, 10, 15, 14],
    [14, 15, 13, 12],
    [12, 13, 9, 8],  ############# \/\/ VVV
    [17, 21, 23, 18],
    [20, 16, 19, 22],
    [16, 17, 18, 19],
    [19, 18, 23, 22],
    [22, 23, 21, 20],
    [20, 21, 17, 16]

]

colorsR = [
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

colorsY = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
]

colorsW = [
    (1, 0.5, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 0),
    (1, 1, 1)
]

colorsO = [
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (1, 0.5, 0)
]

def CubeR():
    for i2 in range(3):
        for i in range(3):
            glBegin(GL_QUADS)
            x = 0
            for surface in surfaces:
                x += 1

                for vertex in surface:
                    glColor3fv(colorsR[x])
                    glVertex3fv(vertices[vertex])

            glEnd()

            glBegin(GL_LINES)

            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
            glEnd()

            q = 0
            for j in range(24):
                vertices[q][1] = vertices[q][1] - 2.1
                q += 1

        q = 0
        for k in range(24):
            vertices[q][1] = vertices[q][1] + 6.3
            q += 1


        glBegin(GL_QUADS)
        x = 0
        for surface in surfaces:
            x += 1

            for vertex in surface:
                glColor3fv(colorsR[x])
                glVertex3fv(vertices[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        w = 0
        for k in range(24):
            vertices[w][2] = vertices[w][2] + 2.1
            w += 1

    w = 0
    for k in range(24):
        vertices[w][2] = vertices[w][2] - 6.3
        w += 1

def CubeY():
    for i2 in range(3):
        for i in range(3):
            glBegin(GL_QUADS)
            x = 0
            for surface in surfaces:
                x += 1

                for vertex in surface:
                    glColor3fv(colorsY[x])
                    glVertex3fv(vertices[vertex])

            glEnd()

            glBegin(GL_LINES)

            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
            glEnd()

            q = 0
            for j in range(24):
                vertices[q][1] = vertices[q][1] - 2.1
                q += 1

        q = 0
        for k in range(24):
            vertices[q][1] = vertices[q][1] + 6.3
            q += 1


        glBegin(GL_QUADS)
        x = 0
        for surface in surfaces:
            x += 1

            for vertex in surface:
                glColor3fv(colorsY[x])
                glVertex3fv(vertices[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        w = 0
        for k in range(24):
            vertices[w][2] = vertices[w][2] + 2.1
            w += 1

    w = 0
    for k in range(24):
        vertices[w][2] = vertices[w][2] - 6.3
        w += 1

def CubeW():
    for i2 in range(3):
        for i in range(3):
            glBegin(GL_QUADS)
            x = 0
            for surface in surfaces:
                x += 1

                for vertex in surface:
                    glColor3fv(colorsW[x])
                    glVertex3fv(vertices[vertex])

            glEnd()

            glBegin(GL_LINES)

            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
            glEnd()

            q = 0
            for j in range(24):
                vertices[q][1] = vertices[q][1] - 2.1
                q += 1

        q = 0
        for k in range(24):
            vertices[q][1] = vertices[q][1] + 6.3
            q += 1


        glBegin(GL_QUADS)
        x = 0
        for surface in surfaces:
            x += 1

            for vertex in surface:
                glColor3fv(colorsW[x])
                glVertex3fv(vertices[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        w = 0
        for k in range(24):
            vertices[w][2] = vertices[w][2] + 2.1
            w += 1

    w = 0
    for k in range(24):
        vertices[w][2] = vertices[w][2] - 6.3
        w += 1

def CubeO():
    for i2 in range(3):
        for i in range(3):
            glBegin(GL_QUADS)
            x = 0
            for surface in surfaces:
                x += 1

                for vertex in surface:
                    glColor3fv(colorsO[x])
                    glVertex3fv(vertices[vertex])

            glEnd()

            glBegin(GL_LINES)

            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
            glEnd()

            q = 0
            for j in range(24):
                vertices[q][1] = vertices[q][1] - 2.1
                q += 1

        q = 0
        for k in range(24):
            vertices[q][1] = vertices[q][1] + 6.3
            q += 1


        glBegin(GL_QUADS)
        x = 0
        for surface in surfaces:
            x += 1

            for vertex in surface:
                glColor3fv(colorsO[x])
                glVertex3fv(vertices[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

        w = 0
        for k in range(24):
            vertices[w][2] = vertices[w][2] + 2.1
            w += 1

    w = 0
    for k in range(24):
        vertices[w][2] = vertices[w][2] - 6.3
        w += 1






def main():
    side = "R"
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-2.1, 2.1, -20)
    glRotatef(0, 0, 0, 0)

    while True:
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

                if event.key == pygame.K_a:
                    if side == "R":
                        side = "Y"
                    elif side == "Y":
                        side = "O"
                    elif side == "O":
                        side = "W"
                    elif side == "W":
                        side = "R"
                if event.key == pygame.K_d:
                    if side == "R":
                        side = "W"
                    elif side == "W":
                        side = "O"
                    elif side == "O":
                        side = "Y"
                    elif side == "Y":
                        side = "R"


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        # glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if side == "R":
            CubeR()
        elif side == "Y":
            CubeY()
        elif side == "W":
            CubeW()
        elif side == "O":
            CubeO()

        pygame.display.flip()
        pygame.time.wait(10)


main()
