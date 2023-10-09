import numpy as np

# Criar vetores
vetor1 = np.array([1, 2, 3])
vetor2 = np.array([4, 5, 6])

# Adição de vetores
soma = vetor1 + vetor2

# Produto escalar
produto_escalar = np.dot(vetor1, vetor2)

# Produto vetorial
produto_vetorial = np.cross(vetor1, vetor2)

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Soma:", soma)
print("Produto Escalar:", produto_escalar)
print("Produto Vetorial:", produto_vetorial)
