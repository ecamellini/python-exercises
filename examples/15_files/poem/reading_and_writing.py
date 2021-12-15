poem = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
"""


# Aprire un file in scrittura: 'w' sta per write
with open('poem.txt', 'w') as f:
    # Scrivere testo nel file
    f.write(poem)

# Aprire un file in modalità lettura: 'r' sta per read
with open('poem.txt', 'r') as f:
    content = f.readlines()
    for line in content:
        print(line)
