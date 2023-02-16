"""
Esercizio: ricerca elemento nella lista

1) Data una lista della spesa, l'utente inserisce un elemento da
   cercare e il programma gli dice se c'è o no. Stampa
   trovato se c'è, non trovato se non c'è.

2) Stessa cosa di sopra, ma dice anche in che posizione si trova
   nella lista.

2) Stessa cosa, ma conta quante volte l'elemento cercato compare e stampa il conto.

3) Ricerca free-text: l'utente inserisce una parola chiave, e il programma
   stampa tutti gli elementi che la contengono Esempio: se l'utente
   iserisce "patate" e nella lista ci sono "patate dolci" e
   "patate novelle" le stampa entrambe, se scrive "pa" le stampa entrambe
   e stampa anche "pasta"

NOTA:
- non si possono usare metodi delle liste come .count, .index, etc.
- non si può usare l'operatore IN per capire se item in list
    ...MA, si può usare IN sulle stringhe per risolvere il punto 3
"""

groceryList = ['Pere', 'Mele', 'Patate', 'Patate Dolci',
               'Patate Novelle', 'Mele', 'Biscotti', 'Pasta']


itemToSearch = input("Insersci un elemento da cercare: ")

# Se potessimo usare l'operatore IN:
# if item in groceryList:
#     print("L'elemento c'è!")
# else:
#     print("L'elemento non c'è")

found = False

for item in groceryList:
    if item == itemToSearch:
        found = True
        break

if found == True:
    print("L'elemento è nella lista.")
else:
    print("L'elemento non c'è")


itemToSearch = input("Insersci un elemento di cui vuoi sapere l'indice : ")
indexOfItemToSearch = None
index = 0
for item in groceryList:
    if item == itemToSearch:
        indexOfItemToSearch = index
        break
    index += 1

if indexOfItemToSearch != None:
    print(f"L'elemento è in posizione {indexOfItemToSearch}")
else:
    print("L'elemento non c'è")


itemToSearch = input("Insersci un elemento da contare: ")
counter = 0

for item in groceryList:
    if item == itemToSearch:
        counter += 1

if counter > 0:
    print(f"L'elemento compare {counter} volte nella lista")
else:
    print("L'elemento non c'è")


wordToSearch = input("Insersci una parola da cercare: ")
found = False

for item in groceryList:
    if wordToSearch in item:
        print(item)
        found = True  # trovato almeno 1

if not found:
    print("Nessun risultato trovato")
