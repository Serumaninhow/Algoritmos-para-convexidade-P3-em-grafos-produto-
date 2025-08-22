def caminho_para_alvo_em_n_somas(conjunto, n_repeticoes, alvo):
    
    if(alvo > n_repeticoes * conjunto[-1]): 
        return False 
    
    mapa = [0] * (n_repeticoes) 
    mapa[-1] = len(conjunto) - 1
    
    while mapa[0] <= mapa[-1]:
        soma=0 
        for i in mapa:
            soma+=conjunto[i]
        if soma == alvo:
            return mapa
        elif soma < alvo:
            if mapa[0] < mapa[-1]:
                mapa[0]+=1
            else:
                mapa.sort()
                if(mapa[0] == mapa[-1]): 
                    return False 
        else:
            if(mapa[0] > mapa[1]):
                mapa[0]-=1
                aux = mapa[0] 
                mapa.sort() 
                if aux == mapa[0]:
                    return False
            else:
                mapa[-1]-=1
    return False 

def Z(conjunto_fator, conjunto_potencia):
    p1 = conjunto_fator
    p2 = conjunto_potencia
    acumulado = set(p1) | set(p2)
    for x in p2: 
        if x == 1:
            continue
        for i in range(1*x, x*p1[-1] + 1):
            res = caminho_para_alvo_em_n_somas(p1, x, i) #
            total=0
            if(res != False):
                for j in res:
                    total+=p1[j]
                aux = {total}
                acumulado = acumulado | aux  
    return acumulado 
    
def Z_dois_sentidos(conjunto_A, conjunto_B):
    Z_A = Z(conjunto_A, conjunto_B)
    Z_B = Z(conjunto_B, conjunto_A)
    acumulado = Z_A | Z_B
    return acumulado

def caminho_para_alvo_em_Z_dois_sentidos(conjunto_A, conjunto_B, alvo):
    p1 = conjunto_A
    p2 = conjunto_B
    res = 0
    valor = alvo
    if(valor not in p1 or valor not in p2):
        for i in p2:
            if i == 1:
                continue
            res = caminho_para_alvo_em_n_somas(p1, i, valor)
            if(res != False):
                break
        if(res == False):      
            for j in p1:
                if j == 1:
                    continue
                res = caminho_para_alvo_em_n_somas(p2, j, valor)
                if(res != False):
                    break
        if(res == False):
            print("Não há esta soma")
        else:
            res.sort()
            for i in range(len(res)):
                res[i] = p1[res[i]]
            texto = ' + '.join(map(str, res))
            print(f'{texto} = {valor}')
    else:
        print(valor)

def Z_n_fatores(conjunto, n):
    if n > 1:
        return Z(conjunto, [n]) - set(conjunto)
    else:
        return set(conjunto)

