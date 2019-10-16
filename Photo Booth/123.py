import pygame

def main():
	running = True
	while running:
		# event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
		
		
def destroy():
	print("cleanup")
	pygame.quit()


if __name__ == '__main__' : # Program start
	pygame.init()
	pygame.display.set_caption("1-2-3")
	screen = pygame.display.set_mode((400,400))
	try:
		main()
	except KeyboardInterrupt: # when ctrl+c is pressed
		destroy()
	
