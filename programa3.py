from algoritmos import *

"""
Executa a soma de minkowski nos dois sentidos entre dois conjuntos, ou seja, considerando cada elemento de um conjunto como potencias da 
soma de minkowski para o outro.
"""

A = [1, 2, 3, 4]
B = [1,2,7]

res = Z_dois_sentidos(A, B)
real = sorted(res)
print(f'{real}')
