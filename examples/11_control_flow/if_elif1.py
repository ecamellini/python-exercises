"""
Chiede all'utente di inserire un numero intero e verifica se l'utente indovina
correttamente il numero definito nel codice.
"""

numero = 23
tentativo = int(input('Inserisci un intero: '))

if tentativo == numero:
    # If-block
    print('Congratulazioni, hai indovinato!')
    print('Ma non ci sono premi in palio :)')
    # Fine if-block
elif tentativo < numero:
    # If-block
    print('No, un po\' più alto!')
    # Puoi eseguire il codice che vuoi in ogni blocco
else:
    print('No, un po\' più basso!')
    # devi aver inserito un numero maggiore per arrivare qua

print('Fine!')  # Questo ultimo statement viene sempre eseguito
