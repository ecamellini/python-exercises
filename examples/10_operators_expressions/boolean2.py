age = int(input('Quanti anni hai: '))
diplomaInput = input('Hai un diploma (scrivi yes o no)? ')
diplomaInputLower = diplomaInput.lower()

# Può accedere al corso solo se
# ha un diploma E
# è maggiorenne
isOverage = age >= 25
hasDiploma = diplomaInputLower == 'yes'

canAttendCourse = isOverage and hasDiploma
print(f"Puoi iscriverti al corso: {canAttendCourse}")
