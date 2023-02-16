from random import random
from guessUtilities import hasGuessed

randomNumber = round(random() * 10)
while True:
    guessInput = int(input('Inserisci un numero tra 0 e 10: '))
    result = hasGuessed(numberToGuess=randomNumber, guess=guessInput)
    if result == 0:
        print("Hai indovinato 🎉")
        break
    elif result == -1:
        print("Prova più in alto!")
    else:
        print("Prova più in basso!")


# # DIVERSE
# hasGuessed(2, 10)
# hasGuessed(10, 2)

# # UGUALI
# hasGuessed(guess=2, numberToGuess=10)
# hasGuessed(numberToGuess=10, guess=2)
