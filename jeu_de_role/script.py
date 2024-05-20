from random import randint

# on initialise les pv
vous = 50
ennemi = 50
# on initialise le nombre de potions de départ
potions = 3
# on utilisera un toogle qui permettra de savoir si une potion a été utilisé au tour suivant
using_potion = 0

# définition des fonctions d'attaque et de potions
def usePotion(vous, using_potion):
    heal = randint(15,50)
    vous += int(heal)
    print(f"Vous utilisez une potion 🧪 ")
    print(f"Vous avez récupèré {heal} points de vie ❤️ ")
    print(f"Il vous reste {vous} points de vie.")
    print(f"Il reste {ennemi} points de vie à l'ennemi.")
    using_potion = 1
    return vous, using_potion
        
def vousAttaquez(ennemi):
    degats = randint(5,10)
    ennemi -= degats
    print(f"Vous infligez {degats} points de dégâts à l'ennemi.")
    print(f"Il reste {ennemi} points de vie à l'ennemi.")
    return ennemi
    
def ennemiAttaque(vous):
    degats = randint(5,15)
    vous -= degats
    print(f"Vous subissez {degats} points de dégâts.")
    print(f"Il vous reste {vous} points de vie.")
    return vous
    
# definition de la fonction de controle du choix
def userAction(choice, vous, ennemi, using_potion):
    if choice == 1:
        ennemi = vousAttaquez(ennemi)
    elif choice == 2:
        vous, using_potion = usePotion(vous, using_potion)
    return vous, ennemi, using_potion  
     
question = """Que voulez vous faire?
1 . Attaquer ⚔️ ?
2 . Prendre une potions 🧪 ? 
Votre décision => """
POSSIBLE_CHOICE = ["1", "2"]

# Start !
print("Le combat commence.")
while vous > 0 and ennemi > 0:
    # tour du joueur
    # print(f"using popo {using_potion}") # DEBUG POTION
    if using_potion:
        using_potion = 0
        print(r"Vous avez utilisé une potion le tour précédent, vous passez votre tour...")
    else:
        choice = input(question)
        if choice.isalpha() or choice not in POSSIBLE_CHOICE:
            print("Veuillez choisir un nombre valide.")
            continue
        vous, ennemi, using_potion = userAction(int(choice), vous, ennemi, using_potion)
    # tour ennemi
    if ennemi <= 0:
        break
    else:
        vous = ennemiAttaque(vous)
    # passage au tour suivant
    print(r"---------------------------------------------")
    
# Fin !
print("Le combat est terminé !")
if vous <= 0:
    print("Vous êtes mort ! ")
elif ennemi <= 0:
    print("L'ennemi est mort ! vous avez gagnez !!! 👑")