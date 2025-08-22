from algoritmos import *

"""
Nesse primeiro código, recebe-se um input e tenta-se achar o alvo esperado em um conjunto iterado em
n somas de minkowski, caso queira procurar por -1, fecha-se a execucao
"""

p1 = [1, 20, 150, 1000, 10000]
print('Conjunto {}'.format(p1))
n = int(input('Numero de repeticoes: '))

if n < 1:
    print('Numero de repeticoes invalido')
else:
    while True:
        valor = int(input('Alvo: '))
        if valor == -1:
            print('Execucao encerrada ...')
            break
        res = caminho_para_alvo_em_n_somas(p1, n, valor)
        if res == False:
            print("não é possível")
        else:
            res.sort()
            for i in range(0, len(res)):
                res[i] = p1[res[i]]
            texto = ' + '.join(map(str, res))
            print(f'{texto} = {valor}')
