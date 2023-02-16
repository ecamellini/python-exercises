
lang = input("Inserisci la lingua del programma: ")

if lang == "IT":
    print("Buongiorno!")
else:
    if lang == "EN":
        print("good morning")
    else:
        if lang == "FR":
            print("Bonjour")
        else:
            if lang == "ES":
                print("Buen dia!")
            else:
                print("Lingua non supportata.")


if lang == "IT":
    print("Buongiorno!")
elif lang == "EN":
    print("good morning")
elif lang == "FR":
    print("Bonjour")
else:
    if lang == "ES":
        print("Buen dia!")
    elif lang == "PT":
        print("Buen dia!")
    else:
        print("Lingua non supportata.")
