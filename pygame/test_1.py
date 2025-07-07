#功能：测试pygame
#说明: Python版本 3.13.5

# Pygame template - skeleton for a new pygame project
import time
import pygame
import random

WIDTH = 720
HEIGHT = 960
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,60)
textImage = myfont.render("pygame", True, WHITE)

# Game loop
running = True
count = 0
start = time.time()

while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    count+=1
    now = time.time()
    fps = count/(now-start)
    fpsImage = myfont.render(str(fps), True, WHITE)
    # Draw / render
    screen.fill(RED)
    screen.blit(fpsImage, (0, 100))
    screen.blit(textImage, (0, 300))
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()