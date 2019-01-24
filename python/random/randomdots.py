import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pygame.display.set_caption("Random Dots!")

colors = [0]*100
locations = [0]*100
sizes = [0]*100
BLACK = (0,0,0)

for n in range(100):
    colors[n] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    locations[n] = (random.randint(0,800), random.randint(0,600))
    sizes[n] = random.randint(10, 100)
    pygame.draw.circle(screen, colors[n], locations[n],sizes[n])
    pygame.display.update()
screen.fill(BLACK)
