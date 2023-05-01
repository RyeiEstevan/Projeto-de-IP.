import pygame
from constantes import *
from sprites import sprites
from item import Item

class Personagem(pygame.sprite.Sprite):
    def __init__(self, tela, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.tela = tela
        self.vida = 1
        self.altura = TAMANHO_CELULA-10
        self.largura = TAMANHO_CELULA-10
        self.velocidade = 5
        self.image = pygame.image.load("sprites\Personagem.png")
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.sprite = pygame.sprite.Group(self)
        self.bombas = 0

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
        
        if botao[pygame.K_SPACE]:
            print(f"Boom bomba, local: ({self.rect.x}, {self.rect.y})")
        
        self.colisao()

        for i in Item.itens:
            if self.rect.colliderect(i):
                self.acao[i.tipo](self)
                i.kill()

    def buff_speed(self):
        self.velocidade += 10
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
        x1 = self.rect.x ; y1 = self.rect.y
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
            if self.rect.colliderect(pygame.rect.Rect(blocos_indestrutiveis[i], (TAMANHO_CELULA, TAMANHO_CELULA))):
                self.rect.x = x1
                self.rect.y = y1