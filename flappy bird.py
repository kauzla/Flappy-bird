import sys, pygame
pygame.init()

size = [900, 504]
screen = pygame.display.set_mode(size)
background = pygame.image.load('pozadina.png')
player = pygame.image.load('ptica.jpg')
pipe = pygame.image.load('cijev.png')
p_y = int((900 - player.get_height()) / 2)
p_x = 250

running = True
while running:
    pygame.display.flip()
    screen.blit(background, (0, 0))
    screen.blit(player, (p_x, p_y))
    
