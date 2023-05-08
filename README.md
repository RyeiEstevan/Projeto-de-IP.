## Projeto-de-IP: CInberman

Nesse repositório, encontra-se o projeto final da disciplina de Introdução à Programação do curso de Ciência da Computação da Universidade Federal de Pernambuco, que é, basicamente, um sistema em 2D, cuja inspiração foi no jogo “Bomberman”. Nele, foram usados conceitos aprendidos durante todo o período da disciplina, tendo um enfoque e primeiro contato maiores com uma técnica de programação chamada de Programação Orientada a Objetos (POO).

Quando analisamos o contexto do jogo, pode-se sintetizar a ideia como uma ambientação de um jovem estudante do Centro de Informática (CIn) da UFPE tentando encontrar o pi estrela, a salvação para todos os problemas, para conseguir fugir do seu maior inimigo, o Polemônio, bastante conhecido pelos alunos do período 2022.2. Para isso, com a ajuda de suas maiores invenções, isto é, bombas que causam estragos gigantes, o jovem deve escapar em 1 minuto do vilão, podendo estender esse tempo a partir da coleta de timers ou acelerar a sua busca pelo salvador dos alunos do CIn por meio da coleta de buffs de velocidade ou de acréscimo de vida.

## Instruções para rodagem do código

Para execução do código, é necessário que haja o Python e o Pygame instalados em seu computador. Ao baixá-los, podemos seguir para o download e rodagem do código, que serão feitos da seguinte forma:

1) Faça o download do código pela aba code e escolha a opção de baixar o arquivo no formato ZIP.
2) Depois de baixado, extraia o arquivo ZIP.
3) Abra a pasta Projeto-de-IP.-main no seu editor de escolha.
4) Execute o arquivo main.py.

O movimento do jogador é controlado pelas teclas WASD. Ademais, a barra de espaço permite colocar a bomba no local em que o personagem está presente.

## Membros da equipe:

[Flávio Roberto (frtb)] - desenvolvimento do mapa, dos blocos indestrutíveis, das constantes e responsável pela limpeza do código.

[Gabriel Ayres (gcfa)] - desenvolvimento do sistema de contagem, bem como produção e organização dos canais de comunicação e elaboração do relatório.

[Gabriela Brito (gtcb)] - desenvolvimento dos blocos destrutíveis, geração desses blocos em lugares aleatórios e planejamento e construção do slide de apresentação do grupo.

[Gustavo Felipe (gfas2)] - desenvolvimento da bomba e criação do sistema de interação entre a bomba, os objetos destrutíveis e o personagem.

[Gustavo Santiago (gssm)] - desenvolvimento dos itens, criação dos sprites, bem como desenvolvimento e implementação do sistema de colisão do projeto, criação dos inimigos e responsável pela limpeza do código.

[Ryei Estevan (resm)] - criação do personagem e dos inimigos, bem como foi responsável pela limpeza do código.

## Organização do código:

Dividimos o código em diversos módulos, os quais descrevem e desenvolvem uma função específica no projeto geral. Sendo assim, podemos citar:

*main.py* - esse é o arquivo principal do código, no qual reunimos e implementamos todas as outras construções dos módulos produzidos em todo o projeto. Armazena, ainda, o laço de repetição principal do projeto, que irá permitir o controle da rodagem ou não do jogo;

*constantes.py* - aqui, são armazenadas as constantes que são usadas durante todo o projeto, como as medidas do mapa, das células, do menu, entre várias outras, descritas por constantes de fácil compreensão. Além disso, nesse módulo, desenvolvemos um dos sistemas que norteou toda a implementação da interface, tendo em vista que produzimos um mapa baseado em uma matriz. Ademais, importamos a biblioteca random para permitir a geração aleatória dos itens e dos dois tipos de blocos, os destrutíveis e indestrutíveis, trazendo a possibilidade de não existência de dois mapas iguais a cada rodada, tornando a experiência do jogador mais satisfatória;

*entidade.py* - o módulo aqui descrito é utilizado para estabelecer uma classe mãe para as classes do personagem e dos inimigos, tornando-as herdeiras dos seus métodos. Assim, temos a checagem das colisões com as bordas, com a bomba e com os blocos presentes nessa classe mãe, bem como é possível perceber a estruturação da movimentação do personagem e dos inimigos;

*personagem.py* - nesse módulo, voltamo-nos ao desenvolvimento da classe do personagem propriamente dito. Portanto, herdamos os métodos da classe entidade, bem como temos a definição da função update e da função de explosão da bomba, apagar fogo e as funções que refletem a interação do personagem com cada item disponível no mapa;

*inimigos.py* - nesse arquivo, focamos no desenvolvimento da classe dos inimigos do nosso protagonista, que herda métodos da classe mãe “entidades”. Sendo assim, criamos todas as dinâmicas dele com o mapa e com o personagem, dando-o uma movimentação randômica, tornando sua movimentação imprevisível e impedindo a repetição de comportamentos e facilidade excessiva da jogatina;

*mapa.py* - como o nome do módulo sugere, separamos esse esse arquivo para que construíssemos a classe do mapa, que abrigaria quase todo o espaço de rodagem do jogo na tela, trazendo a definição das suas propriedades, bem como criamos as bordas do mapa e as armazenamos em uma lista para a posterior checagem da colisão. Além dessa classe, criamos, também, a classe das bordas, que nos permitiu ter o controle da movimentação do personagem, podendo restringir os movimentos para apenas o espaço delimitado inicialmente. Por fim, aqui, temos a geração da posição dos blocos destrutíveis, indestrutíveis e dos itens;

*sprites.py* - acerca desse módulo, estabelecemos a criação dos sprites, que norteiam todos os objetos gráficos presentes no sistema durante a sua rodagem. Além disso, fizemos uso de uma classe (Group), importada do pygame.sprite, que nos permitiria manipular todos os objetos gráficos de uma vez, facilitando o trabalho como um todo. Por fim, criamos um dicionário para referenciar cada arquivo que seria usado graficamente;

*item.py* - esse módulo se debruçou para a criação da classe dos itens, recurso-chave para a criação do projeto, definidos em 4 tipos: vida, velocidade, tempo e portal. O item da vida nos permitiria acrescentar um coração ao personagem. O atributo de velocidade traria um acréscimo na velocidade do protagonista. O tempo permitiria o acréscimo de uma quantidade extra de segundos no timer, que estaria decrescendo. Por fim, o portal seria o representante do objetivo fim do jogo;

*timer.py* - aqui, buscamos desenvolver um dos sistemas de contagem do nosso jogo. Por conseguinte, criamos um cronômetro, com o auxílio da importação do módulo “time” do Python e utilizamos a função “time.time()” para que pudéssemos fazer as medições de forma coerente. Após isso, desenvolvemos o sistema de decrescimento do cronômetro, mecânica base para o funcionamento correto do jogo;

*bomba.py* - nesse módulo, trouxemos alguns dos recursos-chave do sistema construído, os quais são responsáveis por muitas das mecânicas que tentamos desenvolver. Desse modo, aqui, estabelecemos a  classe da bomba, bem como as suas diversas mecânicas de funcionamento, trazendo a função de explodir, bem como a definição da classe do fogo que a bomba soltaria após a explosão;

*blocos.py* - por fim, criamos, nesse arquivo, os blocos destrutíveis e indestrutíveis, que influenciam no modo como o personagem pode se movimentar no jogo, em virtude da possibilidade ou não de destruição de cada bloco e progressão do personagem no mapa.


## Bibliotecas utilizadas:

Quando analisam-se as bibliotecas que foram usadas para o desenvolvimento do código, pode-se perceber que três foram as norteadoras para a plena construção do sistema:

pygame: como requisito do projeto, utilizamos essa biblioteca para nos baseamos durante todo o desenvolvimento, a qual norteou e trouxe um crescimento considerável no conhecimento de todo o grupo. Além disso, fizemos uso de uma sub-biblioteca do pygame: no caso, o pygame.sprite, a qual permitiu a correta manipulação dos efeitos gráficos do jogo;
time: optamos por usar essa biblioteca em virtude da ideia de incrementar um timer ao jogo, visto que ele faria parte da mecânica, na medida em que, caso o cronômetro chegasse a 0 antes do fim do jogo, o jogador seria penalizado, sendo essa mecânica possível, apenas, com a manipulação e contagem de tempo;
random: essa biblioteca foi crucial para a melhoria da jogabilidade, tendo em vista que a usamos no tocante à geração dos blocos destrutíveis e indestrutíveis, bem como os itens coletáveis no mapa e na mecânica de movimento dos inimigos;

## Conceitos utilizados:

Foram utilizados conceitos que norteiam a programação como um todo. Destarte, é comum perceber o uso de estruturas condicionais, as quais foram usadas em diversos pontos do nosso trabalho, como nas checagens de colisão e de botões que foram pressionados, na checagem do cronômetro e da interação dele com o personagem, na geração dos blocos e nas interações da bomba.

Outrossim, temos o conceito de laços de repetição muito estruturados pelo código, o qual permite o controle da rodagem do programa, devido à presença do loop com o while, assim como a geração dos blocos destrutíveis, indestrutíveis e dos itens. Por fim, temos os loops, unidos com as ideias de listas e tuplas, como responsáveis pela geração do mapa como um todo, tendo em vista que são encarregados pela formação da matriz que constitui a base de organização do cenário.

A definição de funções também foi uma base muito importante e que foi usada em praticamente todos os módulos e formam as diversas lógicas presentes em cada um, sendo reunidas na função main.

O uso de dicionários permitiu um controle e organização maior dos nossos sprites, facilitando a leitura do código;

Por fim, pode-se citar o domínio dos conceitos de Programação Orientada a Objetos (POO), cuja importância se fez bastante perceptível nos diversos contextos de criação das classes e objetos do código, que permitiram o correto desenvolvimento do projeto e a melhor organização do programa como um todo.

## Desafios, erros e aprendizados:

No que tange aos desafios encontrados no projeto, pode-se citar a familiarização com o pygame, biblioteca que fomentou grande parte da construção do nosso código. Tendo em vista que estávamos tendo nosso primeiro contato com essa biblioteca, a assimilação da forma de funcionamento dela se tornou um pouco complicada. A fim de superar esse desafio, buscamos nos capacitar, por meio da leitura da documentação do pygame, bem como lemos e assistimos bastantes conteúdos relacionados a essa biblioteca.

Quando tratamos do maior erro que foi cometido no projeto, podemos afirmar, em conjunto, que coaduna bastante com a organização do código, a qual dificultou o processo de limpeza final. Logo, buscamos superar esse erro através da correta estruturação dos comentários após uma profunda releitura e debate de tudo o que fora produzido.

Enfim, ao analisar os aprendizados, podem-se destacar três pontos bastante evidentes: 

Todos os integrantes tiveram um crescimento bastante considerável em organização de código e domínio de divisão do programa em módulos;
Todos aprendemos, de forma definitiva, a utilizar o Git e o Github efetivamente, trazendo um formato de armazenamento melhor dos nossos projetos;
Conseguimos construir conhecimentos e explorar mais as técnicas da Programação Orientada a Objetos.


## Captura de tela do sistema

![Captura de tela 2023-05-07 223251](https://user-images.githubusercontent.com/127794150/236719379-7c660070-5899-4f9e-ab1f-882e927d04fc.png)![Captura de tela 2023-05-07 232249](https://user-images.githubusercontent.com/127794150/236720003-66c63487-f27d-4a23-90cb-ff69abd3419a.png)
![Captura de tela 2023-05-07 232305](https://user-images.githubusercontent.com/127794150/236720011-75881638-36a8-46b0-a0ba-7cab68a552c3.png)
