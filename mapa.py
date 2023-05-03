import pygame
from constantes import *

class Mapa:
    def __init__(self, altura, largura, largura_menu, largura_bordas):

        #Definindo propriedades do mapa
        self.altura = altura
        self.largura = largura
        self.largura_menu = largura_menu
        self.largura_bordas = largura_bordas
        self.background = pygame.image.load("sprites\Back.jpg")

        #Criando a tela do jogo e dando nome a ela
        self.tela = pygame.display.set_mode((largura, altura)) 
        #pygame.display.flip()
        pygame.display.set_caption("CINberman (nome temporario)")
        self.bordas = []
       
        #Criando as 4 bordas e salvando elas numa lista para checar colisão depois
        for i in range (1, ((TAMANHO_CELULA*CELULAS_ALTURA)-TAMANHO_MENU)//TAMANHO_BORDAS):
            x = 0 ; y = i*TAMANHO_BORDAS+TAMANHO_MENU
            self.bordas.append((x, y))
            x = (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS ; y = i*TAMANHO_BORDAS+TAMANHO_MENU
            self.bordas.append((x, y))
        
        for a in range (0, (TAMANHO_CELULA*CELULAS_LARGURA)//TAMANHO_BORDAS):
            x = a*TAMANHO_BORDAS ; y = TAMANHO_MENU
            self.bordas.append((x, y))
            x = a*TAMANHO_BORDAS ; y = (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS
            self.bordas.append((x, y))
         
        mapa2 = [[0 for j in range(MAPA_LARGURA)] for i in range(MAPA_ALTURA)]
        num_blocos_destrutiveis = 120
        for i in range(num_blocos_destrutiveis):
            x = random.randint(0, MAPA_LARGURA - 1)
            y = random.randint(0, MAPA_ALTURA - 1)
            mapa2[y][x] = 1


class Bordas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites\Borda.jpg")
        self.image = pygame.transform.scale(self.image, (TAMANHO_BORDAS, TAMANHO_BORDAS))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        
            
        
