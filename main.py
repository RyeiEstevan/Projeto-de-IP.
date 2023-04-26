import pygame
from mapa import Mapa
from blocos import Blocos_indestrutiveis

#Criando mapa e blocos que não quebram
mapa = Mapa(650, 750, 100, 50) 
blocos = Blocos_indestrutiveis(mapa.tela, mapa.tamanho_menu, mapa.largura_bordas)

#Inicio da main
def main():

    #Iniciando pygame e loop para o jogo ficar rodando até fecharem
    Rodar = True
    pygame.init()
    while Rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rodar == False
                exit()

        pygame.display.update()
main()