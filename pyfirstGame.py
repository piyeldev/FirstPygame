import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()
sky_surface = pygame.image.load('PygameBackground.png')
ground_surface = pygame.image.load('Ground.png')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	# draw all elements here ;)
	# update everything :0
	sky = screen.blit(sky_surface, (-45, 0))
	ground =  screen.blit(ground_surface, (0, 400))
	
	pygame.display.update()
	clock.tick(60)