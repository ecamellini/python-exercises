# I valori di tutte le strutture dati possono essere
# tutti i tipi di valori che Python supporta.
# Anche altre strutture dati!

# Esempi:

list_of_contacts = [
    {
        "name": "Eric",
        "email": "eric@example.com",
        "phone": "213123123"
    },
    {
        "name": "Pippo",
        "email": "pippo@example.com",
        "phone": "213123123"
    }
]


def search_by_name_list(name):
    # Per cercare in una lista sulla base del conenuto degli elementi
    # devo scorrere tutta la lista e controllarli uno per unoa
    for contact in list_of_contacts:
        if contact['name'] == name:
            return contact
    return None


print(search_by_name_list("Eric"))  # stampa i dettagli di Eric
print(search_by_name_list("Pippo"))  # stampa i dettagli di Pippo
print(search_by_name_list("Pluto"))  # stampa None


dictionary_of_contacts = {
    "Eric": {
        "email": "eric@example.com",
        "phone": "213123123"
    },
    "Pippo": {
        "email": "pippo@example.com",
        "phone": "213123123"
    }
}


def search_by_name_dict(name):
    # Qua mi basta usare la chiave del dizionario, non devo scorrere tutti gli elementi
    if name in dictionary_of_contacts:
        return dictionary_of_contacts[name]
    return None


print(search_by_name_dict("Eric"))  # stampa i dettagli di Eric
print(search_by_name_dict("Pippo"))  # stampa i dettagli di Pippo
print(search_by_name_dict("Pluto"))  # stampa None

# Liste di liste sono solitamente usate per rappresentare delle matrici!
# Ad esempio, in questa matrice ogni riga può rappresentare un utente
# e ogni colonna il voto che ha dato a un certo film.
user_ratings_matrix = [
    [1, 2, 4, 0],
    [1, 0, 5, 5],
    [3, 3, 4, 3]
]
