from pygame.mixer import Sound
from pygame.sprite import Sprite
from constantes import *
from pygame.rect import Rect
from pygame import image, transform
from sprites import sprite
from bomba import Bomba

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
        self.dentro_bomba = False
        self.blocos_destrutiveis = blocos_destrutiveis
        self.vida = 3
        self.frames_invenciveis_restantes = 60

    def dano(self):
        if self.frames_invenciveis_restantes == 0:
            self.vida -= 1
            Sound("sons\Dano.wav").play()
            self.frames_invenciveis_restantes = 120
        
    def mover(self):

        if self.direcao == "esquerda":
            self.rect.x -= self.velocidade

        if self.direcao == "direita":
            self.rect.x += self.velocidade

        if self.direcao == "baixo":
            self.rect.y += self.velocidade

        if self.direcao == "cima":
            self.rect.y -= self.velocidade  


    def colisao(self, *args: list[list]):

        self.colisao_bordas()

        #checar colisão com blocos
        rectlist = []
        for lista in args:
            rectlist += [Rect(i, (TAMANHO_CELULA, TAMANHO_CELULA)) for i in lista]
        for rect in rectlist:
            if self.rect.colliderect(rect):
                self.restringir_posicao(rect)
                
        #checar colisão com bomba
        
        colidiu = False
        for rect in Bomba.bombas:
            if self.rect.colliderect(rect):
                colidiu = True
                if not self.dentro_bomba:
                    self.restringir_posicao(rect)                
        if not colidiu:
            self.dentro_bomba = False

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