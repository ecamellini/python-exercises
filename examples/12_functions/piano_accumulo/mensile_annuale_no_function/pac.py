# Piano di accumulo

versamento_annuale_o_mensile = input(
    "Vuoi inserire un versamento annuale o mensile? ")


if versamento_annuale_o_mensile == "annuale":
    # PROBLEMA: notiamo che il codice seguente è ripetuto uguale due volte
    # in entrambi i blocchi if e elif di questo programma.
    versamento_annuale = float(input("Inserisci il versamento annuale: "))
    tasso = float(
        input("Inserisci il tasso di interesse: ")
    ) / 100
    durata = int(input('Inserisci la durata dell\'investimento: '))

    capitale_totale = versamento_annuale * (1 + tasso)
    for anno in range(1, durata):
        print(f"Capitale dopo {anno} anni: {capitale_totale:.2f}")
        capitale_totale = capitale_totale * (1 + tasso) + versamento_annuale

    print(f"Capitale finale dopo {durata} anni: {capitale_totale:.2f}")

elif versamento_annuale_o_mensile == "mensile":
    versamento_mensile = float(input("Inserisci il versamento mensile: "))
    versamento_annuale = versamento_mensile * 12
    tasso = float(
        input("Inserisci il tasso di interesse: ")
    ) / 100
    durata = int(input('Inserisci la durata dell\'investimento: '))

    capitale_totale = versamento_annuale * (1 + tasso)
    for anno in range(1, durata):
        print(f"Capitale dopo {anno} anni: {capitale_totale:.2f}")
        capitale_totale = capitale_totale * (1 + tasso) + versamento_annuale

    print(f"Capitale finale dopo {durata} anni: {capitale_totale:.2f}")
else:
    print("Comando non riconosciuto.")
