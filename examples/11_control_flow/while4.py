import random

numberToGuess = round(random.random() * 10)
notGuessed = True
numberOfGuesses = 1

while notGuessed and numberOfGuesses <= 3:
    print(f"Tentativo numero {numberOfGuesses}")
    guess = int(input("Inserisci un numero: "))

    if guess == numberToGuess:
        print("Congratulazioni! Hai indovinato 🎉")
        notGuessed = False
    elif guess < numberToGuess:
        print("Prova più in alto!")
    else:
        print("Prova più in basso!")

    numberOfGuesses = numberOfGuesses + 1


print("Fine!")
