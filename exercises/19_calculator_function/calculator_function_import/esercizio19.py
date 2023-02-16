import operations

while True:
    operationString = input("Inserisci una operazione: ")

    if operationString == "exit":
        break

    operationStringSplit = operationString.split()

    if len(operationStringSplit) != 3:
        print("Input non valido: inserisci un'operazione con due operandi e operatore separati da spazio.")
        continue

    try:
        n1 = float(operationStringSplit[0])
        op = operationStringSplit[1]
        n2 = float(operationStringSplit[2])

        result = operations.executeOperation(
            operand1=n1, operator=op, operand2=n2)

        if result != None:
            print(result)
        else:
            print("Operazione non supportata!")
    except:
        print("Devi inserire un'operazione tra due numeri.")
        continue


print("Ciaone 👋")
