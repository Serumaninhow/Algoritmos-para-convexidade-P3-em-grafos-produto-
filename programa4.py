from algoritmos import *

"""
Procura um valor na soma de minkowski nos dois sentidos, e mostra o caminho ate la
"""

conjunto_A = [1, 2]
conjunto_B = [1, 2, 7]

while True:
    alvo = int(input())
    if alvo == -1:
        break
    caminho_para_alvo_em_Z_dois_sentidos(conjunto_A, conjunto_B, alvo)
