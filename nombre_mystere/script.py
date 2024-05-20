import random
import sys
# on initialise les valeurs limites
start = 0
end = 10
# on paramètre le nombre d'essais max
essai_max = 5
# on génère le nombre mystère
nombre_mystère = random.randint(start,end)
# on initialise la tentative à 1 (on ajoutera 1 à chaque échec)
i = 0
# print(nombre_mystère) # DEBUG
# on limit les essaies si on est au max sort du while
while i != essai_max:
    essai = input('A quel nombre pensez vous ? ')
    # on indique une erreur si ce n'est pas un digit
    if essai.isalpha() or not essai.isdigit():
        print(f"vous devez entrer un nombre compris entre {start} et {end}")
        continue
    # de même si c'est hors limites
    if (int(essai) < int(start)) or (int(essai) > int(end)):
        print(f"vous devez entrer un nombre compris entre {start} et {end}")
        continue
    else:
        # si c'est bon c'est gagné
        # print(f"essai numéro {i} valeur {essai}") # DEBUG
        if(int(essai) == int(nombre_mystère)):
            # on annonce le nombre d'essais
            print(f'bravo il vous a fallu {i+1} essai(s).')
            # on cut le script
            sys.exit()
        # sinon on indique si c'est plus grand ou plus petit et on ajoute 1 au nombre d'essais
        if(int(essai) > nombre_mystère):
            print("c'est moins")
        else:
            print("c'est plus")
        i+=1
        continue
# sinon on affiche que c'est perdu!
print('Vous avez perdu ! ')