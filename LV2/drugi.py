import numpy as np
import matplotlib.pyplot as plt

# Učitavanje podataka iz csv datoteke
data = np.loadtxt("lv2/data.csv", delimiter=",", skiprows=1)

spol = data[:, 0]      # 0 = žensko, 1 = muško
visina = data[:, 1]    # visina u cm
masa = data[:, 2]      # masa u kg


#prvi


print(len(data)) # 10 000


# drugi
# plt.scatter(visina, masa)

# plt.xlabel("Visina (cm)")
# plt.ylabel("Masa (kg)")
# plt.title("Visina vs Masa")

# plt.grid(True)
# plt.show()

# treci
plt.scatter(visina[::50], masa[::50])

plt.xlabel("Visina (cm)")
plt.ylabel("Masa (kg)")
plt.title("Visina vs Masa")

plt.grid(True)
plt.show()


#cetvrti

print(max(visina))
print(min(visina))
print(np.mean(visina))


#peti

ind_m = (data[:,0] == 1)

visina_m = data[ind_m, 1]

print("Muškarci:")
print("Min:", np.min(visina_m))
print("Max:", np.max(visina_m))
print("Mean:", np.mean(visina_m))

ind_z = (data[:,0] == 0)

visina_z = data[ind_z, 1]

print("Žene:")
print("Min:", np.min(visina_z))
print("Max:", np.max(visina_z))
print("Mean:", np.mean(visina_z))