def hasGuessed(guess, numberToGuess):
    """
    Questa funzione prende guess come parametro, un numero,
    e numberToGuess, un numero da indovinare, e restituisce:
    - 0 se l'utente ha indovinato il random generato dal programma
    - -1 se il numero inserito è più basso
    - +1 se il numero inserito è più in alto
    """
    if guess == numberToGuess:
        return 0
    else:
        if guess < numberToGuess:
            return -1
        else:
            return +1
