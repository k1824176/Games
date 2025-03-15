import pygame
from OpenGL.GL import *
import numpy
import ctypes

class App:

    def __init__(self):

        #pygame initialization
        pygame.init()
        pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()

        #OpenGL initialization
        glClearColor(0.1, 0.2, 0.2, 1.0)
        self.mainloop()

    def mainloop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            glClear(GL_COLOR_BUFFER_BIT)
            pygame.display.flip()

            self.clock.tick(60)
        self.quit()

    def quit(self):
        pygame.quit()

class Triangle:

    def __init__(self):

        #x, y, z, r, g, b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        )

        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)

        self.vertex_count = 3
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

if __name__ == "__main__":
    App()