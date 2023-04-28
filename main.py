import pygame
from constantes import *
from mapa import Mapa
from blocos import Blocos_indestrutiveis
from personagem import personagem


def main():

    #Criando mapa e blocos que não quebram
    mapa = Mapa(CELULAS_ALTURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA, TAMANHO_MENU, TAMANHO_BORDAS) 
    blocos = Blocos_indestrutiveis(mapa.tela)
    player = personagem(mapa.tela, 25, 125 )
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

            if event.type == pygame.KEYDOWN:
                tecla = pygame.key.get_pressed()
                player.movimentacao(tecla)
            
            


        
        blocos.desenhar_blocos()
        mapa.desenhar_bordas()
        player.desenhar_personagem()
        pygame.display.update()
main()