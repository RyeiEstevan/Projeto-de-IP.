import pygame
from constantes import *
from mapa import Mapa
from mapa import Bordas
from blocos import Blocos_indestrutiveis
from personagem import Personagem
from item import Item
from sprites import sprites

def main():

    #Criando objetos e o grupo de seus sprites
    #sprites = pygame.sprite.Group()
    pygame.font.init()
    mapa = Mapa(CELULAS_ALTURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA, TAMANHO_MENU, TAMANHO_BORDAS) 
    bordas = [Bordas(i[0], i[1]) for i in mapa.bordas]
    blocos_ind = [Blocos_indestrutiveis(i[0], i[1]) for i in blocos_indestrutiveis]

    Item(mapa.tela, 0, 2, "velocidade")
    Item(mapa.tela, 0, 5, "tempo")
    Item(mapa.tela, 3, 8, "vida")
    Item(mapa.tela, 4, 2,"bomba")

    player = Personagem(mapa.tela, 25, 125)
    [sprites.add(i) for i in bordas + blocos_ind]

    fonte = pygame.font.SysFont('arial', 40, True, True)

    #Iniciando pygame e loop para o jogo ficar rodando até fecharem
    clock = pygame.time.Clock()
    Rodar = True
    pygame.init()
    while Rodar:
        mensagem = f'Vida: {player.vida}'
        mapa.tela.fill((0,0,0))
        texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
        mapa.tela.blit(mapa.background, (0, TAMANHO_BORDAS+TAMANHO_MENU))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rodar == False
                exit()
        mapa.tela.blit(texto_formatado, (0,0))
        player.sprite.draw(mapa.tela)
        sprites.draw(mapa.tela)
        sprites.update()
        player.sprite.update()
        pygame.display.update()
        clock.tick(60)

        if player.vida <= 0:
            Rodar = False

main()