from pygame.sprite import Group

sprites = Group()
vilao = Group()

sprite = {
    # Interface
    "inicio": "sprites\Tela_inicial1.jpg",
    "ganhou": "sprites\Ganhou.jpg",
    "perdeu": "sprites\Perdeu.jpg",
    # Mapa
    "back" : "sprites\Back.png",
    "bordas": "sprites\Bordas.png",
    # Blocos
    "bloco_destruido": "Bloco_destruido.png",
    "bloco_destrutivel": "sprites\Bloco_destrutivel.png",
    "bloco_indestrutivel": "sprites\Blocos_indestrutiveis.png",
    # Bomba
    "bomba": "sprites\Bomba.png",
    "fogo": "sprites\Fogo.png",
    # Personagem e Inimigos
    "personagem": "sprites\Personagem.png",
    "polemonio": "sprites\Polemonio.png",
    # Coletáveis
    "portal": "sprites\Portal.png",
    "tempo": "sprites\Tempo.png",
    "velocidade": "sprites\Velocidade.png",
    "vida": "sprites\Vida.png",
    "item_bomba": "sprites\Bomba_power_up.png"
}
