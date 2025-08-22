from algoritmos import *

"""
Considera um conjunto conj, e executa a soma iterada de minkowski em n fatores de conj e guarda esse 
valor no conjunto acumulado e exibe o conjunto e o numero de elementos que ele possui 
"""

conj = [1, 5, 25, 125, 625]
mult = int(input())

acumulado = Z_n_fatores(conj, mult)
real = sorted(acumulado)

print(f'{real} ')
print(f"total de elementos = {len(acumulado)}")

