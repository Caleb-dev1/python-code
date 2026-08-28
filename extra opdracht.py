import random
game = input  ("welke game wil je spelen?\nRaad het nummer\nKop of munt\nDobbelstene spel\nsteen papier schaar\nQuiz\nwat wil je spel? ")
if game == "Raad het nummer":
    while True:
        getal = random.randint(1, 100)
        poging = 0  ### ik heb dit hier gedaan want dan begin je bij 0 pogning en je heb maar 5 keer de kans

        while poging < 5:
            raden = int(input("Raad het getal tussen 1 en 100: "))
            poging += 1
            if raden > getal:
                print("lager")
            elif raden < getal:
                print("hoger")
            else:
                print("goed gedaan je hebt het")
                break
        else:
            print("helaas pindakaas volgende keer beter het getal was", getal)

        alweer = input("wil je alweer spelen? ja/nee ")
        if alweer == "ja":
            continue  ### als je ja zegt laat dit de loop door gaan
        elif alweer == "nee":
            break  ### dit laat de loop stoppen
elif game == "Kop of munt":
    while True:
        geluk = random.choice(["kop", "munt"])
        raden = input("kop of munt: ")
        if raden == geluk:
            print("goed gedaan")
        else:
            print("niet goed helaas je bent slecht in dit zeg")

        alweer = input("wil je alweer spelen ja/nee? ")
        if alweer == "ja":
            continue
        elif alweer  == "nee":
            break

elif game == "Dobbelstene spel":
    aantal_zijdens = int(input("hoeveel zijdens zijn er "))
    zijdens = random.randint(1, aantal_zijdens)
    worp = print("het rolt", zijdens)

elif game == "Steen papier schaar":
    while True:
        robot = random.choice(["steen", "papier", "schaar"])
        keuze = input("steen, papier, schaar: ")
        if robot == "schaar" and keuze == "papier":
            print("WOPM WOPM je hebt verloren")
        elif robot == "steen" and keuze == "schaar":
            print("WOPM WOPM je hebt verloren")
        elif robot == "papier" and keuze == "steen":
            print("WOPM WOPM je hebt verloren")
        elif robot == "schaar" and keuze == "steen":
            print("goed gedaan je hebt op een ene van de mannier gewonnen ")
        elif robot == "steen" and keuze == "papier":
            print("goed gedaan je hebt op een ene van de mannier gewonnen ")
        elif robot == "schaar" and keuze == "steen":
            print("goed gedaan je hebt op een ene van de mannier gewonnen ")
        elif robot == "papier" and keuze == "schaar":
            print("goed gedaan je hebt op een ene van de mannier gewonnen ")
        elif robot == keuze:
            print("gelijk spel")

        alweer = input("wil je alweer spelen? ja/nee ")
        if alweer == "ja":
            continue
        elif alweer == "nee":
            break
elif game == "Quiz":
    vraag1 = input("wat is deze programma ")
    vraag2 = input("wat is de hoofdstad van Nederlan ")
    vraag3 = input("waar ligt newyork ")

    antwoord1 = "Python"
    antwoord2 = "Amsterdam"
    antwoord3 = "VS"
    score = 0

    if vraag1 == antwoord1:
        print("je hebt goed")
        score += 1
    else:
        print("je hebt het fout")

    if vraag2 == antwoord2:
        print("je hebt goed")
        score += 1
    else:
        print("je hebt het fout")

    if vraag3 == antwoord3:
        print("je hebt goed")
        score += 1

    else:
        print("je hebt het fout")

    print("jouw score is", score)
