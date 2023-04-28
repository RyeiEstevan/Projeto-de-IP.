import pygame
from constantes import *

materiais = {
    "bomba" : (50, 50, 50),
    "vida" : (200, 0, 0),
    "tempo" : (200, 200, 200),
    "velocidade" : (50, 50, 200)
}

class Item:

    def __init__(self, tela, x, y, tipo: str):
        
        self.tamanho_blocos = TAMANHO_CELULA
        self.tela = tela
        self.tipo = tipo
        self.cor = materiais[tipo]
        self.x = x
        self.y = y
        x, y = celulas[self.x][self.y]
        self.rect = pygame.rect.Rect((x, y),(TAMANHO_CELULA, TAMANHO_CELULA))

    def desenhar(self):
        pygame.draw.rect(self.tela, self.cor, self.rect)
        
