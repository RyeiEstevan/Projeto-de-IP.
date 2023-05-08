from pygame import transform, image
import random
from sprites import *
from constantes import *
from mapa import blocos_destrutiveis
from entidades import Entidade
from bomba import Fogo, Bomba

class Inimigo(Entidade):

    DIRECOES = ["esquerda", "direita", "cima", "baixo"]
    
    def __init__(self, tipo, blocos_destrutiveis):
        pos_valida = False
        while pos_valida == False:
            x = random.randint(0, MAPA_ALTURA - 1)
            y = random.randint(0, MAPA_LARGURA - 1)
            if (x > 1 or y > 1) and celulas[x][y] not in blocos_indestrutiveis + blocos_destrutiveis:
                x, y = celulas[x][y]
                pos_valida = True
        super().__init__(x, y, TAMANHO_CELULA, blocos_destrutiveis, "polemonio")
        self.direcao = random.choice(__class__.DIRECOES)
        self.colide = False
        self.vida = 1
        self.velocidade = 1
        self.image = transform.scale(image.load(sprite[tipo]), (TAMANHO_CELULA, TAMANHO_CELULA))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        vilao.add(self)
        #self.adicionar_colisao(blocos_destrutiveis, blocos_indestrutiveis, Bomba.bombas)

    def morrer(self):
        vilao.remove(self)

    def update(self):
        if self.frames_invenciveis_restantes > 0:
            self.frames_invenciveis_restantes -= 1

        if self.rect.collidelist(Fogo.fogo) != -1:
            self.dano()

        if self.vida <= 0:
            self.morrer()

        if self.direcao == "esquerda":
            self.rect.x -= self.velocidade

        elif self.direcao == "direita":
            self.rect.x += self.velocidade

        elif self.direcao == "baixo":
            self.rect.y += self.velocidade

        elif self.direcao == "cima":
            self.rect.y -= self.velocidade  
        
        self.colisao(blocos_destrutiveis, blocos_indestrutiveis)
    
    def restringir_posicao(self, rect):

        if self.direcao == 'cima':
            self.rect.y = rect.y + TAMANHO_CELULA

        elif(self.direcao == 'baixo'):
            self.rect.y = rect.y - TAMANHO_CELULA

        elif(self.direcao == 'esquerda'):
            self.rect.x = rect.x + TAMANHO_CELULA

        else:
            self.rect.x = rect.x - TAMANHO_CELULA

        self.mudar_direcao()

    def mudar_direcao(self):
        self.direcao = random.choice([x for x in __class__.DIRECOES if x is not self.direcao])

    def colisao_bordas(self):

        if self.rect.x > (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA:
            self.rect.x = (CELULAS_LARGURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA
            self.mudar_direcao()
            

        elif self.rect.x < TAMANHO_BORDAS:
            self.rect.x = TAMANHO_BORDAS
            self.mudar_direcao()
            

        if self.rect.y > (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA:
            self.rect.y = (CELULAS_ALTURA*TAMANHO_CELULA)-TAMANHO_BORDAS-TAMANHO_CELULA
            self.mudar_direcao()
            

        elif self.rect.y < TAMANHO_MENU+TAMANHO_BORDAS:
            self.rect.y = TAMANHO_MENU+TAMANHO_BORDAS
            self.mudar_direcao()
