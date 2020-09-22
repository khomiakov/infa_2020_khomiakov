import pygame
import pygame.draw as d

pygame.init()
screen = pygame.display.set_mode((400, 400))
d.rect(screen, (100, 0, 100), (100, 100, 100, 200))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
clock = pygame.time.Clock()
clock.tick(30)
