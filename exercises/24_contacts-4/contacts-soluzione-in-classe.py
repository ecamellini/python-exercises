# Esempio
# contatti = {
#     "Eric": {
#         "email": "eric@asd.com",
#         "telefono": "123123123"
#     }
# }

# Esempio: se volessi stampare l'email
# print(contatti["Eric"]['email'])

# Esempio di read:
# contatto_da_stampare = contatti['Eric']


contatti = {}


def create_contact():
    nome = input("Inserisci il nome: ")
    telefono = input("Inserisci il telefono: ")
    email = input("Inserisci l'email: ")

    contatti[nome] = {
        "email": email,
        "telefono": telefono
    }


def print_contact(nome):
    email = contatti[nome]['email']
    telefono = contatti[nome]['telefono']
    print(f"Email di {nome}: {email}")
    print(f"Telefono di {nome}: {telefono}")


def read_contact():
    nome = input("Inserisci il nome del contatto da cercare: ")

    if nome in contatti:
        print_contact(nome)
    else:
        print("Contatto non trovato")


def read_all_contacts():
    for nome in contatti:
        print_contact(nome)


def search_contact():
    stringa_da_cercare = input("Inserisci un a chiave di ricerca: ")
    for nome in contatti:
        email = contatti[nome]['email']
        telefono = contatti[nome]['telefono']

        stringa_in_nome = stringa_da_cercare.lower() in nome.lower()
        stringa_in_email = stringa_da_cercare.lower() in email.lower()
        stringa_in_telefono = stringa_da_cercare.lower() in telefono.lower()

        if (stringa_in_nome or stringa_in_email or stringa_in_telefono):
            print_contact(nome)


while True:
    comando = input("Inserisci il comando: ")

    if comando == "create":
        create_contact()
    elif comando == "read":
        read_contact()
    elif comando == "read_all":
        read_all_contacts()
    elif comando == "search":
        search_contact()
    elif comando == "exit":
        break
    else:
        print("Comando non supportato.")

    print()
    print("--------------------------------------------------")
    print()

print("Programma terminato - tutti i tuoi contatti andranno persi.")
