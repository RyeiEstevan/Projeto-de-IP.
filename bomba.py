import pygame
from constantes import *
from sprites import sprites, sprite
from mapa import blocos_destrutiveis
from pygame.sprite import Sprite
from pygame import image, transform

#classe da bomba
class Bomba(Sprite):

    bombas = []

    def __init__(self,x, y, blocos_destrutiveis):
        #Definindo as propriedades da bomba
        Sprite.__init__(self)
        self.image = image.load(sprite["bomba"])
        self.image = transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        #Lista com os blocos destrutiveis para utilizar na hora de gerar o fogo da bomba
        self.quebrar = blocos_destrutiveis
        #Variável para controlar o tempo da bomba explodir
        self.contagem = -180
        Bomba.bombas.append(self.rect)
        #Loop para encontrar as coordenadas que a bomba precisa estar
        for i in celulas:
            for j in i:
                if  x + TAMANHO_CELULA/2 >= j[X] and x + TAMANHO_CELULA/2 < j[X] + TAMANHO_CELULA:
                    if j not in blocos_indestrutiveis:
                        self.rect.x = j[X]
                if y + TAMANHO_CELULA/2 >= j[Y] and y + TAMANHO_CELULA/2 < j[Y] + TAMANHO_CELULA:
                    if j not in blocos_indestrutiveis:
                        self.rect.y = j[Y]
        
        sprites.add(self)
    #Definindo update para atualizar toda a mecânica da bomba, do timer para ela explodir e o som de quando ela é colocada
    def update(self):
        self.contagem += 1
        if self.contagem == 0:
            explosao = pygame.mixer.Sound("sons\Explosão.wav")
            self.explodir()
            explosao.play()
        elif self.contagem == 60:
            self.apagar_fogo()
    #Definindo explodir para espalhar o fogo da bomba
    def explodir(self):
        #Adicionando na lista quebrar os blocos atingidos pelo fogo
        sprites.remove(self)
        Bomba.bombas.remove(self.rect)
        self.fogo1 = Fogo(self.rect.x, self.rect.y - TAMANHO_CELULA, self.quebrar) #Fogo Superior
        self.fogo2 = Fogo(self.rect.x, self.rect.y + TAMANHO_CELULA, self.quebrar) #Fogo Inferior
        self.fogo3 = Fogo(self.rect.x - TAMANHO_CELULA, self.rect.y, self.quebrar) #Fogo Esquerdo
        self.fogo4 = Fogo(self.rect.x + TAMANHO_CELULA, self.rect.y, self.quebrar) #Fogo Direito
        self.fogo5 = Fogo(self.rect.x, self.rect.y, self.quebrar) #Fogo Central
#Definindo a classe fogo 
class Fogo(Sprite):

    fogo = []

    def __init__(self,x, y, quebrar):
        #Gerando as propriedades básicas do fogo, como o sprite e a posição
        Sprite.__init__(self)
        self.image = image.load(sprite["fogo"])
        self.image = transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Variável para contar o tempo até o fogo sumir
        self.contagem = 60
        #Destruindo os blocos 
        for i in quebrar:
            if self.rect.colliderect(i.rect):
                sprites.remove(i)
                blocos_destrutiveis.remove((i.rect.x, i.rect.y))
                quebrar.remove(i)
        #Colocando o sprit do fogo 
        if not pygame.sprite.spritecollide(self, sprites, False):
            sprites.add(self)
            __class__.fogo.append(self)
    #Definindo update para atualizar o fogo
    def update(self):
        #Variável para controlar o tempo que o fogo fica na tela
        self.contagem -= 1
        if self.contagem == 0:
            self.apagar()
    #Definindo apagar para apagar o fogo da explosão
    def apagar(self):
        __class__.fogo.remove(self)
        sprites.remove(self)