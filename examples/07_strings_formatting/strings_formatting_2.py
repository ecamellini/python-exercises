"""
Vari modi di formattare le stringhe.
"""

name = "Pluto"

print(f"Si chiama {name} e ha {30} anni.")  # f-string

print("Si chiama {0} e ha {1} anni.".format(name, 30))  # Python conta da 0

print("Si chiama {} e ha {} anni.".format(name, 30))  # numerazione automatica

# Possiamo anche concatenare stringhe con +, ma non è una buona pratica
# Perché? Perché dobbiamo occuparci noi di convertire i tipi in stringa e mettere spazi
print("Si chiama " + name + " e ha " + str(30) + " anni.")

# Possiamo dare nomi ai placeholder
print('{name} ha {age} anni da ottobre 2021'.format(name=name, age=30))

print("Si chiama", name, "e ha", 30, "anni.")  # passiamo più elementi a print
