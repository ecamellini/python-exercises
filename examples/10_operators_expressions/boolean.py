"""
Boolean type and operators.
"""

# Paolo è un ragazzo italiano, moro.

# Quindi, in termini booleani, abbiamo due affermazioni vere:
# Paolo è moro -> Vero (True)
# Paolo è italiano -> Vero (True)

# Mentre, ad esempio:
# Paolo è biondo -> Falso (False)
# Paolo è francese -> Falso (False)

# Tabella della verità: operatore AND
# Il risultato dell'operatore AND è True se entrambi i suoi operandi sono True.
False and False  # False -- Esempio: Paolo è biondo E Paolo è francese -> False
False and True  # False -- Esempio: Paolo è biondo E Paolo è italiano -> False
True and False  # False -- Esempio: Paolo è moro E Paolo è francese -> False
True and True  # True -- Esempio: Paolo è moro E Paolo è italiano -> True

# Tabella della verità: operatore OR
# Il risultato dell'operatore OR è True se almeno uno degli operandi è True.

False or False  # False -- Esempio: Paolo è biondo Oppure Paolo è francese -> False
False or True  # True -- Esempio: Paolo è biondo Oppure Paolo è italiano -> True
True or False  # True -- Esempio: Paolo è moro Oppure Paolo è francese -> True
True or True  # True -- Esempio: Paolo è moro Oppure Paolo è italiano -> True

# Tabella della verità: operatore NOT (Negazione)
# Il risultato dell'operatore NOT è True se l'operando è False, e viceversa.
not False  # True -- Paolo NON è biondo --> True
not True  # False -- Paolo NON è moro --> False

# Esempio
# Paolo è moro, italiano, e ha 33 anni.
paolo_moro = True
paolo_biondo = False
paolo_italiano = True
paolo_francese = False
paolo_anni = 33

print(f"Paolo NON è moro: {not paolo_moro}")  # False
print(f"Paolo è moro E italiano: {paolo_moro and paolo_italiano}")  # True
print(f"Paolo è moro E francese: {paolo_moro and paolo_francese}")  # False
print(f"Paolo ha 30 anni o meno: {paolo_anni <= 30}")  # False
print(f"Paolo è biondo Oppure francese: \
  {paolo_biondo or paolo_francese}")  # False
print(f"Paolo è biondo Oppure italiano: \
  {paolo_biondo or paolo_italiano}")  # True
print(f"Paolo è biondo Oppure italiano, e ha più di 30 anni: \
{paolo_biondo or paolo_italiano and paolo_anni > 30}")  # True
