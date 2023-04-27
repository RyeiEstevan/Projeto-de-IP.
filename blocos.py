import pygame
from constantes import *

class Blocos_indestrutiveis:
    def __init__(self, tela):

        #Definindo tamanho dos blocos, sua cor e onde serão salvos
        self.tamanho_blocos = TAMANHO_CELULA
        self.tela = tela
        self.cor_blocos = (255, 255, 212)
        self.blocos_indestrutiveis = []

    def desenhar_blocos(self):
        for i in range (MAPA_ALTURA):
            for a in range (MAPA_LARGURA):
                x = celulas[i][a][X] ; y = celulas[i][a][Y]
                if i%2 != 0 and a%2 != 0:
                    bloco = pygame.draw.rect(self.tela, self.cor_blocos, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
                    self.blocos_indestrutiveis.append(bloco)
        
