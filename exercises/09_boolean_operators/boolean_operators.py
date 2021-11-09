"""
Puoi accedere a un corso solo se hai un diploma e più di 25 anni
Scrivi un programma che:
- Chiede l'età all'utente
- Chiede se l'utente ha un diploma - l'utente può rispondere True o False
- Ci dice se l'utente può accedere al corso oppure no, stampando True o False
"""

età = int(input("Quanti anni hai? "))
diploma = input("Hai un diploma? ").lower() == "sì"

print("Puoi accedere al corso: ", età > 25 and diploma)
