from pygame import transform, image
import pygame
from pygame.sprite import Sprite
import random
from sprites import sprites
from constantes import *
from mapa import blocos_destrutiveis

class Inimigo(Sprite):

    sprite = {
        "polemonio" : "sprites\Polemonio.png"
    }

    def __init__(self, tela, x, y, tipo, blocos_destrutiveis):
        super().__init__()

        self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
        self.colide = False
        self.velocidade = 2
        self.image = transform.scale(image.load(Inimigo.sprite[tipo]), (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        sprites.add(self)

    def update(self):

        if self.direcao == "esquerda":
            self.rect.x -= self.velocidade

        elif self.direcao == "direita":
            self.rect.x += self.velocidade

        elif self.direcao == "baixo":
            self.rect.y += self.velocidade

        elif self.direcao == "cima":
            self.rect.y -= self.velocidade  
        
        self.colisao()
    
    def colisao(self):

        #checar colisão bordas
        if self.rect.x > (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA:
            self.rect.x = (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA
            self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
            

        elif self.rect.x < TAMANHO_BORDAS:
            self.rect.x = TAMANHO_BORDAS
            self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
            

        if self.rect.y > (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA:
            self.rect.y = (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA
            self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
            

        elif self.rect.y < TAMANHO_MENU+TAMANHO_BORDAS:
           self.rect.y = TAMANHO_MENU+TAMANHO_BORDAS
           self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
        
        #checar colisão com blocos indestrutíveis
        for i in range (len(blocos_indestrutiveis)):
            rect = pygame.rect.Rect(blocos_indestrutiveis[i], (TAMANHO_CELULA, TAMANHO_CELULA))
            if self.rect.colliderect(rect):
                if self.direcao == 'cima':
                    self.rect.y = rect.y + TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

                elif(self.direcao == 'baixo'):
                    self.rect.y = rect.y - TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

                elif(self.direcao == 'esquerda'):
                    self.rect.x = rect.x + TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

                else:
                    self.rect.x = rect.x - TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

        #checar colisão com blocos destrutíveis
        for i in range (len(blocos_destrutiveis)):
            rect = pygame.rect.Rect(blocos_destrutiveis[i], (TAMANHO_CELULA, TAMANHO_CELULA))
            if self.rect.colliderect(rect):
                if self.direcao == 'cima':
                    self.rect.y = rect.y + TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

                elif(self.direcao == 'baixo'):
                    self.rect.y = rect.y - TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

                elif(self.direcao == 'esquerda'):
                    self.rect.x = rect.x + TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

                else:
                    self.rect.x = rect.x - TAMANHO_CELULA
                    self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])