import random

nombreMystere = random.randint(1,100)
essais = 0
essaisMax = 15

while essais != essaisMax:
    entree = input("Veuillez saisir un nombre compris entre 1 et 100\n")
    essais = essais + 1
    if entree.isdigit():
        nombre = int(entree)
        if nombre == nombreMystere:
            print("Vous avez gagné")
            break
        else:
            if essais == essaisMax:
                print("Vous avez perdu")
            else:
                if nombre < nombreMystere:
                    print("Le nombre mystère est plus grand")
                else:
                    print("Le nombre mystère est plus petit")