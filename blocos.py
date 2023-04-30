import pygame
from constantes import *

class Blocos_indestrutiveis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #Definindo tamanho dos blocos, sua cor e onde serão salvos
        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load("sprites\Blocos_indestrutiveis.png")
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

     
        
