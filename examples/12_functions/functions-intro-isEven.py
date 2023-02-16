

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


number1 = int(input("Inserisci un numero: "))
number2 = int(input("Inserisci un numero: "))
number3 = int(input("Inserisci un numero: "))


print("Il primo numero è pari: ", isEven(number1))
print("Il secondo numero è pari: ", isEven(number2))
print("Il terzo numero è pari: ", isEven(number3))
