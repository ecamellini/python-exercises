"""
Esempi di escape sequences.
"""

# Stampiamo una stringa con un apice
print("What's your name?")
# Questo invece darebbe errore print('What's your name?')

# Altro modo:
print('What\'s your name?')

# Stampiamo una stringa con un backslash
print("""This is a backslash: \\""")

# Due escape sequences utili: \n e \t
print("Prima riga.\nSeconda riga.")
print("Prima dello spazio.\tDopo lo spazio.")

# r-String, raw String - ignora i caratteri speciali e li stampa come sono
# Utili ad esempio per rappresentare dei Path, con molti backslahes
print(r"Prima riga.\nSeconda riga.")
percorso_del_mio_file = r"C:\Documenti\nome_file"
print(percorso_del_mio_file)  # se non fosse raw, \n andrebbe a capo
percorso_del_mio_file = "C:\Documenti\nome_file"
print(percorso_del_mio_file)  # lo vedamo qua
