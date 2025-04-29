import numpy as np

matrizA = np.zeros((3, 5))
matrizB = np.zeros((3, 5))

for i in range(3):
    for j in range(5):
        matrizA[i, j] = int(input(f"Valores matriz A ({i+1},{j+1}): "))

for i in range(3):
    for j in range(5):
        matrizB[i, j] = int(input(f"Valores matriz B ({i+1},{j+1}): "))

soma_matrizes = matrizA + matrizB

print(soma_matrizes)