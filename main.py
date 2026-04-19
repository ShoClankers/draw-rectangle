import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.evemt.get():
        if event.type == pygmame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 255), pygmame.Rect(30, 30, 60, 60))

    pygame.display.flip()