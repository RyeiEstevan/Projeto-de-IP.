import pygame
from constantes import *
from mapa import Mapa
from mapa import Bordas
from blocos import Blocos_indestrutiveis
from personagem import Personagem


def main():

    #Criando objetos e o grupo de seus sprites
    sprites = pygame.sprite.Group()
    mapa = Mapa(CELULAS_ALTURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA, TAMANHO_MENU, TAMANHO_BORDAS) 
    bordas = [Bordas(i[0], i[1]) for i in mapa.bordas]
    blocos_ind = [Blocos_indestrutiveis(i[0], i[1]) for i in blocos_indestrutiveis]
    player = Personagem(mapa.tela, 25, 125)
    [sprites.add(i) for i in bordas+blocos_ind+[player]]

    #Iniciando pygame e loop para o jogo ficar rodando até fecharem
    clock = pygame.time.Clock()
    Rodar = True
    pygame.init()
    while Rodar:
        mapa.tela.blit(mapa.background, (0, TAMANHO_BORDAS+TAMANHO_MENU))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rodar == False
                exit()


        sprites.draw(mapa.tela)
        sprites.update()
        pygame.display.update()
        clock.tick(60)
main()