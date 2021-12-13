zoo = ('pitone', 'elefante', 'pinguino')
print(zoo)  # stampa { 'pitone', 'elefante', 'pinguino' }
print('Numero di animali nello zoo:', len(zoo))

new_zoo = ('scimmia', 'cammello', zoo)
# stampa { 'scimmia', 'cammello', ('pitone', 'elefante', 'pinguino') }
print(new_zoo)

print('Animali nel nuovo zoo:', new_zoo)
print('Animali portati dal vecchio zoo:', new_zoo[2])
print('Ultimo animale portato dal vecchio zoo:', new_zoo[2][2])
print('Numero di animali nello zoo:',
      len(new_zoo)-1+len(new_zoo[2]))
