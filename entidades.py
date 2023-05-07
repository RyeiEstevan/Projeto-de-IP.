from pygame.sprite import Sprite
from constantes import *
from pygame.rect import Rect
from pygame import image, transform
from sprites import sprite

class Entidade(Sprite):

    def __init__(self, x, y, tamanho, blocos_destrutiveis, tipo):
        super().__init__()
        self.altura = tamanho
        self.largura = tamanho
        self.velocidade = 1
        self.vida = 5
        self.image = image.load(sprite[tipo])
        self.image = transform.scale(self.image, (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.explodir = False
        self.colide_bomba = False
        self.blocos_destrutiveis = blocos_destrutiveis
        self.vida = 3
        self.buff_tempo = 0
        self.tempo_explodir = 0
        self.bomba = 0
        
    def mover(self):

        if self.direcao == "esquerda":
            self.rect.x -= self.velocidade

        if self.direcao == "direita":
            self.rect.x += self.velocidade

        if self.direcao == "baixo":
            self.rect.y += self.velocidade

        if self.direcao == "cima":
            self.rect.y -= self.velocidade  


    def colisao(self, *args: list[Sprite], **kwargs):

        self.colisao_bordas()

        #checar colisão com blocos
        spritelist = []
        for i in args:
            spritelist += i
        for rect in (Rect(i, (TAMANHO_CELULA, TAMANHO_CELULA)) for i in spritelist):
            if self.rect.colliderect(rect):
                self.restringir_posicao(rect)
                
        #checar colisão com bomba
        if self.explodir:
            rect = Rect((self.bomba.rect.x,self.bomba.rect.y),(TAMANHO_CELULA, TAMANHO_CELULA))
            if self.rect.colliderect(rect):
                if self.colide_bomba:
                    self.restringir_posicao(rect)
            else:
                self.colide_bomba = True

    def restringir_posicao(self, rect: Rect):
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

    def colisao_bordas(self):

        if self.rect.x > (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.largura:
            self.rect.x = (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.largura
        elif self.rect.x < TAMANHO_BORDAS:
            self.rect.x = TAMANHO_BORDAS
        if self.rect.y > (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.altura:
            self.rect.y = (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-self.altura
        elif self.rect.y < TAMANHO_MENU+TAMANHO_BORDAS:
           self.rect.y = TAMANHO_MENU+TAMANHO_BORDAS