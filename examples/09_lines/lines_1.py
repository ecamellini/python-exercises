"""
Esempi di linee logiche e linee fisiche.
"""

# Due linee logiche (due istruzioni), due linee fisiche.
i = 5
print(i)

# Due linee logiche (due istruzioni), una linea fisica.
i = 5; print(i) # SCONSIGLIATO! Codice meno leggibile

# Una linea logica (una istruzione), più linee fisiche.
print('This is a string. \
This continues the string.')

# Python a volte non richiede esplicitamente backslash per andare a capo.
# Ad esempio, quando aspetta che si chiudano parentesi.
print(
    "Primo,",
    "Secondo,",
    "Terzo!"
)
