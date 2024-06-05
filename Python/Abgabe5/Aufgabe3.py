import pygame # to use pygame keyboard and mouse control
from pygame.locals import * # to use constants from pygame directly
from OpenGL.GL import * # to use features from OpenGL
from MainWindow import MainWindow
from Objects2d import *

if __name__ == "__main__":
    objects = []
    objects.append(Square())
    objects.append(Square(1,1))
    game = MainWindow(windowHeight= 1080, windowWidth=1920, name="Window")
    game.mainloop(objectlist=objects)
