import numpy as np

data = np.loadtxt("data.txt", delimiter=",", skiprows=1)

values = data[:, 1]
probs = values / np.sum(values)
rho = np.diag(probs) #vfnhbwf gkjnyjcnb

print("Вер-ть:")
print(probs)

print("\nМатрица:")
print(rho)

'''
amps = data[:, 1]
amps = amps[:8]
rho = np.outer(psi, psi.conj())'''