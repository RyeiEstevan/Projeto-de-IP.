#Definindo todos os parâmetros do jogo em relação a coordenadas e tamanhos
#Tamanho de cada posição da matriz
TAMANHO_CELULA = 50
#Quantidade de posições na horizontal e vertical
CELULAS_ALTURA = 14
CELULAS_LARGURA = 16
#configurações de menu e bordas
TAMANHO_MENU = 100
X = 0 ;  Y = 1
TAMANHO_BORDAS = int(TAMANHO_CELULA/2)
MAPA_ALTURA = CELULAS_ALTURA - int(TAMANHO_MENU/TAMANHO_CELULA) - int( (TAMANHO_BORDAS*2)/TAMANHO_CELULA )
MAPA_LARGURA = CELULAS_LARGURA - int( (TAMANHO_BORDAS*2)/TAMANHO_CELULA )

celulas = [] #celulas será uma matriz com a coordenada de cada celula
c = []
y = TAMANHO_MENU + TAMANHO_BORDAS
#gerando a matriz do mapa
for i in range (MAPA_ALTURA):
    x = TAMANHO_BORDAS
    for a in range (MAPA_LARGURA):
        c.append((x, y))
        x += TAMANHO_CELULA
    celulas.append(c) ; c = []
    y += TAMANHO_CELULA
#gerando uma lista com as coordenadas dos blocos indestrutíveis
blocos_indestrutiveis = []
for i in range (MAPA_ALTURA):
    for a in range (MAPA_LARGURA):
        if i%2 != 0 and a%2 != 0:
            x = celulas[i][a][X] ; y = celulas[i][a][Y]
            blocos_indestrutiveis.append((x, y))


NUM_BLOCOS_DESTRUTIVEIS = 80