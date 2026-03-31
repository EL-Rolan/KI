import matplotlib.pyplot as plt

lines = np.loadtxt("variant_4.txt")

t = []
x = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith("#"):
        continue

    parts = line.split()
    if len(parts) < 2:
        continue

    try:
        t.append(float(parts[0]))
        x.append(float(parts[1]))
    except ValueError:
        # строка не содержит чисел — пропускаем
        continue

# --- Строим график ---
plt.plot(t, x)
plt.xlabel("Время (с)")
plt.ylabel("Сигнал")
plt.grid()
plt.show()
