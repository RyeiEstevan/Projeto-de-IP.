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







