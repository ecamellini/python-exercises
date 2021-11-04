"""
Placeholder più avanzati.
"""

# float (.) con precisione di 3 cifre dopo lo 0
# Stampa: 0.333 invece di 0.3333333333333333
print('{0:.3f}'.format(1.0/3))
print(f'{1.0/3:.3f}')

# circonda la stringa di tratti bassi (_) fino ad arrivare a una lunghezza di 11
# Stampa: '___hello___' invece di 'hello'
print('{0:_^11}'.format('hello'))
print(f'{"hello":_^11}')
