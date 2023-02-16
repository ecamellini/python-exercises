N = int(input("Inserisci un numero: "))

# if N < 0:
#     # exit()
#     print("Fine programma!")
# elif N % 2 == 0:
#     print("Pari!")
# else:
#     print("Dispari!")

if N > 0:
    if N % 2 == 0:
        print("Pari")
    else:
        print("Dispari")
else:
    print("No, devi inserire un numero > 0")
    N = int(input("Inserisci un numero: "))

    if N > 0:
        if N % 2 == 0:
            print("Pari")
        else:
            print("Dispari")
    else:
        print("No, devi inserire un numero > 0")
        N = int(input("Inserisci un numero: "))

        if N > 0:
            if N % 2 == 0:
                print("Pari")
            else:
                print("Dispari")
