import random

numberToGuess = round(random.random() * 10)
maxAttempt = 10

for attempt in range(1, maxAttempt + 1):
    print(f"Tentativo numero: {attempt}")
    guess = int(input("Inserisci un numero: "))

    if guess == numberToGuess:
        print("Congratulazioni! Hai indovinato 🎉")
        exit()
    elif attempt == maxAttempt:
        print("Hai esaurito i tentativi. Mi spiace :(")
    elif guess < numberToGuess:
        print("Prova più in alto!")
    else:
        print("Prova più in basso!")
