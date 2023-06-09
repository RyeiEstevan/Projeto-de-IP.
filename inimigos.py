from pygame import transform, image
import random
from sprites import *
from constantes import *
from mapa import blocos_destrutiveis
from entidades import Entidade
from bomba import Fogo, Bomba
#Definindo a classe dos inimigos
class Inimigo(Entidade):

    DIRECOES = ["esquerda", "direita", "cima", "baixo"]
    
    def __init__(self, tipo, blocos_destrutiveis):
        #Variável para checar se a posição gerada para o inimigo é válida
        pos_valida = False
        #Loop para ficar gerando posições para o inimigo nascer, até ter uma válida
        while pos_valida == False:
            x = random.randint(0, MAPA_ALTURA - 1)
            y = random.randint(0, MAPA_LARGURA - 1)
            if (x > 1 or y > 1) and celulas[x][y] not in blocos_indestrutiveis + blocos_destrutiveis:
                x, y = celulas[x][y]
                pos_valida = True
        #Gerando as caracteristicas do inimigo
        super().__init__(x, y, TAMANHO_CELULA, blocos_destrutiveis, "polemonio")
        self.direcao = random.choice(__class__.DIRECOES)
        self.rect.topleft = x, y
        #Lista contenco os inimigos
        vilao.add(self)
    #Função para retirar o inimigo morto da lista
    def morrer(self):
        vilao.remove(self)
    #Atualiza a direção que o inimigo se move, além de checar se ele colidiu como fogo
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
    #Restringe a posição do inimigo
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
    #Sorteia uma nova direção para ele andar
    def mudar_direcao(self):
        self.direcao = random.choice([x for x in __class__.DIRECOES if x is not self.direcao])
    #Checa a colisão com a borda
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
