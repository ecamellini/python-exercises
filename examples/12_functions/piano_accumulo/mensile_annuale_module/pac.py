# Piano di accumulo

from function import capitale_piano_accumulo

versamento_annuale_o_mensile = input(
    "Vuoi inserire un versamento annuale o mensile? ")

if versamento_annuale_o_mensile == "annuale":
    versamento_annuale = float(input("Inserisci il versamento annuale: "))
    capitale_piano_accumulo(versamento_annuale=versamento_annuale)
elif versamento_annuale_o_mensile == "mensile":
    versamento_mensile = float(input("Inserisci il versamento mensile: "))
    capitale_piano_accumulo(versamento_annuale=versamento_mensile * 12)
else:
    print("Comando non riconosciuto.")
