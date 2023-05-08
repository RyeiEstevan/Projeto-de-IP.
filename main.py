import pygame
from constantes import *
from mapa import Mapa,  Bordas, blocos_destrutiveis, items_posição
from blocos import Blocos_indestrutiveis, Blocos_destrutiveis
from personagem import Personagem
from item import Item
from sprites import *
from timer import Timer
from inimigos import Inimigo

def main():
    pygame.mixer.music.set_volume(0.5)
    tema = pygame.mixer.music.load("sons\Tema.mp3")
    pygame.mixer.music.play(-1)

    tempo_invencivel = 0
    #Criando objetos e o grupo de seus sprites
    #sprites = pygame.sprite.Group()
    pygame.font.init()
    mapa = Mapa(CELULAS_ALTURA*TAMANHO_CELULA, CELULAS_LARGURA*TAMANHO_CELULA, TAMANHO_MENU, TAMANHO_BORDAS) 
    bordas = [Bordas(i[0], i[1]) for i in mapa.bordas]
    blocos_ind = [Blocos_indestrutiveis(i[0], i[1]) for i in blocos_indestrutiveis]
    blocos_dest = [Blocos_destrutiveis(i[0], i[1]) for i in blocos_destrutiveis]

    Item(mapa.tela, items_posição[0], "velocidade")
    Item(mapa.tela, items_posição[1], "tempo")
    Item(mapa.tela, items_posição[2], "vida")
    Item(mapa.tela, items_posição[3], "portal")

    inimigo = Inimigo("polemonio", blocos_dest)
    player = Personagem(25, 125, blocos_dest)
    [sprites.add(i) for i in bordas + blocos_ind + blocos_dest]

    
    fonte = pygame.font.SysFont('arial', 40, True, True)

    # Gerando o timer
    tempo = 60
    timer = Timer()

    #Iniciando pygame e loop para o jogo ficar rodando até fecharem
    clock = pygame.time.Clock()
    Rodar = True
    pygame.init()
    while Rodar:
        timer.__str__() ; tempo += player.buff_tempo
        timer_impressao = f'{tempo-int(timer.sec)}s'
        texto_timer = fonte.render(timer_impressao, False, (255, 255, 255))
        mensagem = f'{player.vida}'
        mapa.tela.fill((0,0,0))
        texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
        mapa.tela.blit(mapa.background, (0, TAMANHO_BORDAS+TAMANHO_MENU))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rodar == False
                exit()
        
        vilao.draw(mapa.tela)
        vilao.update()
        mapa.tela.blit(texto_timer, (TAMANHO_CELULA*CELULAS_LARGURA - 100 -TAMANHO_CELULA//2,0))
        mapa.tela.blit(texto_formatado, (50,0))
        player.sprite.draw(mapa.tela)
        sprites.draw(mapa.tela)
        sprites.update()
        player.sprite.update()

        if pygame.sprite.spritecollide(player, vilao, False) and tempo_invencivel == 0:
            player.dano.play()
            player.vida -= 1
            tempo_invencivel += 1
        elif tempo_invencivel > 0 and tempo_invencivel < 75:
            tempo_invencivel +=1
        else:
            tempo_invencivel = 0

        mapa.tela.blit(mapa.relogio, (TAMANHO_CELULA*CELULAS_LARGURA-50, 0))
        mapa.tela.blit(mapa.coração, (0, 0))
        pygame.display.update()
        clock.tick(60)

        if tempo-int(timer.sec) < 0:
            player.dano.play()
            player.vida -= 1
            tempo += 60
        if player.vida <= 0:
            Rodar = False
            win_lose(0)
        elif player.portal:
            Rodar = False
            win_lose(1)
        #Depois de perder ou ganhar, se você apertar qualquer botão do teclado, a tela é fechada automaticamente

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

def win_lose(W_L):
    if W_L == 1:
        W_L = "ganhou"
    elif W_L == 0:
        W_L = "perdeu"
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
