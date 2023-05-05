import pygame
from constantes import *
from sprites import sprites
from item import Item
from bomba import Bomba

class Personagem(pygame.sprite.Sprite):
    def __init__(self, tela, x, y):
        super().__init__()
        self.vida = 1
        self.altura = TAMANHO_CELULA-10
        self.largura = TAMANHO_CELULA-10
        self.velocidade = 3
        self.image = pygame.image.load("sprites\Personagem.png")
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.sprite = pygame.sprite.Group(self)
        self.bombas = 0
        self.explodir = False
        self.tempo_explodir = 0
        self.bomba = 0

    def update(self):
        self.x1 = self.rect.x ; self.y1 = self.rect.y
        botao = pygame.key.get_pressed()
        if botao[pygame.K_a]:
            self.rect.x -= self.velocidade

        if botao[pygame.K_d]:
            self.rect.x += self.velocidade

        if botao[pygame.K_w]:
            self.rect.y -= self.velocidade

        if botao[pygame.K_s]:
            self.rect.y += self.velocidade
        
        if botao[pygame.K_SPACE]:
            if not self.explodir:
                self.explodir = True
                print(f"Boom bomba, local: ({self.rect.x}, {self.rect.y})")
                self.bomba = Bomba(self.rect.x, self.rect.y)

        if self.explodir:        
            self.tempo_explodir += 1
            if self.tempo_explodir == 180:
                self.explodir_bomba()
            elif self.tempo_explodir == 240:
                self.apagar_fogo()
        
        self.colisao()

        for i in Item.itens:
            if self.rect.colliderect(i):
                self.acao[i.tipo](self)
                i.kill()

    def explodir_bomba(self):
        sprites.remove(self.bomba)
        self.bomba.explodir()
    
    def apagar_fogo(self):
        self.tempo_explodir = 0
        sprites.remove(self.bomba.fogo1)
        sprites.remove(self.bomba.fogo2)
        sprites.remove(self.bomba.fogo3)
        sprites.remove(self.bomba.fogo4)
        sprites.remove(self.bomba.fogo5)
        self.explodir = False

    def buff_speed(self):
        self.velocidade += 2
        print(f"velocidade: {self.velocidade}")

    def add_bomba(self):
        self.bombas += 1
        print(f"bombas: {self.bombas}")

    def curar(self):
        self.vida += 1
        print(f"vida: {self.vida}")

    def dano(self):
        self.vida -= 1
        print(f"vida: {self.vida}")

    acao = {
        "velocidade" : buff_speed,
        "bomba" : add_bomba,
        "vida" : curar,
        "tempo" : dano
    }

    def colisao(self):
        #checar colisão bordas
        if self.rect.x > (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.largura:
            self.rect.x = (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.largura
        elif self.rect.x < TAMANHO_BORDAS:
            self.rect.x = TAMANHO_BORDAS
        if self.rect.y > (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.altura:
            self.rect.y = (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.altura
        elif self.rect.y < TAMANHO_MENU+TAMANHO_BORDAS:
           self.rect.y = TAMANHO_MENU+TAMANHO_BORDAS
        
        for i in range (len(blocos_indestrutiveis)):
            rect = pygame.rect.Rect(blocos_indestrutiveis[i], (TAMANHO_CELULA, TAMANHO_CELULA))
            if self.rect.colliderect(rect):
                direcao = (self.x1 - rect.x,self.y1 - rect.y)
                if abs(direcao[0]) > abs(direcao[1]):
                    if direcao[0] < 0:
                        self.rect.x = rect.x - self.largura
                    else:
                        self.rect.x = rect.x + TAMANHO_CELULA
                else:
                    if direcao[1] < 0:
                        self.rect.y = rect.y - self.altura
                    else:
                        self.rect.y = rect.y + TAMANHO_CELULA

