import pygame
from constantes import *
from mapa import Mapa,  Bordas, blocos_destrutiveis, items_posição
from blocos import Blocos_indestrutiveis, Blocos_destrutiveis
from personagem import Personagem
from item import Item
from sprites import *
from timer import Timer
from inimigos import Inimigo
from bomba import Fogo

def main():
    pygame.mixer.music.set_volume(0.5)
    tema = pygame.mixer.music.load("sons\Tema.mp3")
    pygame.mixer.music.play(-1)

    #Criando objetos e o grupo de seus sprites
    pygame.font.init()
    mapa = Mapa(CELULAS_ALTURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA, TAMANHO_MENU, TAMANHO_BORDAS) 
    bordas = [Bordas(i[0], i[1]) for i in mapa.bordas]
    blocos_ind = [Blocos_indestrutiveis(i[0], i[1]) for i in blocos_indestrutiveis]
    blocos_dest = [Blocos_destrutiveis(i[0], i[1]) for i in blocos_destrutiveis]

    #Criando os itens
    itens = ["velocidade", "tempo", "vida", "portal", "item_bomba"]
    for i, tipo in enumerate(itens):
        Item(mapa.tela, items_posição[i], tipo)

    #Criando os inimigos
    numero_inimigos = 4
    for _ in range(numero_inimigos):
        Inimigo("polemonio", blocos_dest)

    #Criando o personagem
    player = Personagem(25, 125, blocos_dest)
    [sprites.add(i) for i in bordas + blocos_ind + blocos_dest]

    #Definindo a fonte dos textos
    fonte = pygame.font.SysFont('arial', 40, True, True)

    # Gerando o timer
    tempo = 60
    timer = Timer()

    #Iniciando pygame e loop para o jogo ficar rodando até fecharem
    clock = pygame.time.Clock()
    Rodar = True
    pygame.init()

    while Rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rodar == False
                exit()
                
        #Gerando o timer na tela
        timer.__str__() ; tempo += player.buff_tempo
        timer_impressao = f'{tempo-int(timer.sec)}s'
        texto_timer = fonte.render(timer_impressao, False, (255, 255, 255))

        #Gerando a vida na tela
        mensagem = f'{player.vida}'
        mapa.tela.fill((0,0,0))
        texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
        mapa.tela.blit(mapa.background, (0, TAMANHO_BORDAS+TAMANHO_MENU))
        
        #Desenhando os sprites na tela
        vilao.draw(mapa.tela)
        vilao.update()
        mapa.tela.blit(texto_timer, (TAMANHO_CELULA*CELULAS_LARGURA - 100 -TAMANHO_CELULA//2,0))
        mapa.tela.blit(texto_formatado, (50,0))
        player.sprite.draw(mapa.tela)
        sprites.draw(mapa.tela)
        sprites.update()
        player.sprite.update()

        #Desenhando os sprites do relogio e do coração
        mapa.tela.blit(mapa.relogio, (TAMANHO_CELULA*CELULAS_LARGURA-50, 0))
        mapa.tela.blit(mapa.coração, (0, 0))
        pygame.display.update()
        clock.tick(60)

        #Checa se o tempo acabou, reseta o timer e dá dano no personagem
        if tempo-int(timer.sec) < 0:
            player.dano()
            tempo += 60

        #checa se o personagem ainda tem vidas
        if player.vida <= 0:
            Rodar = False
            win_lose("perdeu")

        #Acaba o jogo quando o personagem encontra o portal
        elif player.portal:
            Rodar = False
            win_lose("ganhou")

        #Depois de perder ou ganhar, se você apertar qualquer botão do teclado, a tela é fechada automaticamente

#Tela de início
def start():
    largura = CELULAS_LARGURA*TAMANHO_CELULA
    altura = CELULAS_ALTURA*TAMANHO_CELULA
    tela_start = pygame.display.set_mode((largura, altura)) 
    start_back = pygame.image.load(sprite["inicio"])
    start_back = pygame.transform.scale(start_back, (largura, altura))
    pygame.display.set_caption("CINberman - Start_screen")
    pygame.init()
    no_menu = True
    while no_menu:
        tela_start.blit(start_back, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_menu == False
                exit()
        botao = pygame.key.get_pressed()
        if botao[pygame.K_RETURN]:
            no_menu = False
            main()
        if botao[pygame.K_ESCAPE]:
            no_menu = False
            exit()
        pygame.display.update()

#Tela de fim de jogo, tanto de derrota quanto para vitória
def win_lose(W_L):
    largura = CELULAS_LARGURA*TAMANHO_CELULA
    altura = CELULAS_ALTURA*TAMANHO_CELULA
    tela_wl = pygame.display.set_mode((largura, altura)) 
    wl_back = pygame.image.load(sprite[W_L])
    wl_back = pygame.transform.scale(wl_back, (largura, altura))
    if W_L == "ganhou":
        pygame.display.set_caption("CINberman - Você ganhou!")
    elif W_L == "perdeu":
        pygame.display.set_caption("CINberman - Você perdeu!")
    pygame.init()
    no_wl = True
    while no_wl:
        tela_wl.blit(wl_back, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_wl == False
                exit()
            if event.type == pygame.KEYDOWN:
                no_wl == False
                exit()
        pygame.display.update()


start()
