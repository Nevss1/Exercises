# Esse tema contém estudo de progressão de pilhas

N, F = (int(i) for i in input().split()) # recebe dois valores inteiros divididos por um espaço
# N -> tamanho da matriz quadrada
# F -> Poder da fissura

vulcao = []
for i in range(N):
    vulcao.append([str(j) for j in input()])  ## faz uma lista da linha contendo cada valor da linha separado

pilha = [(0, 0)]
while pilha:
    linha, coluna = pilha.pop() # ponto inicial (0,0)
    if vulcao[linha][coluna] != '*' and F >= int(vulcao[linha][coluna]):
        vulcao[linha][coluna] = '*'
        if linha < N - 1: # verifica se a linha não é a linha mais de baixo (baixo)
            pilha.append((linha + 1, coluna))
        if coluna < N - 1:
            pilha.append((linha, coluna + 1))  # verifica se a coluna não é a coluna mais da direita
        if linha > 0:
            pilha.append((linha - 1, coluna))  # verifica se não é a linha mais em cima
        if coluna > 0:
            pilha.append((linha, coluna - 1))  # verifica se não é a coluna mais da esquerda

print(vulcao)