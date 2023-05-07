from pygame import transform, image
import pygame
from pygame.sprite import Sprite
import random
from sprites import *
from constantes import *
<<<<<<< HEAD
from entidades import Entidade
=======
from mapa import blocos_destrutiveis
>>>>>>> 0a4bc1f134c05ada09a58b753cb74da4a0bb57d6

class Inimigo(Entidade):

    def __init__(self, x, y, tipo, blocos_destrutiveis):
        super().__init__(x, y, TAMANHO_CELULA, blocos_destrutiveis, "polemonio")

        self.direcao = random.choice(["esquerda", "direita", "cima", "baixo"])
        self.colide = False
        self.velocidade = 2
        self.image = transform.scale(image.load(sprite[tipo]), (TAMANHO_CELULA, TAMANHO_CELULA))
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
        
        self.colisao(blocos_destrutiveis, blocos_indestrutiveis)
    
    def restringir_posicao(self, rect):

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

    def colisao_bordas(self):

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