from random import randint

# on initialise les pv
vous = 50
ennemi = 50
# on initialise le nombre de potions de départ
potions = 3
# on utilisera un toogle qui permettra de savoir si une potion a été utilisé au tour suivant
using_potion = 0

# définition des fonctions d'attaque et de potions
def usePotion(vous, using_potion, potions):
    heal = randint(15,50)
    vous += int(heal)
    potions -= 1
    print(f"Vous utilisez une potion 🧪 ")
    print(f"Vous avez récupèré {heal} points de vie ❤️ ")
    print(f"Il vous reste {vous} points de vie.")
    print(f"Il reste {ennemi} points de vie à l'ennemi.")
    using_potion = 1
    return vous, using_potion, potions
        
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
def userAction(choice, vous, ennemi, using_potion, potions):
    if choice == 1:
        ennemi = vousAttaquez(ennemi)
    elif choice == 2:
           
        vous, using_potion, potions = usePotion(vous, using_potion, potions)
    return vous, ennemi, using_potion, potions  
     
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
        if choice == "2" and potions == 0:
            print("vous n'avez plus de potions")
            continue
        else: 
            vous, ennemi, using_potion, potions = userAction(int(choice), vous, ennemi, using_potion, potions)
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