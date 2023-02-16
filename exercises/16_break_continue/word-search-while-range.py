text = input("Inserisci un testo di più parole: ")
wordToSearch = input("Inserisci una parola da cercare nel testo: ")

words = text.split()
found = False
foundWordIndex = None  # vuoto...

i = 0
while i < len(words):
    word = words[i]
    print(f"Parola numero {i} del testo:", word)

    if word == wordToSearch:
        found = True
        foundWordIndex = i
        # Se volessi uscire ora uso l'istruzione break, come segue:
        # break
        # è come exit, ma invece che chiudere il programma, chiude il ciclo / esce dal ciclo

    i += 1


if found == True:
    print("Ho trovato la parola che cercavi!")
    print(f"Era la parola numero {foundWordIndex + 1}")
else:
    print("Non ho trovato la parola che cercavi.")
