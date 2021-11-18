
"""
Riprendi il programma scritto nell'esercizio 15 dove l'utente può
indovinare cerca di indovinare un numero. Modificalo in modo che:
- La logica per controllare se ha indovinato sia in una funzione
- La funzione deve:
    - Stampare messaggi di aiuto all'utente in caso il numero sia troppo basso o troppo alto
    - Restituire True se l'utente indovina, False, altrimenti
    - Essere documentata con una docstring
- L'utente può tentare un numero illimitato di volte

"""

number = 23


def guess(n):
    """
    Dato n, restituisce True se n è uguale a number.

    La funzione stampa aiuti in caso il numero sia sbagliato,
    dicendo all'utente se deve provare un po' più in alto o
    un po' più in basso.

    Parametri:
    n: un numero

    Restituisce:
    Un boolean, True se n == number, False altrimenti.
    """
    if n == number:
        return True
    else:
        if n < number:
            print('No, un po\' più alto!')
        else:
            print('No, un po\' più basso!')
        return False


while True:
    n = int(input('Inserisci un intero: '))
    if guess(n):
        print('Congratulazioni, hai indovinato!')
        break
