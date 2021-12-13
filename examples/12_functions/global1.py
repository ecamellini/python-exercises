nome_contatto = None
cognome_contatto = None


def salva_contatto(nome, cognome):
    # global è necessario, altrimenti non posso modificare variabili esterne a una funzione
    global nome_contatto
    global cognome_contatto
    nome_contatto = nome
    cognome_contatto = cognome


salva_contatto("Paolo", "Bianchi")
print(nome_contatto)
print(cognome_contatto)
