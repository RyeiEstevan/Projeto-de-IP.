import pygame
from constantes import *

class Blocos_indestrutiveis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #Definindo tamanho dos blocos, sua cor e onde serão salvos
        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load("sprites\Blocos_indestrutiveis.png")
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
     
     
   
class Blocos_destrutiveis(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.tamanho_blocos = TAMANHO_CELULA
        self.image = pygame.image.load("sprites\Blocos_destrutiveis.png")
        self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

        #Destruiçao de bloco
        self.destruido = False

    def explode(self):
        if not self.destruido:
            self.destruido = True
            self.image = pygame.image.load("sprites\Blocos_destruidos.png")
            self.image = pygame.transform.scale(self.image, (self.tamanho_blocos, self.tamanho_blocos))
    
      #self.kill()



#essa função eu criei p verificar se há blocos destrutíveis no alcance da bomba, mas como não tinha a classe da bomba ainda coloquei por aqui
 def verificar_blocos_destrutiveis_no_alcance(self, mapa):
        blocos_destrutiveis = []

        #Verificando células na horizontal esquerda
        for x in range(self.rect.left - self.tamanho_blocos * self.alcance, self.rect.left, self.tamanho_blocos):
            y = self.rect.top
            if y >= 0 and y < len(mapa) and x >= 0 and x < len(mapa[y]) and mapa[y][x] == 1:
                blocos_destrutiveis.append((x, y))

        #Verificando células na horizontal direita
        for x in range(self.rect.right, self.rect.right + self.tamanho_blocos * self.alcance, self.tamanho_blocos):
            y = self.rect.top
            if y >= 0 and y < len(mapa) and x >= 0 and x < len(mapa[y]) and mapa[y][x] == 1:
                blocos_destrutiveis.append((x, y))

        #Verificando células na vertical p cima
        for y in range(self.rect.top - self.tamanho_blocos * self.alcance, self.rect.top, self.tamanho_blocos):
            x = self.rect.left
            if y >= 0 and y < len(mapa) and x >= 0 and x < len(mapa[y]) and mapa[y][x] == 1:
                blocos_destrutiveis.append((x, y))

        #Verificando células na vertical p baixo
        for y in range(self.rect.bottom, self.rect.bottom + self.tamanho_blocos * self.alcance, self.tamanho_blocos):
            x = self.rect.left
            if y >= 0 and y < len(mapa) and x >= 0 and x < len(mapa[y]) and mapa[y][x] == 1:
                blocos_destrutiveis.append((x, y))

        return blocos_destrutiveis

#essa função deve ser colocada na classe da bomba, mas ela verifica basicaemnte quais blocos devem ser destruídos:
def explode(self, mapa, blocos_destrutiveis):
    #Blocos q devem ser destruidos
    blocos_a_destruir = self.verificar_blocos_destrutiveis_no_alcance(mapa)
    for bloco_coord in blocos_a_destruir:
        for bloco in blocos_destrutiveis:
            if bloco.rect.topleft == bloco_coord:
                bloco.explode()
 
#O ideal passar a lista criada aqui de blocos destrutíveis como argumento na classe bomba p iterar sobre elea
blocos_destrutiveis = []
for i in range(MAPA_ALTURA):
    for j in range(MAPA_LARGURA):
        if mapa2[i][j] == 1:
            x = j * TAMANHO_CELULA
            y = i * TAMANHO_CELULA
            blocos_destrutiveis.append(Blocos_destrutiveis(x, y))

#Falta a classe bomba aqui p passar a lista de blocos destrutíveis
bomba = Bomba(jogador.rect.topleft, jogador.direcao, blocos_destrutiveis, mapa, jogador.alcance_bomba)

        
