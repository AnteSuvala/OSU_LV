import numpy as np
import matplotlib.pyplot as plt

# Dimenzije jednog kvadrata
size = 50

# Kreiranje crnog (0) i bijelog (1) kvadrata
black = np.zeros((size, size))
white = np.ones((size, size))

# Kombiniranje kvadrata u 2x2 matricu
bottom = np.hstack((white, black))
top = np.hstack((black, white))
image = np.vstack((bottom, top))

# Prikaz slike s gridom
plt.imshow(image, cmap='gray', extent=[0, 100, 0, 100])  # extent za postavljanje osi
plt.grid(color='black', linestyle='-', linewidth=1)        # grid linije
plt.xticks(np.arange(0, 100, 50))  # x osi: 0,50,100
plt.yticks(np.arange(0, 100, 50))  # y osi: 0,50,100
plt.gca().invert_yaxis()           # obrni y os od 100 do 0
plt.show()