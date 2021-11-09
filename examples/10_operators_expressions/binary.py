"""
Binary operators.
"""

# Utilizza bin(X) per stampare X in binario, e int per la conversione inversa.
print(bin(10))  # '0b1010'
print(int('1010', 2))  # 10

# Left shift - Sposta i bit di N posizioni a sinistra
# 4 binario: 100 cioè 00100
# Shift a sinistra di due: 100 << 2 = 10000 cioè 16 decimale
# Shift a sinistra è moltiplicazione per due, due shift è per 4
print(4 << 2)

# Right shift - Sposta i bit di N posizioni a destra
# 4 binario: 100
# Shift a destra di due: 100 >> 2 = 1 cioè 1 decimale
# Shift a destra è divisione per due, due shift è per 4
print(4 >> 2)

# Bitwise AND / AND binario
# Per ogni bit, se sono entrambi 1 --> 1. Altrimenti --> 0
# 10 binario: 1010
# 6 binario: 0110
# AND binario: 1010 & 0110 = 0010 cioè 2 decimale
print(10 & 6)

# Bitwise OR / OR binario
# Per ogni bit, se almeno uno è 1 --> 1. Altrimenti --> 0
# 10 binario: 1010
# 6 binario: 0110
# OR binario: 1010 | 0110 = 1110 cioè 14 decimale
print(10 | 6)

# Bitwise XOR / XOR binario (eXclusive-OR)
# Per ogni bit, se i bit sono diversi --> 1.
# 10 binario: 1010
# 6 binario: 0110
# XOR binario: 1010 ˆ 0110 = 1100 cioè 12 decimale
print(10 ^ 6)

# Bitwise NOT / Negazione binaria (complemento a due )
# L'inversione binaria di x è -(x+1)
# ~5 restituisce -6. Per più dettagli http://stackoverflow.com/a/11810203
print(~5)
