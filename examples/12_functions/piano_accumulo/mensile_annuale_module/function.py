def capitale_piano_accumulo(versamento_annuale):
    tasso = float(
        input("Inserisci il tasso di interesse: ")
    ) / 100
    durata = int(input('Inserisci la durata dell\'investimento: '))

    capitale_totale = versamento_annuale * (1 + tasso)
    for anno in range(1, durata):
        print(f"Capitale dopo {anno} anni: {capitale_totale:.2f}")
        capitale_totale = capitale_totale * (1 + tasso) + versamento_annuale

    print(f"Capitale finale dopo {durata} anni: {capitale_totale:.2f}")
