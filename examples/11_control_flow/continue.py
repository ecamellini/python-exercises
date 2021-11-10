"""
Esempio di break e continue in un ciclo while.
"""

while True:
    s = input('Inserisci qualcosa: ')
    if s == 'esci':
        break
    if len(s) < 3:
        print('Stringa troppo corta!')
        continue
    print('Stringa abbastanza lunga.')
    print('Infatti, è lunga', len(s))
