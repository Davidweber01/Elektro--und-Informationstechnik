import pygame # to use pygame keyboard and mouse control
from pygame.locals import * # to use constants from pygame directly
from OpenGL.GL import * # to use features from OpenGL
from random import random

class MainWindow: # Class and constructor for main Window
    def __init__(self, windowHeight = 480, windowWidth = 640, name = "Main Window"):
        pygame.init() # invoke initial settings
        pygame.display.set_caption(name) # set window title
        self.time_interval = 1000
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, self.time_interval) 
        self.__windowSize = (windowWidth, windowHeight)# set size (default VGA)
        self.__videoFlags = OPENGL | DOUBLEBUF # use OpenGl and double Buffer
        # create window with given size and specified video options
        self.__window = pygame.display.set_mode(self.__windowSize, self.__videoFlags)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

    def OrthogonalProjection(self, xRange=(-10, 10), yRange=(-10, 10), zRange=(0, 1), frame=0):
        # set initial 2D-perspective for scene
        glMatrixMode(GL_PROJECTION) # switch to projection matrix to change settings
        glLoadIdentity() # reset all prior projection matrices (set all to identity)
        # set scene coordinates for orthogonal projection: left, right, bottom, top, near-, far-clipping
        glOrtho(xRange[0]-frame, xRange[1]+frame, yRange[1]+frame, yRange[0]-frame, zRange[0], zRange[1])
        glMatrixMode(GL_MODELVIEW) # switch back to model matrix to create model objects
        glLoadIdentity() 

    def mainloop(self, objectlist):
        # Schleife Hauptprogramm
        while True:
            # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
            for event in pygame.event.get():
                # Beenden bei [ESC] oder [X]
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                elif event.type == self.timer_event:
                    glClearColor(random(), random(), random(), random()) # define background color and alpha of window
            glClear(GL_COLOR_BUFFER_BIT)
            for obj in objectlist:
                obj.update()
            pygame.display.flip()
            pygame.time.wait(10)

    def close(self):
        pygame.quit() # quit pygame to close window
    