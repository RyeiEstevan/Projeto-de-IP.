import pygame

class Blocos_indestrutiveis:
    def __init__(self, tela, x, y):

        #Definindo tamanho dos blocos, sua cor e onde serão salvos
        self.tamanho_blocos = 50
        xo = x ; cor_blocos = (255, 255, 212)
        self.blocos_indestrutiveis = []

        #criando 6 lugares com blocos e 7 lugares sem blocos em cada uma das 13 linhas do mapa
        for i in range (1, 13):
            y+= 50
            x = xo
            if i%2 != 0:
                for a in range (1, 13):
                    x += 50
                    if a%2 != 0:
                        bloco = pygame.draw.rect(tela, cor_blocos, (x, y, 50, 50))
                        self.blocos_indestrutiveis.append(bloco)

