import json

classi = {
    "prima": [
        {
            "nome": "Paolo",
            "cognome": "Rossi"
        },
        {
            "nome": "Paolo",
            "cognome": "Bianchi"
        },
        {
            "nome": "Pippo",
            "cognome": "Verdi"
        }
    ],
    "seconda": [
        {
            "Nome": "Giuseppe",
            "Cognome": "Rossi"
        },
        {
            "Nome": "John",
            "Cognome": "Doe"
        },
        {
            "Nome": "Jack",
            "Cognome": "White"
        }
    ]
}


with open('classi.json', 'w') as f:
    # Salvare un dizionario in un file JSON
    json.dump(classi, f)


classi.clear()  # Svuoto il dizionario
print(classi)  # Stampa {}

with open('classi.json', 'r') as f:
    # Leggere un dizionario da un file JSON
    classi = json.load(f)

print(classi)  # Il dizionario contiene di nuovo i dati iniziali
