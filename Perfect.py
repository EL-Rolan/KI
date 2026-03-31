import numpy as np

'''
data = np.loadtxt("data.txt", delimiter=",", skiprows=1)

x = data[:, 0]  # время или частота
y = data[:, 1]  # сигнал / амплитуда / мощность'''

# Базисные состояния
zero = np.array([1, 0])
one = np.array([0, 1])

# Тензорное произведение
def kron(*args):
    result = args[0]
    for op in args[1:]:
        result = np.kron(result, op)
    return result

# Гейт Адамара
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

# Единичная матрица
I = np.eye(2)

# Начальное состояние |000>
psi0 = kron(zero, zero, zero)

# Адамар на первый кубит
H1 = kron(H, I, I)
psi1 = H1 @ psi0

# CNOT (0 -> 1)
CNOT_01 = np.array([
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,0]])

# CNOT (0 -> 2)
CNOT_02 = np.array([
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,1,0,0,0,0]])

# Применяем гейты
psi2 = CNOT_01 @ psi1
psi3 = CNOT_02 @ psi2

# Матрица плотности GHZ
rho = np.outer(psi3, psi3.conj())

print("GHZ state vector:")
print(psi3)

print("\nDensity matrix:")
print(rho)