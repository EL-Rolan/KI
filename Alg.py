import numpy as np
import matplotlib.pyplot as plt

# ===== 1. загрузка =====
data = np.loadtxt("variant_4.txt")
t = data[:, 0]
y = data[:, 1]

N = len(y)
dt = t[1] - t[0]          # шаг по времени

# ===== 2. убираем среднее =====
y0 = y - np.mean(y)

# ===== 3. БПФ =====
Y = np.fft.rfft(y0)
freqs = np.fft.rfftfreq(N, d=dt)

# игнорируем нулевую частоту
idx = np.argmax(np.abs(Y[1:])) + 1
f = freqs[idx]
T = 1 / f

# ===== 4. амплитуда =====
A = 2 * np.abs(Y[idx]) / N

# ===== 5. восстановление =====
y_fit = A * np.sin(2 * np.pi * f * t)

# ===== 6. шум =====
noise = y0 - y_fit
sigma = np.std(noise)

# ===== 7. вывод =====
print(f"A = {A:.3f}")
print(f"f = {f:.6f} Гц")
print(f"T = {T:.3f}")
print(f"σ = {sigma:.3f}")

# ===== 8. график =====
plt.figure(figsize=(10, 5))
plt.scatter(t, y0, s=8, label="данные")
plt.plot(t, y_fit, 'r', lw=2, label="подгон")
plt.title(f"f_freq = {f:.6f} Гц, A = {A:.3f}, σ = {sigma:.3f}, T = {T:.3f}")
plt.legend()
plt.grid()
plt.show()
