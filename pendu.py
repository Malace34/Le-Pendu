import random

dessins = [
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",  # 0 vie
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # 1 vie
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # 2 vies
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # 3 vies
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # 4 vies
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # 5 vies
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  # 6 vies
]

def afficher_mot(mot, lettres_trouvees):
    resultat = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            resultat += lettre + " "
        else:
            resultat += "_ "
    return resultat

def jouer():
    mots = ["python", "ordinateur", "clavier", "avion", "porte", "police", "table"]
    secret = random.choice(mots)
    lettres_trouvees = []
    lettres_proposees = []
    vies = 6

    while vies > 0:
        print(afficher_mot(secret, lettres_trouvees))
        print("Lettres proposées :", lettres_proposees)
        print("Vies restantes :", vies)
        print(dessins[vies])
        lettre = input("Propose une lettre : ").lower()

        if len(lettre) != 1:
            print("Vous devez entrer une seule lettre.")
            continue
        if lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre.")
            continue

        lettres_proposees.append(lettre)

        if lettre in secret:
            lettres_trouvees.append(lettre)
            if "_" not in afficher_mot(secret, lettres_trouvees):
                print("Bravo ! Le mot était", secret)
                return
        else:
            vies -= 1
            print(lettre, "n'est pas dans le mot.")
    print(dessins[0])
    print("Perdu ! Le mot était", secret)

rejouer = "oui"
while rejouer == "oui":
    jouer()
    rejouer = input("Veux-tu rejouer ? (oui/non) ").lower()
    
print("Merci d'avoir joué !")