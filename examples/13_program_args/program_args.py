"""
Esempio di utilizzo dei program arguments.
"""

import sys

# Esegui il programma con alcuni argomenti da linea di comando.
# Ad esempio:
# python program_args.py arg1 arg2 arg3

print('Il numero di argomenti è:', len(sys.argv))
print('Gli argomenti sono:', sys.argv)

# Noterai che il primo argomento è il percorso del file che stai eseguendo.
