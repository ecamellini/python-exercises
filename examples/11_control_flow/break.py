"""
Esempio di break in un ciclo while.
"""

while True:
    s = input('Inserisci qualcosa: ')
    if s == 'esci':
        break
    print('La lunghezza della stringa inserita è', len(s))

print('Fine!')
