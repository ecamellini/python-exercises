"""
Chiede all'utente di inserire la sua età e stampa un messaggio
"Maggiorenne" se l'età è maggiore di 18 anni, altrimenti stampa "Minorenne".
"""

age = int(input("Inserisci la tua età: "))

if age < 18:
    print("Minorenne")
else:
    print("Maggiorenne")
