"""
Scrivi un programma che:
- Legge una frase, un testo, dall'utente
- Legge poi una parola dall'utente, parola da cercare nel testo
- Stampa una ad una le parole della frase inserita
- Se trova la parola da cercare, la stampa e termina il programma

"""

frase = input("Inserisci un testo: ")
parola_da_trovare = input("Inserisci una parola da cercare: ")

for parola in frase.split():
    print(parola)
    if parola == parola_da_trovare:
        break
    else:
        continue
