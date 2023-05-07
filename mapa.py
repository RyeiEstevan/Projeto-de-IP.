import pygame
from constantes import *
from sprites import sprite

class Mapa:
    def __init__(self, altura, largura, largura_menu, largura_bordas):

        #Definindo propriedades do mapa
        self.altura = altura
        self.largura = largura
        self.largura_menu = largura_menu
        self.largura_bordas = largura_bordas
        self.background = pygame.image.load(sprite["fundo"])
        self.coração = pygame.image.load(sprite["vida"])
        self.coração = pygame.transform.scale(self.coração, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.relogio = pygame.image.load(sprite["tempo"])
        self.relogio = pygame.transform.scale(self.relogio, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.background = pygame.transform.scale(self.background, (CELULAS_LARGURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA))

        #Criando a tela do jogo e dando nome a ela
        self.tela = pygame.display.set_mode((largura, altura)) 
        #pygame.display.flip()
        pygame.display.set_caption("CINberman")
        
        self.bordas = []
       
        #Criando as 4 bordas e salvando elas numa lista para checar colisão depois
        for y in range (TAMANHO_BORDAS+TAMANHO_MENU, TAMANHO_CELULA*CELULAS_ALTURA, TAMANHO_BORDAS):
            self.bordas.append((0, y))
            x = (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS
            self.bordas.append((x, y))
        
        for x in range (0, (TAMANHO_CELULA*CELULAS_LARGURA), TAMANHO_BORDAS):
            y = TAMANHO_MENU
            self.bordas.append((x, y))
            y = (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS
            self.bordas.append((x, y))


class Bordas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite["bordas"])
        self.image = pygame.transform.scale(self.image, (TAMANHO_BORDAS, TAMANHO_BORDAS))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
            
        