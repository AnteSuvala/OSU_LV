ham_broj = 0
spam_broj = 0
ham_rijeci = 0
spam_rijeci = 0
spam_usklicnik = 0

with open("SMSSpamCollection.txt", "r", encoding="utf-8") as datoteka:
    for red in datoteka:
        red = red.strip()
        tip, poruka = red.split("\t", 1)

        broj_rijeci = len(poruka.split())

        if tip == "ham":
            ham_broj += 1
            ham_rijeci += broj_rijeci
        elif tip == "spam":
            spam_broj += 1
            spam_rijeci += broj_rijeci
            if poruka.endswith("!"):
                spam_usklicnik += 1

prosjek_ham = ham_rijeci / ham_broj
prosjek_spam = spam_rijeci / spam_broj

print("Prosječan broj riječi u ham porukama:", prosjek_ham)
print("Prosječan broj riječi u spam porukama:", prosjek_spam)
print("Broj spam poruka koje završavaju uskličnikom:", spam_usklicnik)