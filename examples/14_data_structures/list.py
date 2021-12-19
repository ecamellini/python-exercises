frutti = ['pere', 'mele', 'banane']

print("Stampo gli elementi della lista uno ad uno:")
print(frutti[0])  # Stampa 'pere'
print(frutti[1])  # Stampa 'mele'
print(frutti[2])  # Stampa 'banane'
print()

print("Stampo gli elementi della lista con un for:")
for frutto in frutti:
    print(frutto)
print()


print(f"Lunghezza della lista: {len(frutti)}")
print()

# aggiungiamo un frutto
frutti.append('meloni')
print(frutti)
print(f"Ho aggiunto alla lista: {frutti[3]}")
print()

print(f"Elementi ordinati: ")
frutti.sort()
print(frutti)
print()

frutti.insert(1, 'mango')
print(frutti)
print()

frutti.remove('pere')
print("Ho cancellato 'pere'.")
print(frutti)
print()

del frutti[0]
print("Ho cancellato il primo elemento.")
print(frutti)
print()

frutti.clear()
print("Ho cancellato tutto.")
print(frutti)
print()

print("Aggiungo due volte albicocche - la lista ammette duplicati:")
frutti.append('albicocche')
frutti.append('albicocche')
print(frutti)
