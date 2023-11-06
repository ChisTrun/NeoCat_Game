import pygame,sys
from pygame.locals import*

pygame.init()
manhinh = pygame.display.set_mode((800,600))
icon = pygame.image.load('source/cat/nyan-cat-icegif-15-0_preview_rev_1.png').convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("Cat_Rainbow")
game_run = True