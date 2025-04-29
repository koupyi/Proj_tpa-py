import numpy as np

matriz = np.zeros((4, 5))

for i in range(4):
    for j in range(5):
        matriz[i, j] = int(input(f"Valores ({i+1},{j+1}): "))

soma_linhas = np.sum(matriz, axis=1)

print(soma_linhas)
