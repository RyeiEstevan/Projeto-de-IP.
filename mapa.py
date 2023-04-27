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
        self.bordas = []
        #Criando as 4 bordas e salvando elas numa lista para checar colisão depois
    def desenhar_bordas(self):
        cor_borda = (80, 80, 80)
        self.bordas = [pygame.draw.line(self.tela, cor_borda, (0, self.largura_menu+int(self.largura_bordas/2)), (self.largura, self.largura_menu+int(self.largura_bordas/2)), self.largura_bordas),
        pygame.draw.line(self.tela, cor_borda, (int(self.largura_bordas/2), self.largura_menu+int(self.largura_bordas/2)), (int(self.largura_bordas/2), self.altura), self.largura_bordas),
        pygame.draw.line(self.tela, cor_borda, (0, self.altura-int(self.largura_bordas/2)), (self.largura, self.altura-int(self.largura_bordas/2)), self.largura_bordas), 
        pygame.draw.line(self.tela, cor_borda, (self.largura-int(self.largura_bordas/2), self.largura_menu+int(self.largura_bordas/2)), (self.largura-int(self.largura_bordas/2), self.altura), self.largura_bordas)]
        
        
