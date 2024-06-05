import pygame # to use pygame keyboard and mouse control
from pygame.locals import * # to use constants from pygame directly
from OpenGL.GL import * # to use features from OpenGL
from MainWindow import MainWindow

if __name__ == "__main__":
    game = MainWindow(windowHeight= 1080, windowWidth=1920, name="Window")
    game.mainloop()
