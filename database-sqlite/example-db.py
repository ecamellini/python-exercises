import sqlite3

con = sqlite3.connect("library.db")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE Book(title, author, year)")
    print("Tabella Book creata con successo.")
except:
    print("Non creo la tabella perché esite già.")

cur.execute("""INSERT INTO Book VALUES
        ('Il Signore degli Anelli', 'Tolkien', 1954),
        ('2000 Leghe Sotto i Mari', 'Verne', 1850)
""")
con.commit()
print("Query INSERT eseguita correttamente.")


res = cur.execute("""SELECT * FROM Book""")

books = res.fetchall()

for book in books:
    print(book)
    # print(book[0])
    # print(book[1])
    # print(book[2])
