import pygame


pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (20, 28, 140)

y = 0
speed = int(height*0.05)
title = None
