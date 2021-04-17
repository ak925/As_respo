{
	"cmd":["python3","-u","$file"]
}
import pygame
from pygame.sprite import Sprite

#retest


 


class Alien(Sprite):
	"""Adding a single alien on the screen and keeping """
	def __inti__(self,ai_game):
		"""Initialize the alien and set its starting position."""
		super().__intit__()
		self.screen=ai_game.screen
