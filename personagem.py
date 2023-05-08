import pygame
from constantes import *
from sprites import sprites, sprite
from item import Item
from bomba import Bomba
from pygame.sprite import Group
from entidades import Entidade
from mapa import blocos_destrutiveis
from inimigos import x, y

class Personagem(Entidade):
    def __init__(self, x, y, blocos_destrutiveis):
        super().__init__(x, y, TAMANHO_CELULA-10, blocos_destrutiveis, "personagem")
        self.velocidade = 5
        self.sprite = Group(self)
        self.explodir = False
        self.colide_bomba = False
        self.blocos_destrutiveis = blocos_destrutiveis
        self.vida = 3
        self.buff_tempo = 0
        self.tempo_explodir = 0
        self.bomba = 0
        self.portal = False
        self.dano = pygame.mixer.Sound("sons\Dano.wav")

    def update(self):
        self.buff_tempo = 0
        self.x1 = self.rect.x ; self.y1 = self.rect.y
        botao = pygame.key.get_pressed()
        if botao[pygame.K_SPACE]:
            if not self.explodir:
                bomba_barulho = pygame.mixer.Sound("sons\Colocar bomba.wav")
                self.explodir = True
                print(f"Boom bomba, local: ({self.rect.x}, {self.rect.y})")
                self.bomba = Bomba(self.rect.x, self.rect.y, self.blocos_destrutiveis)
                bomba_barulho.play()

        if botao[pygame.K_a]:
            self.rect.x -= self.velocidade

        if botao[pygame.K_d]:
            self.rect.x += self.velocidade

        if botao[pygame.K_w]:
            self.rect.y -= self.velocidade

        if botao[pygame.K_s]:
            self.rect.y += self.velocidade       
 

        if self.explodir:        
            self.tempo_explodir += 1
            if self.tempo_explodir == 180:
                explosao = pygame.mixer.Sound("sons\Explosão.wav")
                self.explodir_bomba()
                explosao.play()

            elif self.tempo_explodir == 240:
                self.apagar_fogo()
        
        self.colisao(blocos_destrutiveis, blocos_indestrutiveis)
        for i in Item.itens:
            if self.rect.colliderect(i):
                self.acao[i.tipo](self)
                i.kill()

    def explodir_bomba(self):
        sprites.remove(self.bomba)
        self.bomba.explodir()
        if self.bomba.fogo1.rect.colliderect(self.rect):
            self.dano.play()
            self.vida -= 1
        if self.bomba.fogo2.rect.colliderect(self.rect):
            self.dano.play()
            self.vida -= 1
        if self.bomba.fogo3.rect.colliderect(self.rect):
            self.dano.play()
            self.vida -= 1
        if self.bomba.fogo4.rect.colliderect(self.rect):
            self.dano.play()
            self.vida -= 1
        if self.bomba.fogo5.rect.colliderect(self.rect):
            self.dano.play()
            self.vida -= 1
    
    def apagar_fogo(self):
        self.tempo_explodir = 0
        sprites.remove(self.bomba.fogo1)
        sprites.remove(self.bomba.fogo2)
        sprites.remove(self.bomba.fogo3)
        sprites.remove(self.bomba.fogo4)
        sprites.remove(self.bomba.fogo5)
        self.explodir = False
        self.colide_bomba = False

    def buff_speed(self):
        self.velocidade += 5

    def curar(self):
        self.vida += 1

    def tempo(self):
        self.buff_tempo = 30
    
    def fim_jogo(self):
        self.portal = True

    acao = {
        "velocidade" : buff_speed,
        "vida" : curar,
        "tempo" : tempo,
        "portal" : fim_jogo
    }