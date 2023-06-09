import pygame
from constantes import *
from sprites import *
from item import Item
from bomba import Bomba, Fogo
from pygame.sprite import Group
from entidades import Entidade
from mapa import blocos_destrutiveis
from inimigos import x, y
#Definindo a classe do personagem
class Personagem(Entidade):

    def __init__(self, x, y, blocos_destrutiveis):
        #Gerando as caracteristicas do personagem
        super().__init__(x, y, TAMANHO_CELULA-10, blocos_destrutiveis, "personagem")
        self.velocidade = 3
        self.sprite = Group(self)
        self.blocos_destrutiveis = blocos_destrutiveis
        self.vida = 3
        self.buff_tempo = 0
        self.maximo_bombas = 1
        self.portal = False
    #Atualiza os status do personagem, como a movimentação, checa a colisão com os inimigos, o fogo e os blocos
    def update(self):

        if pygame.sprite.spritecollide(self, vilao, False):
            self.dano()

        if self.rect.collidelist(Fogo.fogo) != -1:
            self.dano()

        if self.frames_invenciveis_restantes > 0:
            self.frames_invenciveis_restantes -= 1

        self.buff_tempo = 0
        self.x1 = self.rect.x ; self.y1 = self.rect.y
        botao = pygame.key.get_pressed()

        if botao[pygame.K_SPACE]:
            if len(Bomba.bombas) < self.maximo_bombas and not self.dentro_bomba:
                self.dentro_bomba = True
                for i in vilao:
                    i.dentro_bomba = True
                bomba_barulho = pygame.mixer.Sound("sons\Colocar bomba.wav")
                Bomba(self.rect.x, self.rect.y, self.blocos_destrutiveis)
                bomba_barulho.play()

        if botao[pygame.K_a]:
            self.rect.x -= self.velocidade

        if botao[pygame.K_d]:
            self.rect.x += self.velocidade

        if botao[pygame.K_w]:
            self.rect.y -= self.velocidade

        if botao[pygame.K_s]:
            self.rect.y += self.velocidade
        
        self.colisao(blocos_destrutiveis, blocos_indestrutiveis)
        for i in Item.itens:
            if self.rect.colliderect(i):
                self.acao[i.tipo](self)
                i.kill()
    #Definindo os efeitos dos power ups
    def buff_speed(self):
        self.velocidade += 3

    def curar(self):
        self.vida += 1

    def tempo(self):
        self.buff_tempo = 30
    
    def fim_jogo(self):
        self.portal = True

    def item_bomba(self):
        self.maximo_bombas += 1

    acao = {
        "velocidade" : buff_speed,
        "vida" : curar,
        "tempo" : tempo,
        "portal" : fim_jogo,
        "item_bomba" : item_bomba
    }