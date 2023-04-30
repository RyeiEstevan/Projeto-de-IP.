import pygame
from mapa import Mapa

class Personagem(pygame.sprite.Sprite):
    def __init__(self, tela, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.tela = tela
        self.vida = 3
        self.altura = 40
        self.largura = 40
        self.velocidade = 20
        self.image = pygame.image.load("sprites\Personagem.png")
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        botao = pygame.key.get_pressed()
        if botao[pygame.K_a]:
            self.rect.x -= self.velocidade

        if botao[pygame.K_d]:
            self.rect.x += self.velocidade

        if botao[pygame.K_w]:
            self.rect.y -= self.velocidade

        if botao[pygame.K_s]:
            self.rect.y += self.velocidade
        
        