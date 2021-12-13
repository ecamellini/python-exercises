contact_name = ""
contact_surname = ""
contact_phone = ""
contact_email = ""


def input_contact():
    global contact_name
    global contact_surname
    global contact_phone
    global contact_email
    print("Inserisci i dettagli del contatto da salvare:")
    contact_name = input("Name: ")
    contact_surname = input("Surname: ")
    contact_phone = input("Phone: ")
    contact_email = input("Email: ")


def print_contact():
    print("\nContatto:")
    print("Nome: " + contact_name)
    print("Cognome: " + contact_surname)
    print("Telefono: " + contact_phone)
    print("Email: " + contact_email)
