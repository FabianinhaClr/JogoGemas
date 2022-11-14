Jogo de pedras preciosas
Clara Antonelo
O jogo
Gemas consiste em um tabuleiro com colunas e número de linhas contendo gemas de letras distintas definidas pelo jogador no início do jogo. A cada passo do jogo o jogador deve escolher de posição duas gemas de forma que se crie uma cadeia de 3 ou mais gemas da mesma letra.. Quando a cadeia é criada, as gemas organizadas são destruídas (eliminadas), e fazendo com que as gemas caiam,, tomando o lugar das gemas destruídas. Ao cair, é possível que novas cadeias se formem. Os espaços vazios criados pelas gemas que caíram são então preenchidos por gemas geradas.
Desenvolvimento, não foi fácil mas estou viva, problemas técnicos com o meu notebook me impossibilitaram de encaminhar antes.
main() essa função lê comandos, testar sua validade e executar comando. 
n_linhas = int(input("Digite com quantas linhas você deseja jogar[3-10]: "))
n_colunas = int(input("Digite aqui com quantas colunas você deseja jogar [3-10]: "))
n_gemas = int(input("Digite o número de gemas diferentes você deseja incluir(lembrando: as gemas serão compostas por letras do alfabeto[3-26]: "))
esta parte do jogo serve para pedir o número de linhas e colunas que o jogador quer jogar, e a quantidade de variedade de gemas o jogador quer
Função criar(linhas, colunas) cria uma matriz com números de linhas por número de colunas e as preenche com espaços vazios.
Função completar(tabuleiro, n_gemas) completa espaços vazios no tabuleiro gerando novas gemas. 
Função randrange do pacote random para gerar novas gemas de maneira aleatória, essa função propositadamente se assemelha a função range, que cria uma lista de inteiros.
Função exibir(tabuleiro) exibe o tabuleiro atual identificando linhas e colunas correspondentes.
Função trocar(l1, c1, l2, c2, tabuleiro) tenta trocar as gemas das posições linha 1, coluna 1 e linha 2, coluna 2. 
Função eliminar(tabuleiro) elimina cadeias substituindo gemas destruídas por espaço em braco e retorna número de gemas destruídas. Esta função deverá necessariamente fazer uso das funções:
identificar_cadeias_horizontais
identificar_cadeias_verticais
eliminar_cadeia

Função identificar_cadeias_horizontais(tabuleiro) retorna uma lista contendo cadeias horizontais de 3 ou mais gemas. Cada cadeia é representada por uma lista [linha, coluna_i, linha, coluna_f]
linha: o número da linha
coluna_i: o número da coluna da gema mais à esquerda (menor) da cadeia
coluna_f: o número da coluna da gema mais à direita (maior) da cadeia

Função identificar_cadeias_verticais(tabuleiro) retorna uma lista contendo cadeias verticais de 3 ou mais gemas. Cada cadeia é representada por uma lista [linha_i, coluna, linha_f, coluna]
linha_i: o número da linha da gema mais superior (menor) da cadeia
coluna: o número da coluna das gemas da cadeia
linha_f: o número da linha mais inferior (maior) da cadeia

Função eliminar_cadeia(tabuleiro, cadeia) elimina as gemas compreendidas numa cadeia, representada por uma lista [linha_inicio, coluna_inicio, linha_fim, coluna_fim]
linha_i: o número da linha da gema mais superior (menor) da cadeia
coluna_i: o número da coluna da gema mais à esquerda (menor) da cadeia
linha_f: o número da linha mais inferior (maior) da cadeia
coluna_f: o número da coluna da gema mais à direita (maior) da cadeia
Retorna o número de gemas eliminadas 
Função deslocar(tabuleiro) desloca gemas para baixo, de forma que nenhum espaço vazio apareça abaixo de uma gema. Esta função deve necessariamente fazer uso da função deslocar_coluna.
Função deslocar_coluna(tabuleiro, i) desloca as gemas na coluna i para baixo, ocupando espaços vazios abaixo.
Função existem_movimentos_validos(tabuleiro) retorna True se existem mesmo uma cadeia de gemas válidas e False caso contrário.
