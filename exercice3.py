import random

x = random.randint(1, 100)
essai = 7
print("on va jouer un petit jeux deviner le nombre que j`ai choisi")
while True:
    if essai > 0:
        guess = int(input("entrez votre nombre"))

        if guess == x:
            essai -= 1
            print(f"bravo {guess} est le nombre que j`ai choisi : {essai}")
            break
        elif guess > x:
            print("votre nombre est trop grand")
            essai -= 1
        elif guess < x:
            print("votre nombre est plus petit")
            essai -= 1
        elif guess < 0 or guess > 100:
            print("t`est hors intervalle")
            essai -= 1
    elif essai == 0:
        print(f"Game Over le nombre que j`ai choisi est {x} ")
        break
