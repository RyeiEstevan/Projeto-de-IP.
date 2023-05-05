import pygame
from constantes import *
from pygame.sprite import Sprite
from sprites import sprites

materiais = {
    "vida" : "sprites\Vida.png",
    "tempo" : 'sprites\Tempo.png',
    "velocidade" : "sprites\Velocidade.png",
    "portal" : "sprites\Portal.png"
}

class Item(Sprite):

    itens = []

    def __init__(self, tela, x, y, tipo: str):
        
        Sprite.__init__(self)
        self.image = pygame.image.load(materiais[tipo])
        self.image = pygame.transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.tela = tela
        self.tipo = tipo
        self.rect.x = celulas[x][y][X]
        self.rect.y = celulas[x][y][Y]
        sprites.add(self)
        Item.itens.append(self)

    def kill(self):
       Item.itens.remove(self)
       sprites.remove(self)
        
