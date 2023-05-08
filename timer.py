import time

#Criando a classe Timer:
class Timer:
    
    #Definindo o Construtor da classe Timer
    def __init__(self, value = 0):
        self.start = time.time()
        self.set(value)

    #Criando a função que lê e retorna o tempo  real já reduzido:    
    def get (self) -> float:
        return time.time() - self.start
    
    #Criando a Função que define o tempo:
    def set (self, value : float):
        self.start = time.time() - value

    #Criando a Função que imprime o tempo na tela.    
    def __str__(self):
        value = self.get()
        self.sec = str(int(value))
