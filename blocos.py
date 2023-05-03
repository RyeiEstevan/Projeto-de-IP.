import pygame
from constantes import *

class Blocos_indestrutiveis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #Definindo tamanho dos blocos, sua cor e onde serão salvos
        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load("sprites\Blocos_indestrutiveis.png")
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
     
     
   
class Blocos_destrutiveis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load("sprites\Blocos_destrutiveis.png")
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

        # Variável de controle de destruição do bloco
        self.destruido = False

    def explode(self):
        if not self.destruido:
            self.destruido = True
            self.image = pygame.image.load("sprites\Blocos_destruidos.png")
            self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
    
        
            # Realizando outras ações necessárias, como remover o bloco do grupo de sprite
            # self.kill()

     
        
