import pygame
from mapa import Mapa
class personagem:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.x = x
        self.y = y
        self.vida = 3
        self.altura = 40
        self.largura = 40
        self.velocidade = 20
        self.cor = 'BLUE'

    def movimentacao(self,botao):
        if botao[pygame.K_a]:
            self.x -= self.velocidade

        if botao[pygame.K_d]:
            self.x += self.velocidade

        if botao[pygame.K_w]:
            self.y -= self.velocidade

        if botao[pygame.K_s]:
            self.y += self.velocidade


    def desenhar_personagem(self):
        pygame.draw.rect(self.tela, self.cor, (self.x, self.y, self.largura, self.altura))