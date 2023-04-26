import pygame

class Mapa:
    def __init__(self, altura, largura, largura_menu, largura_bordas):
        
        #Definindo propriedades do mapa
        self.altura = altura
        self.largura = largura
        self.largura_menu = largura_menu
        self.largura_bordas = largura_bordas

        #Criando a tela do jogo e dando nome a ela
        self.tela = pygame.display.set_mode((largura, altura)) 
        self.tela.fill((0, 153, 0)) 
        pygame.display.flip()
        pygame.display.set_caption("CINberman (nome temporario)")
        cor_borda = (80, 80, 80)
        #Criando as 4 bordas e salvando elas numa lista para checar colisão depois
        
        self.bordas = [pygame.draw.line(self.tela, cor_borda, (0, largura_menu+int(largura_bordas/2)), (largura, largura_menu+int(largura_bordas/2)), largura_bordas),
        pygame.draw.line(self.tela, cor_borda, (int(largura_bordas/2), largura_menu+int(largura_bordas/2)), (int(largura_bordas/2), altura), largura_bordas),
        pygame.draw.line(self.tela, cor_borda, (0, altura-int(largura_bordas/2)), (largura,altura-int(largura_bordas/2)), largura_bordas), 
        pygame.draw.line(self.tela, cor_borda, (largura-int(largura_bordas/2), largura_menu+int(largura_bordas/2)), (largura-int(largura_bordas/2), altura), largura_bordas)]
        
        