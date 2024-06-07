#2021 Fase1 OBI
registro = int(input())
valores = []

for i in range(registro):
    registrar = input()
    registrar = registrar
    valores.append(registrar)

tempos_respostas = []
for v in valores:
    if v[0] == "R":
        tem = False
        for i in tempos_respostas:
            if i[2]: # está no vácuo?
                i[1] +=1 # recebe + 1
            if i[0] == int(v[2:]):
                tem = True # já existe esse amigo
                i[2] = True # Volta a ficar no vácuo

        if not tem: # se não tiver um amigo novo, adicione a lista
            recebido = [int(v[2:]), 0, True] # -> 0 amigo / 1 t.r / 2 vácuo?
            tempos_respostas.append(recebido)
    elif v[0] == "E":
        for i in tempos_respostas:
            if int(i[0]) == int(v[2:]):
                i[1] += 1
                i[2] = False
            elif i[2]: # está no vácuo?
                i[1] += 1
    else:
        for i in tempos_respostas:
            if i[2]: # está no vácuo?
                i[1] += int(v[2])-1

tempos_respostas = sorted(tempos_respostas) # código abaixo é o output correto
for i in tempos_respostas:
    if i[2] == True:
        i[1] = -1
    print(i[0], i[1])