import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread("lv2/road.jpg")

plt.imshow(img)
plt.title("Original")
plt.axis("off")
plt.show()


# Ako je uint8, pretvori u float 0-1
if img.dtype == np.uint8:
    img = img / 255.0

# Posvjetljivanje
factor = 2
img_light = np.clip(img * factor, 0, 1)

plt.imshow(img_light)


plt.imshow(img_light)
plt.title("Posvijetljena slika")
plt.axis("off")
plt.show()

visina, sirina, kanali = img.shape

img_quarter = img[:, sirina//4 : sirina//2]

plt.imshow(img_quarter)
plt.title("Druga četvrtina")
plt.axis("off")
plt.show()


img_rot = np.rot90(img, -1)

plt.imshow(img_rot)
plt.title("Rotacija 90°")
plt.axis("off")
plt.show()


img_mirror = np.fliplr(img)

plt.imshow(img_mirror)
plt.title("Zrcaljena slika")
plt.axis("off")
plt.show()