import pygame
from constantes import *
from sprites import sprites, sprite
from mapa import blocos_destrutiveis
from pygame.sprite import Sprite
from pygame import image, transform

#classe da bomba
class Bomba(Sprite):

    bombas = []

    def __init__(self,x, y, blocos_destrutiveis):
        #Definindo as propriedades da bomba,
        Sprite.__init__(self)
        self.image = image.load(sprite["bomba"])
        self.image = transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.quebrar = blocos_destrutiveis
        self.contagem = -180
        Bomba.bombas.append(self.rect)
 
        for i in celulas:
            for j in i:
                if  x >= j[X] and x < j[X] + TAMANHO_CELULA:
                    if j not in blocos_indestrutiveis:
                        self.rect.x = j[X]
                if y >= j[Y] and y < j[Y] + TAMANHO_CELULA:
                    if j not in blocos_indestrutiveis:
                        self.rect.y = j[Y]
        
        sprites.add(self)

    def update(self):
        self.contagem += 1
        if self.contagem == 0:
            explosao = pygame.mixer.Sound("sons\Explosão.wav")
            self.explodir()
            explosao.play()
        elif self.contagem == 60:
            self.apagar_fogo()
        
    def explodir(self):
        sprites.remove(self)
        Bomba.bombas.remove(self.rect)
        self.fogo1 = Fogo(self.rect.x, self.rect.y - TAMANHO_CELULA, self.quebrar) #Fogo Superior
        self.fogo2 = Fogo(self.rect.x, self.rect.y + TAMANHO_CELULA, self.quebrar) #Fogo Inferior
        self.fogo3 = Fogo(self.rect.x - TAMANHO_CELULA, self.rect.y, self.quebrar) #Fogo Esquerdo
        self.fogo4 = Fogo(self.rect.x + TAMANHO_CELULA, self.rect.y, self.quebrar) #Fogo Direito
        self.fogo5 = Fogo(self.rect.x, self.rect.y, self.quebrar) #Fogo Central

class Fogo(Sprite):

    fogo = []

    def __init__(self,x, y, quebrar):
        Sprite.__init__(self)
        self.image = image.load(sprite["fogo"])
        self.image = transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contagem = 60
        __class__.fogo.append(self)

        for i in quebrar:
            if self.rect.colliderect(i.rect):
                sprites.remove(i)
                blocos_destrutiveis.remove((i.rect.x, i.rect.y))
                quebrar.remove(i)
        
        if not pygame.sprite.spritecollide(self, sprites, False):
            sprites.add(self)

    def update(self):
        self.contagem -= 1
        if self.contagem == 0:
            self.apagar()

    def apagar(self):
        __class__.fogo.remove(self)
        sprites.remove(self)