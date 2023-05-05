import pygame
from constantes import *
from sprites import sprites

class Bomba(pygame.sprite.Sprite):
    def __init__(self,x, y, blocos_destrutiveis):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites\Bomba.png")
        self.image = pygame.transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.quebrar = blocos_destrutiveis

        for i in celulas:
            for j in i:
                if  x >= j[X] and x < j[X] + TAMANHO_CELULA:
                    if j not in blocos_indestrutiveis:
                        self.rect.x = j[X]
                if y >= j[Y] and y < j[Y] + TAMANHO_CELULA:
                    if j not in blocos_indestrutiveis:
                        self.rect.y = j[Y]
        
        sprites.add(self)
        
    def explodir(self):
        self.fogo1 = Fogo(self.rect.x, self.rect.y - TAMANHO_CELULA, self.quebrar) #Fogo Superior
        self.fogo2 = Fogo(self.rect.x, self.rect.y + TAMANHO_CELULA, self.quebrar) #Fogo Inferior
        self.fogo3 = Fogo(self.rect.x - TAMANHO_CELULA, self.rect.y, self.quebrar) #Fogo Esquerdo
        self.fogo4 = Fogo(self.rect.x + TAMANHO_CELULA, self.rect.y, self.quebrar) #Fogo Direito
        self.fogo5 = Fogo(self.rect.x, self.rect.y, self.quebrar) #Fogo Central

class Fogo(pygame.sprite.Sprite):
    def __init__(self,x, y, quebrar):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites\Fogo.png")
        self.image = pygame.transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        for i in quebrar:
            if self.rect.colliderect(i.rect):
                sprites.remove(i)
                blocos_destrutiveis.remove((i.rect.x, i.rect.y))
                quebrar.remove(i)

        
        if not pygame.sprite.spritecollide(self, sprites, False):
            sprites.add(self)

