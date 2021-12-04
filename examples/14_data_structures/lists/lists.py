frutti = ['pere', 'mele', 'banane', 'meloni', 'a', 'b', 'c', 'd', 'e']

print("Stampo il tipo della variabile che contiene la mia lista:")
print(type(frutti))  # Stampa 'list'

print("Stampo gli elementi della lista uno ad uno:")
print(frutti[0])  # Stampa 'pere'
print(frutti[1])  # Stampa 'mele'
print(frutti[2])  # Stampa 'banane'

print("Stampo gli elementi della lista con un for:")
for frutto in frutti:
    print(frutto)

print(f"Lunghezza della lista: {len(frutti)}")

# aggiungiamo un frutto
frutti.append('meloni')

print(f"Ho aggiunto alla lista: {frutti[3]}")
print(frutti)

print(f"Elementi ordinati: ")
frutti.sort()
print(frutti)

del frutti[0]
print("Ho cancellato il primo elemento.")
print(frutti)
