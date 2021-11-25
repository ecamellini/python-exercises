"""
Chiede all'utente di inserire un numero intero e verifica se l'utente indovina
correttamente il numero definito nel codice.
Se l'utente non indovina, ripete la stessa logica.
"""

number = 23
tentativo = 0

while tentativo != number:
    tentativo = int(input('Inserisci un intero: '))
    if tentativo == number:
        print('Congratulazioni, hai indovinato!')
    elif tentativo < number:
        print('No, un po\' più alto!')
    else:
        print('No, un po\' più basso!')

print('Fine!')
