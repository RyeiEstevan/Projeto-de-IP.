from pygame import transform, image
from pygame.sprite import Sprite
import random
from sprites import sprites
from constantes import *

class Inimigo(Sprite):

    sprite = {
        "polemonio" : "sprites\Polemonio.png"
    }

    def __init__(self, tela, x, y, tipo):
        super().__init__()

        self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
        self.velocidade = 1
        self.image = transform.scale(image.load(Inimigo.sprite[tipo]), (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        sprites.add(self)

    def update(self):

        if self.direcao == "esquerda":
            self.rect.x -= self.velocidade

        elif self.direcao == "direita":
            self.rect.x += self.velocidade

        elif self.direcao == "baixo":
            self.rect.y -= self.velocidade

        elif self.direcao == "cima":
            self.rect.y += self.velocidade  

    
    



    
    

