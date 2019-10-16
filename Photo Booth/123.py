import pygame

def main():
	running = True
	while running:
		# event handling, gets all event from the queue
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
			# if spacebar is pressed
			elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
				# img = pygame.image.load('123.png') 
				# screen.blit(img, (0,0))
				# pygame.display.update()
				load_img('123')
			elif event.type == pygame.KEYUP and event.key == pygame.K_1:
				load_img('1')
			elif event.type == pygame.KEYUP and event.key == pygame.K_2:
				load_img('2')
			elif event.type == pygame.KEYUP and event.key == pygame.K_3:
				load_img('3')

# method to load image based on key
def load_img(n):
	img = pygame.image.load('{0}.png'.format(n))
	screen.blit(img, (0, 0))
	pygame.display.update()		
		
# method to quit
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
	
