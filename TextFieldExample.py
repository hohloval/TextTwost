import os, sys
import pygame
from pygame.locals import *
from TextField import *


if __name__ == '__main__':
    pygame.init()

    size = width, height = 320, 240
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TextField example")
    field = TextField(width//2, height//2, 65, screen)
    field.set_font_color((250, 250, 250))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                print(chr(event.key))

            field.check_change(event)

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                field.clear_field()

        screen.fill(black)
        field.draw()
        pygame.display.flip()

