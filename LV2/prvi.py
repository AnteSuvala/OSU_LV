import numpy as np
import matplotlib.pyplot as plt

# Koordinate točaka
x = np.array([1, 2, 3, 3])
y = np.array([1, 2, 2, 1])

# Zatvaranje četverokuta (dodamo prvu točku na kraj)
x = np.append(x, x[0])
y = np.append(y, y[0])

# Crtanje
plt.plot(x, y, marker='o', color='red')

# Mreža i osi
plt.grid(True)
plt.axis([0,4,0,4])
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.title("Četverokut na koordinatnom sustavu")
plt.show()