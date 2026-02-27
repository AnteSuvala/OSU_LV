import string

rijeci = {}

with open("song.txt", "r", encoding="utf-8") as datoteka:
    for red in datoteka:
        red = red.strip()
        rijeci_u_redu = red.split()

        for rijec in rijeci_u_redu:
            rijec = rijec.lower()

            rijec = rijec.strip(string.punctuation)

            rijeci[rijec] = rijeci.get(rijec, 0) + 1

jednom = [r for r, broj in rijeci.items() if broj == 1]
print(jednom)
# print("Broj riječi koje se pojavljuju samo jednom:", len(jednom))
# print("Te riječi su:")
for r in jednom:
    print(r)