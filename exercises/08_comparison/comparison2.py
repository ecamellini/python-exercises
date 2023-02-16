x = int(input('Inserisci il primo numero: '))
y = int(input('Inserisci il secondo numero: '))

isXGreater = x > y
print(f"Il primo è maggiore: {isXGreater}")


print(f"Il primo numero è pari: {(x % 2) == 0}")

# SOLUZIONE PIÙ LUNGA:
# modulo = x % 2
# print(f"Resto divisione per 2: {modulo}")
# isXEven = modulo == 0
# print(f"Il primo numero è pari: {isXEven}")


isXOdd = x % 2 == 1  # 1* modo di chiederci se X è dispari
isXOdd = x % 2 != 0  # Altro modo di chiederci se X è dispari
isXOdd = not (x % 2 == 0)

if isXOdd:
    print("X è dispari.")
else:
    print("X è pari.")
