import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import keyboard

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (0, 0, 1),  # blue
    (1, 0.5, 0),  # orange
    (1, 1, 0),  # yellow
    (1, 0, 0),  # red
    (1, 1, 1),  # white
    (0, 1, 0),  # green
    (0, 0, 1),
    (1, 0.5, 0),
    (1, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 0)
)


def Cube():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x += 1

        for vertex in surface:
            glColor3dv(colors[x])
            glVertex3fv(vertices[vertex])

    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keyboard.is_pressed("up_arrow"):
            glRotatef(1, 1, 0, 0)
        if keyboard.is_pressed("down_arrow"):
            glRotatef(1, -1, 0, 0)
        if keyboard.is_pressed("left_arrow"):
            glRotatef(1, 0, 1, 0)
        if keyboard.is_pressed("right_arrow"):
            glRotatef(1, 0, -1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
