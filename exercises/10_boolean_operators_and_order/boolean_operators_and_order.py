"""
Per un nuovo film, i casting sono aperti a chi ha i seguenti tratti:
- Meno di 20 anni, con capelli biondi o mori
- Più di 65 anni, con capelli grigi
- Qualsiasi età, con capelli lunghi e non castani
- Qualsiasi età, con capelli corti, purché siano biondi o mori

Scrivi un programma che:
- Chiede l'età all'utente
- Pone una serie di domande all'utente, alle quali può rispondere
- Ci dice se l'utente può partecipare al casting oppure no, stampando True o False
"""

età = int(input("Quanti anni hai? "))
colore_capelli = input("Di che colore sono i tuoi capelli? ")
capelli_lunghi = input("Hai i capelli lunghi? ").lower() == "sì"

capelli_mori = colore_capelli.lower() == "mori"
capelli_biondi = colore_capelli.lower() == "biondi"
capelli_castani = colore_capelli.lower() == "castani"
capelli_grigi = colore_capelli.lower() == "grigi"

condizione_1 = (età < 20) and (capelli_biondi or capelli_mori)
condizione_2 = (età > 65) and capelli_grigi
condizione_3 = capelli_lunghi and not capelli_castani
condizione_4 = not capelli_lunghi and (capelli_biondi or capelli_mori)

print("Puoi partecipare al casting:")
print(condizione_1 or condizione_2 or condizione_3 or condizione_4)
