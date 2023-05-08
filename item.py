import pygame
from constantes import *
from pygame.sprite import Sprite
from sprites import sprites, sprite

#Declarando biblioteca com os 'power ups' e itens que teremos no jogo: Vida, Tempo, Velocidade, e o Portal:

# Criando  a classe Item:
class Item(Sprite):

    itens = []

    
# Definindo o Construtor da classe:
    def __init__(self, tela, cel, tipo: str):
        
        Sprite.__init__(self)
        self.image = pygame.image.load(sprite[tipo])
        self.image = pygame.transform.scale(self.image, (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.tela = tela
        self.tipo = tipo
        self.rect.x = cel[X]
        self.rect.y = cel[Y]
        sprites.add(self)
        Item.itens.append(self)
        
        
#Criando a  função que remove da tela o Sprite do item coletado:
    def kill(self):
       pegou = pygame.mixer.Sound("sons\Item.wav")
       Item.itens.remove(self)
       sprites.remove(self)
       pegou.play()
        
