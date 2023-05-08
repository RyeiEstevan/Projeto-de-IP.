import pygame
from constantes import *
from sprites import sprite
from pygame.sprite import Sprite

#classe dos blocos indestrutíveis
class Blocos_indestrutiveis(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        #Definindo tamanho dos blocos, seus sprites e onde serão salvos
        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load(sprite["bloco_indestrutivel"])
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

#classe dos blocos destrutíveis
class Blocos_destrutiveis(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        #definindo todas as propriedades dos blocos
        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load(sprite["bloco_destrutivel"])
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y