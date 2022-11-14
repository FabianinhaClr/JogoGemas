import random

random.seed(0)

def main():
    print("Bem Vindo ao Jogo Gemas feito exclusivamente por Clara Antonelo, vamos relembrar, você está jogando o jogo Gemas \\"
          "e funciona da seguinte forma junte 3 ou mais gemas numa mesma linha ou coluna para eliminá-las")
    pontos = 0
    n_linhas = int(input("Digite com quantas linhas você deseja jogar[3-10]: "))
    n_colunas = int(input("Digite aqui com quantas colunas você deseja jogar [3-10]: "))
    n_gemas = int(input("Digite o número de gemas diferentes você deseja incluir(lembrando: as gemas serão compostas por letras do alfabeto[3-26]: "))
    tabuleiro = criar(n_linhas, n_colunas)
    completar(tabuleiro, n_gemas)
    numero_gemas = eliminar(tabuleiro)
    while numero_gemas > 0:
        deslocar(tabuleiro)
        completar(tabuleiro, n_gemas)
        numero_gemas = eliminar(tabuleiro)
    while existem_movimentos_validos(tabuleiro):
        exibir(tabuleiro)
        comando = input("Deseja permanecer no jogo ou sair?")
        if comando == "permanecer":
            linha1 = int(input("Qual a linha(horizontal) da gema que você deseja mover: "))
            coluna1 = int(input("Qual a coluna(vertical) da gema que você deseja mover: "))
            linha2 = int(input("Qual a linha(horizontal) da gema que você deseja substituir: "))
            coluna2 = int(input("Qual a coluna(vertical) da gema que você deseja substituir: "))
            print()
            valido = trocar(linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                numero_gemas = eliminar(tabuleiro)
                total_gemas = 0
                while numero_gemas > 0:
                    deslocar(tabuleiro)
                    completar(tabuleiro, n_gemas)
                    total_gemas += numero_gemas
                    print("Uauuu, nesta rodada: %d gemas foram destruídas por você! Continue assim" % numero_gemas)
                    exibir(tabuleiro)
                    numero_gemas = eliminar(tabuleiro)
                pontos += total_gemas
                print("Você destruiu %d de gemas! Estou orgulhosa!" % (total_gemas))
            else:
                print()
                print("OPS, este movimento é inválido!")
        elif comando == "sair":
            print("Que pena de esteja indo embora")
            return
        else:
            print("Eu sou apenas uma máquina e ainda não entendo bem o que você deseja, tente de novo e analise as opções com calma!")
    print("Fim de Jogo: Não existem mais movimentos válidos para está partida!")
    print("Você destruiu um total de %d gemas" % (pontos))


def completar(tabuleiro, n_gemas):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    n_linhas = len(tabuleiro)
    n_colunas = len(tabuleiro[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            if tabuleiro[i][j] == ' ':
                gema = random.randrange(n_gemas)
                tabuleiro[i][j] = alfabeto[gema]

def criar(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(' ')
        matriz.append(linha)
    return matriz

def exibir(tabuleiro):
    n_linhas = len(tabuleiro)
    n_colunas = len(tabuleiro[0])
    string = "\n    "
    for i in range(n_colunas):
        string += str(i) + " "
    string += "\n  +"
    for i in range(n_colunas):
        string += "--"
    string += "-+\n"
    for linha in range(n_linhas):
        string += str(linha) + " | "
        for coluna in range(n_colunas):
            string += tabuleiro[linha][coluna] + " "
        string += "|\n"
    string += "  +"
    for i in range(n_colunas):
        string += "--"
    string += "-+"
    print(string)

def trocar(linha1, coluna1, linha2, coluna2, tabuleiro):
    if linha1 + 1 != linha2:
        if linha1 - 1 != linha2:
            if coluna1 + 1 != coluna2:
                if coluna1 - 1 != coluna2:
                    return False
    novo_tabuleiro = clonar_matriz(tabuleiro)
    novo_tabuleiro[linha1][coluna1] = tabuleiro[linha2][coluna2]
    novo_tabuleiro[linha2][coluna2] = tabuleiro[linha1][coluna1]
    if len(identificar_cadeias_horizontais(novo_tabuleiro)) > 0:
        tabuleiro[linha1][coluna1] = novo_tabuleiro[linha1][coluna1]
        tabuleiro[linha2][coluna2] = novo_tabuleiro[linha2][coluna2]
        return True
    elif len(identificar_cadeias_verticais(novo_tabuleiro)) > 0:
        tabuleiro[linha1][coluna1] = novo_tabuleiro[linha1][coluna1]
        tabuleiro[linha2][coluna2] = novo_tabuleiro[linha2][coluna2]
        return True
    return False

def eliminar(tabuleiro):
    gemas = 0
    horizontais = identificar_cadeias_horizontais(tabuleiro)
    verticais = identificar_cadeias_verticais(tabuleiro)
    for h in horizontais:
        gemas += eliminar_cadeia(tabuleiro, h)
    for v in verticais:
        gemas += eliminar_cadeia(tabuleiro, v)

    return gemas

def identificar_cadeias_horizontais(tabuleiro):
    cadeias = []
    igual = True
    coluna = 0
    n_linhas = len(tabuleiro)
    n_colunas = len(tabuleiro[0])
    for linha in range(n_linhas):
        while coluna < n_colunas - 2:
            cont = 1
            while cont < n_colunas - coluna and igual:
                if tabuleiro[linha][coluna] != tabuleiro[linha][coluna + cont]:
                    if cont >= 2:
                        break
                    igual = False
                else:
                    cont += 1
            if igual and cont > 2:
                if tabuleiro[linha][coluna] != ' ':
                    cadeias.append([linha, coluna, linha, coluna + cont - 1])
            igual = True
            coluna += cont
        coluna = 0
    return cadeias

def identificar_cadeias_verticais(tabuleiro):
    cadeias = []
    igual = True
    linha = 0
    n_linhas = len(tabuleiro)
    n_colunas = len(tabuleiro[0])
    for coluna in range(n_colunas):
        while linha < n_colunas - 2:
            cont = 1
            while cont < n_linhas - linha and igual:
                if tabuleiro[linha][coluna] != tabuleiro[linha + cont][coluna]:
                    if cont >= 2:
                        break
                    igual = False
                else:
                    cont += 1
            if igual and cont > 2:
                if tabuleiro[linha][coluna] != ' ':
                    cadeias.append([linha, coluna, linha + cont - 1, coluna])
            igual = True
            linha += cont
        linha = 0
    return cadeias

def eliminar_cadeia(tabuleiro, cadeia):
    gemas = 0
    if cadeia[0] == cadeia[2]:
        for i in range(cadeia[1], cadeia[3] + 1):
            tabuleiro[cadeia[0]][i] = ' '
            gemas += 1
    else:
        for j in range(cadeia[0], cadeia[2] + 1):
            tabuleiro[j][cadeia[1]] = ' '
            gemas += 1
    return gemas

def deslocar(tabuleiro):
    n_colunas = len(tabuleiro[0])
    for i in range(n_colunas):
        deslocar_coluna(tabuleiro, i)
    h = identificar_cadeias_horizontais(tabuleiro)
    v = identificar_cadeias_verticais(tabuleiro)
    if len(h) > 0 or len(v) > 0:
        eliminar(tabuleiro)
        deslocar(tabuleiro)

def deslocar_coluna(tabuleiro, i):
    cont = 0
    linha = len(tabuleiro) - 1
    while linha > 0:
        while (tabuleiro[linha][i] == ' ') and (linha - (cont + 1)) > 0:
            cont += 1
            if tabuleiro[linha - cont][i] != ' ':
                tabuleiro[linha][i] = tabuleiro[linha - cont][i]
                tabuleiro[linha - cont][i] = ' '
        cont = 0
        linha -= 1

def existem_movimentos_validos(tabuleiro):
    clone = clonar_matriz(tabuleiro)
    n_linhas = len(tabuleiro)
    n_colunas = len(tabuleiro[0])
    for linha in range(n_linhas):
        if validos_horizontal(clone, linha):
            return True

    return False

def validos_horizontal(tabuleiro, linha):
    for coluna in range(len(tabuleiro[0]) - 1):
        if trocar(linha, coluna, linha, coluna + 1, tabuleiro):
            return True
    return False

def clonar_matriz(tabuleiro):
    novo = []
    n_linhas = len(tabuleiro)
    n_colunas = len(tabuleiro[0])
    for lin in range(n_linhas):
        linha = []
        for col in range(n_colunas):
            linha.append(tabuleiro[lin][col])
        novo.append(linha)
    return novo

main()