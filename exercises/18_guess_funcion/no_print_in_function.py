def controlla_tentativo(tentativo):
    """
    Dato un tentativo, controlla se è uguale al numero da indovinare.
    Se è uguale, restituisce "indovinato".
    Se è minore, restituisce "minore".
    Se è maggiore, restituisce "maggiore".
    """
    number = 23
    if tentativo == number:
        return "indovinato"
    elif tentativo < number:
        return "minore"
    else:
        return "maggiore"


while True:
    tentativo = int(input('Inserisci un intero: '))
    risultato = controlla_tentativo(tentativo=tentativo)
    if risultato == "indovinato":
        print('Congratulazioni, hai indovinato!')
        break
    elif risultato == "minore":
        print("Inserisci un numero più grande.")
    elif risultato == "maggiore":
        print("Inserisci un numero più basso.")

print('Fine!')
