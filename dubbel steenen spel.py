import random
speler1 = {
    "naam": input("Naam speler 1: "),
    "leeftijd": input("Leeftijd: "),
    "klas": input("Klas: "),
    "worpen": [],
    "gemiddelde": 0
}

antwoord = input("Speler 1 wil je rollen? (ja/nee): ").lower()

if antwoord == "ja":
    worp = []
    for i in range(3):
        zijdens = random.randint(1, 10)
        worp.append(zijdens)
        print("Worp", i + 1, "is:", zijdens)

    speler1["worpen"] = worp
    speler1["gemiddelde"] = sum(worp) / 3
else:
    print("Speler 1 heeft niet gerold.")
speler2 = {
    "naam": input("Naam: "),
    "leeftijd": input("Leeftijd: "),
    "klas": input("Klas: ")
}
if antwoord == "ja":
    worp = []
    for i in range (3):
        zijdens = random.randint(1, 10)
        worp.append(zijdens)
        print("Worp", i + 1, "is:", zijdens)
speler3 = {
    "naam": input("Naam: "),
    "leeftijd": input("Leeftijd: "),
    "klas": input("Klas: ")
}
if "ja":
    worp = []
    for i in range (3):
        zijdens = random.randint(1, 10)
        worp.append(zijdens)
        print("Worp", i + 1, "is:", zijdens)

