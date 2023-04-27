import pygame
from constantes import *
from mapa import Mapa
from blocos import Blocos_indestrutiveis


def main():

    #Criando mapa e blocos que não quebram
    mapa = Mapa(CELULAS_ALTURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA, TAMANHO_MENU, TAMANHO_BORDAS) 
    blocos = Blocos_indestrutiveis(mapa.tela)

    #Iniciando pygame e loop para o jogo ficar rodando até fecharem
    Rodar = True
    pygame.init()
    while Rodar:
        mapa.tela.fill((0, 153, 0)) 
        blocos.desenhar_blocos()
        mapa.desenhar_bordas()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rodar == False
                exit()

        
        blocos.desenhar_blocos()
        mapa.desenhar_bordas()
        pygame.display.update()
main()