import pygame
from constantes import *

class Mapa:
    def __init__(self, altura, largura, largura_menu, largura_bordas):
        
        #Definindo propriedades do mapa
        self.altura = altura
        self.largura = largura
        self.largura_menu = largura_menu
        self.largura_bordas = largura_bordas
        self.background = pygame.image.load("wallpaperflare.com_wallpaper.jpg")

        #Criando a tela do jogo e dando nome a ela
        self.tela = pygame.display.set_mode((largura, altura)) 
        self.tela.blit(self.background, (0, 0))
        pygame.display.flip()
        pygame.display.set_caption("CINberman (nome temporario)")
        self.bordas = []
        
    def desenhar_bordas(self):
        cor_borda = (80, 80, 80)

        #Criando as 4 bordas e salvando elas numa lista para checar colisão depois
        for i in range (1, ((TAMANHO_CELULA*CELULAS_ALTURA)-TAMANHO_MENU)//TAMANHO_BORDAS):
            self.bordas.append(pygame.draw.rect(self.tela, cor_borda, (0, i*TAMANHO_BORDAS+TAMANHO_MENU, TAMANHO_BORDAS, TAMANHO_BORDAS)))
            self.bordas.append(pygame.draw.rect(self.tela, cor_borda, ((CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS, i*TAMANHO_BORDAS+TAMANHO_MENU, TAMANHO_BORDAS, TAMANHO_BORDAS)))
        
        for a in range (0, (TAMANHO_CELULA*CELULAS_LARGURA)//TAMANHO_BORDAS):
            self.bordas.append(pygame.draw.rect(self.tela, cor_borda, (a*TAMANHO_BORDAS, TAMANHO_MENU, TAMANHO_BORDAS, TAMANHO_BORDAS)))
            self.bordas.append(pygame.draw.rect(self.tela, cor_borda, (a*TAMANHO_BORDAS, (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS, TAMANHO_BORDAS, TAMANHO_BORDAS)))





        