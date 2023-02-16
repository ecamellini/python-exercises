def executeOperation(operator, operand1, operand2):
    """
    Funzione che esegue un'operazione.
    Operazioni ammesse: +, -, *, /
    Restituisce il risultato, oppure None in
    caso di operazione non supportata
    """

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
