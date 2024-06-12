import pygame # to use pygame keyboard and mouse control
from pygame.locals import * # to use constants from pygame directly
from OpenGL.GL import * # to use features from OpenGL
from Universum import Universum

WIDTH = 1920
HEIGHT = 1080
SCALE = 20

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Game Of Life")

    time_interval = 100
    timer_event = pygame.USEREVENT + 1

    pygame.time.set_timer(timer_event, time_interval)
    pygame.display.set_mode((WIDTH, HEIGHT), OPENGL | DOUBLEBUF)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH // SCALE, 0, HEIGHT // SCALE, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    pause = False
    universum = Universum(WIDTH // SCALE, HEIGHT // SCALE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0] // SCALE
                y = - pos[1] // SCALE
                universum.grid[x][y].switch_alive()
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if pause == True:
                    pause = False
                else:
                    pause = True
            elif event.type == timer_event:
                if pause == False:
                    universum.berechne_folgezustand()
        glClear(GL_COLOR_BUFFER_BIT)
        universum.darstellung()
        pygame.display.flip()
        pygame.time.wait(10)