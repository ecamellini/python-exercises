"""
Chiede all'utente di inserire un numero intero e verifica se l'utente indovina
correttamente il numero definito nel codice.
Se l'utente non indovina, ripete la stessa logica, fino a un massimo di 5 tentativi.
Per ogni tentativo, stampa "Tentativo numero X".
Se i tentativi finiscono, stampa un messaggio che avverte l'utente di cosa è successo, prima di terminare.

>> Usiamo exit per uscire dal ciclo.
"""

number = 23

for i in range(5):
    print(f"Tentativo numero { i + 1 }")
    tentativo = int(input('Inserisci un intero: '))

    if tentativo == number:
        print('Congratulazioni, hai indovinato!')
        exit()
    elif tentativo < number:
        print('No, un po\' più alto!')
    else:
        print('No, un po\' più basso!')
else:
    print('Hai finito i tentativi.')

print('Fine programma!')
