frutti = set(['pere', 'mele', 'banane', 'banane'])

print(frutti)  # stampa {'mele', 'pere', 'banane'}
print()

frutti.add('banane')
print("Ho aggiunto un elemento duplicato, ma il set non cambia.")
print(frutti)
print()

print("Posso scorrere un set usando for, come per le liste.")
for i in frutti:
    print(i)
