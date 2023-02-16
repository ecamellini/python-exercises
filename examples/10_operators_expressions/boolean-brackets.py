
# Abbiamo un utente maggiorenne, che ha un diploma
# e che è residente a Milano
age = 35
isOver30 = age > 30
hasDiploma = True
hasMilanResidence = True

# Può accedere al corso solo se:
# - È residente a Milano E
# - ha un diploma Oppure ha più di 30 anni

canAccess = hasMilanResidence and (hasDiploma or isOver30)
