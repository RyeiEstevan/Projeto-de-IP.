import random

TAMANHO_CELULA = 50
CELULAS_ALTURA = 14
CELULAS_LARGURA = 16
TAMANHO_MENU = 100
X = 0 ;  Y = 1
TAMANHO_BORDAS = int(TAMANHO_CELULA/2)
MAPA_ALTURA = CELULAS_ALTURA - int(TAMANHO_MENU/TAMANHO_CELULA) - int( (TAMANHO_BORDAS*2)/TAMANHO_CELULA )
MAPA_LARGURA = CELULAS_LARGURA - int( (TAMANHO_BORDAS*2)/TAMANHO_CELULA )

celulas = [] #celulas será uma matriz com a coordenada de cada celula
c = []
y = TAMANHO_MENU + TAMANHO_BORDAS
for i in range (MAPA_ALTURA):
    x = TAMANHO_BORDAS
    for a in range (MAPA_LARGURA):
        c.append((x, y))
        x += TAMANHO_CELULA
    celulas.append(c) ; c = []
    y += TAMANHO_CELULA

blocos_indestrutiveis = []
for i in range (MAPA_ALTURA):
    for a in range (MAPA_LARGURA):
        if i%2 != 0 and a%2 != 0:
            x = celulas[i][a][X] ; y = celulas[i][a][Y]
            blocos_indestrutiveis.append((x, y))



mapa2 = [[0 for j in range(MAPA_LARGURA)] for i in range(MAPA_ALTURA)]
num_blocos_destrutiveis = 50
blocos_destrutiveis = []
i
for i in range(num_blocos_destrutiveis):
    x = random.randint(0, MAPA_ALTURA - 1)
    y = random.randint(0, MAPA_LARGURA - 1)
    if (celulas[x][y] != celulas[0][0] and celulas[x][y] != celulas[0][1] and celulas[x][y] != celulas[1][0]) and celulas[x][y] not in blocos_indestrutiveis:
        blocos_destrutiveis.append(celulas[x][y])
