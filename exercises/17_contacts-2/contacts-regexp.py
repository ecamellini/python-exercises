import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


while True:
    comando = input("Inserisci un comando: ").lower()

    if comando == "create":
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        telefono = input("Telefono: ")
        email = input("Email: ")
        while not re.fullmatch(regex, email):
            email = input("Email non valida. Inserisci una nuova email: ")
    elif comando == "read":
        print("Dettagli contatto:")
        print(nome)
        print(cognome)
        print(email)
        print(telefono)
    elif comando == "exit":
        exit()
    else:
        print("Operazione non consentita, riprova.")

    print("--------------------------------------")
