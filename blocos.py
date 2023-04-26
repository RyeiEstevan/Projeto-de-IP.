import pygame

class Blocos_indestrutiveis:
    def __init__(self, tela, tamanho_menu, tamanho_bordas):

        #Definindo propriedades do mapa e vendo a posição de onde começaremos a criar os blocos (x0, y0)
        cor_blocos = (200, 80, 80)
        self.largura_bloco = 65
        self.altura_bloco = 46
        xo = int(tamanho_bordas/2) - self.largura_bloco  -8; yo = int(tamanho_bordas/2) + tamanho_menu -self.altura_bloco -6
        self.blocos_indestruvieis = []
        xl = xo
        
        #Loop que cria 5 lugares sem blocos e 5 lugares com blocos em cada uma das 10 linhas do mapa
        for _ in range (5):
            yo += self.altura_bloco*2 
            xo = xl
            for _ in range(5):
                xo += self.largura_bloco*2 
                bloco = pygame.draw.rect(tela, cor_blocos, (xo, yo, self.largura_bloco, self.altura_bloco))
                
                #Salvando os blocos em uma lista para checar colisão depois
                self.blocos_indestruvieis.append(bloco)