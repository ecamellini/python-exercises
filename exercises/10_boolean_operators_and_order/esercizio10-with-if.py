age = int(input('Quanti anni hai? '))
hairColor = input("""Inserisci il colore dei capelli.
(Valori ammessi: biondo, moro, castano, grigio, altro):
""").lower()
hairLenght = input("""Hai i capelli lunghi o corti?
(Valori ammessi: lunghi, corti)
""").lower()

isUnder20 = age < 20
isOver65 = age > 65

hasBlondeHair = hairColor == "biondo"
hasBlackHair = hairColor == "moro"
hasBrownHair = hairColor == "castano"
hasGreyHair = hairColor == "grigio"

hasShortHair = hairLenght == "corti"

canAccessCasting1 = isUnder20 and (hasBlondeHair or hasBlackHair)
canAccessCasting2 = isOver65 and hasGreyHair
canAccessCasting3 = (not hasShortHair) and (not hasBrownHair)
canAccessCasting4 = hasShortHair and (hasBlondeHair or hasBlackHair)

canAccessCasting = canAccessCasting1 or canAccessCasting2 or canAccessCasting3 or canAccessCasting4
print(f"Puoi accedere al casting: {canAccessCasting}")

# canAccessCasting = (isUnder20 and (hasBlondeHair or hasBlackHair)) or (isOver65 and hasGreyHair) or (
#     (not hasShortHair) and (not hasBrownHair)) or (hasShortHair and (hasBlondeHair or hasBlackHair))

if canAccessCasting:
    print("Congratulazioni! Puoi accedere ai provini.")
    if age < 18:
        print("Essendo minorenne hai diritto anche a un bel buono Amazon da 20 euro.")
else:
    print("Peccato, riprova la prossima volta.")


print("Questa stringa verrà stampata sempre.")
