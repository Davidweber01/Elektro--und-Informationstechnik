import pygame # to use pygame keyboard and mouse control
from pygame.locals import * # to use constants from pygame directly
from OpenGL.GL import * # to use features from OpenGL
from MainWindow import MainWindow
from Objects2d import *
from math import ceil

if __name__ == "__main__":
    game = MainWindow(windowHeight= 1080, windowWidth=1920, name="Window")
    # Calculate aspect ratio
    aspect_ratio = game.windowWidth / game.windowHeight
    
    # Set orthogonal projection ranges to match window dimensions
    xRange = (0, game.windowWidth // 10)
    yRange = (0, game.windowHeight // 10)
    
    game.OrthogonalProjection(xRange=xRange, yRange=yRange, zRange=(0, 1), frame=0)
    
    # Create a grid of squares to fill the screen
    objects = []
    for x in range(0, int(game.windowWidth/10)):
        for y in range(0, int(game.windowHeight/10)):
            objects.append(Square(x, y, size=10))
    
    game.mainloop(objectlist=objects)
