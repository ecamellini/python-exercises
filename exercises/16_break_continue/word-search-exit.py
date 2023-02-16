text = input("Inserisci una testo di più parole: ")
wordToSearch = input("Inserisci una parola da cercare nel testo: ")

words = text.split()

for word in words:
    print(word)
    if word == wordToSearch:
        exit()
