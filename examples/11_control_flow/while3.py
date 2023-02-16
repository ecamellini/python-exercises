import random

numberToGuess = round(random.random() * 10)
hasGuessed = False

while (not hasGuessed):
    guess = int(input("Inserisci un numero: "))

    if guess == numberToGuess:
        print("Congratulazioni! Hai indovinato 🎉")
        hasGuessed = True
    elif guess < numberToGuess:
        print("Prova più in alto!")
    else:
        print("Prova più in basso!")

print("Fine!")
