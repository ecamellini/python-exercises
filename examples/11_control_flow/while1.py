"""
Chiede all'utente di inserire un numero intero e verifica se l'utente indovina
correttamente il numero definito nel codice.
Se l'utente non indovina, ripete la stessa logica.
"""

number = 23
continua = True

while continua:
    tentativo = int(input('Inserisci un intero: '))

    if tentativo == number:
        print('Congratulazioni, hai indovinato!')
        continua = False  # questo causerà un'uscita dal ciclo
    elif tentativo < number:
        print('No, un po\' più alto!')
    else:
        print('No, un po\' più basso!')

print('Fine!')
