somma = 0

while somma <= 100:
    numero = int(input("Inserisci un numero: "))
    somma = somma + numero
    if (somma < 100):
        if (numero % 2 == 0):
            print('Pari')
        else:
            print('Dispari')
    else:
        print(f"La somma è: {somma}")
