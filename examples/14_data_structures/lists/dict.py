
rubrica = {
    'Eric': 'eric@example.com',
    'Pippo': 'pippo@example.com',
    'Pluto': 'pluto@example.com',
}
print(rubrica)
print()

print("L'email di Eric è: ", rubrica['Eric'])

print("Aggiungo John: ")
rubrica['John'] = 'john@example.com'
print(rubrica)
print()

print("Cancello Pluto:")
del rubrica['Pluto']
print(rubrica)
print()

print(f'Ci sono {len(rubrica)} contatti nella rubrica')

for name, email in rubrica.items():
    print(f'Contatto {name} : email {email}')

print()

contatto = input("Inserisci il nome del contatto da stampare: ")
if contatto in rubrica:
    print(f"Indirizzo di {contatto}:", rubrica[contatto])
else:
    print("Contatto non trovato.")
