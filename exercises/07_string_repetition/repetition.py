"""
Scrivi un programma che:
- Legge una stringa e un numero N dall'utente
- Stampa la stringa N volte, per 3 righe
- Facoltativo: riscrivi il programma usando la scorciatoia operazione+assegnamento

Esempio: se l'utente inserisce 🌲 e 4 il programma stampa
🌲🌲🌲🌲
🌲🌲🌲🌲
🌲🌲🌲🌲
"""

s = input("Inserisci una stringa: ")
n = int(input("Inserisci un numero: "))

s *= n  # senza usare la scorciatoia *= posso direttamente stampare 3 volte la stringa s * n
print(s)
print(s)
print(s)

# Altre soluzioni
print(f"""{s}
{s}
{s}""")


print(f"{s}\n{s}\n{s}")
