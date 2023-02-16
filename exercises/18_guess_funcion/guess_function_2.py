from random import random

numberToGuess = round(random() * 10)


def hasGuessed(guess):
    if guess == numberToGuess:
        return True
    else:
        if guess < numberToGuess:
            print("Prova più in alto")
        else:
            print("Prova più in basso")

        return False


while True:
    guessInput = int(input('Inserisci un numero tra 0 e 10: '))
    if hasGuessed(guessInput):
        print("Hai indovinato 🎉")
        break

# print(hasGuessed(0))
# print(hasGuessed(1))
# print(hasGuessed(2))
# print(hasGuessed(3))
# print(hasGuessed(4))
# print(hasGuessed(5))
# print(hasGuessed(6))
# print(hasGuessed(7))
# print(hasGuessed(8))
# print(hasGuessed(9))
# print(hasGuessed(10))
