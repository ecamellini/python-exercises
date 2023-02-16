"""
Programma per l'inventario di una biblioteca.
Per ogni libro, salviamo solo il titolo.
Il codice del libro è il suo indice nel catalogo.
Cioè: il primo libro ha codice 0, il non libro ha codice 8.

Deve permettere all'utente di:
1. Visualizzare una lista dei libri presenti
2. Inserire un nuovo libro
3. Dato il codice di un libro, stampane il titolo
4. Dato il codice di un libro, aggiornane il titolo
"""


libro = {
    "titolo": "Il Signore degli Anelli",
    "anno": 1912,
    "inCatalogo": 3,
    "autore": "Tolkien"
}

titolo = libro['titolo']
print(f"Il titolo del libro è: {titolo}")

libro["inCatalogo"] += 1
libro["anno"] = 1910


booksCatalogue = [
    {
        "titolo": "Il Signore degli Anelli",
        "anno": 1912,
        "inCatalogo": 3,
        "autore": "Tolkien"
    },
    {
        "titolo": "2000 Leghe Sotto I Mari",
        "anno": 1850,
        "inCatalogo": 6,
        "autore": "Jules Verne"
    },
]

print("Il titolo del primo libro in catalogo è:")
print(booksCatalogue[1]["titolo"])

# OPPURE

primoLibro = booksCatalogue[0]
titoloPrimoLibro = primoLibro['titolo']
print(titoloPrimoLibro)


# AGGIUNGERE UN LIBRO AL CATALOGO

titolo = input("Inserisci il titolo del libro: ")
autore = input("Inserisci l'autore: ")
anno = int(input("Inserisci l'anno in cui è stato scritto: "))

libroDaAggiungere = {
    "titolo": titolo,
    "anno": anno,
    "autore": autore,
    "inCatalogo": 1
}


booksCatalogue.append(libroDaAggiungere)
