"""
Vediamo perché ci serve formattare stringhe.
"""

age = 35
print("Anni di Pippo:")
print(age)
print("Tra 3 anni Pippo ne avrà:")
print(age + 5)
print("Tra 10 anni Pippo ne avrà:")
print(age + 10)
print("Pippo è nato nel:")
print(2021 - age)

# E se invece Pippo si chiamasse Pluto? Usiamo una variabile.
# Ma dobbiamo poterla usare all'interno di una stringa.
name = "Pluto"
print(f"Anni di {name}:")
print(age)
print(f"Tra 3 anni {name} ne avrà:")
print(age + 5)
print(f"Tra 10 anni {name} ne avrà:")
print(age + 10)
print(f"{name} è nato nel:")
print(2021 - age)
