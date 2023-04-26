import pygame

class Mapa:
    def __init__(self, altura, largura, menu, bordas):

        #Definindo propriedades do mapa
        self.tela_altura = altura
        self.tela_largura = largura
        self.tamanho_menu = menu
        self.largura_bordas = bordas

        #Criando a tela do jogo e dando nome a ela
        self.tela = pygame.display.set_mode((self.tela_largura, self.tela_altura)) 
        self.tela.fill((0, 153, 0)) 
        pygame.display.flip()
        pygame.display.set_caption("CINberman (nome temporario)")

        #Criando as 4 bordas e salvando elas numa lista para checar colisão depois
        cor_borda = (80, 80, 80)
        self.bordas = [pygame.draw.line(self.tela, cor_borda, (0,self.tamanho_menu), (0, self.tela_altura), self.largura_bordas), pygame.draw.line(self.tela, cor_borda, (0, self.tela_altura), (self.tela_largura, self.tela_altura), self.largura_bordas), pygame.draw.line(self.tela, cor_borda, (self.tela_largura, self.tela_altura), (self.tela_largura, self.tamanho_menu), self.largura_bordas), pygame.draw.line(self.tela, cor_borda, (0, self.tamanho_menu), (self.tela_largura, self.tamanho_menu), int(self.largura_bordas/2))]
        
        