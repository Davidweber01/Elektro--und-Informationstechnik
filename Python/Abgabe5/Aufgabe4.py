import pygame # to use pygame keyboard and mouse control
from pygame.locals import * # to use constants from pygame directly
from OpenGL.GL import * # to use features from OpenGL
from MainWindow import MainWindow
from Objects2d import *

if __name__ == "__main__":
    game = MainWindow(windowHeight= 1080, windowWidth=1920, name="Window")
    # Calculate aspect ratio
    aspect_ratio = game.windowWidth / game.windowHeight
    
    # Choose ranges based on the larger dimension
    if aspect_ratio >= 1:  # Width is larger
        xRange = (-10 * aspect_ratio, 10 * aspect_ratio)
        yRange = (-10, 10)
    else:  # Height is larger
        xRange = (-10, 10)
        yRange = (-10 / aspect_ratio, 10 / aspect_ratio)
    
    game.OrthogonalProjection(xRange=xRange, yRange=yRange, zRange=(0, 1), frame=0)
    
    # Create a grid of squares to fill the screen
    objects = []
    x_min, x_max = xRange
    y_min, y_max = yRange
    for x in range(int(x_min), int(x_max)):
        for y in range(int(y_min), int(y_max)):
            objects.append(Square(x, y, size=1))

    game.mainloop(objectlist=objects)
