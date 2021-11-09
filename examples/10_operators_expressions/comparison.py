"""
Operatori di confronto.
"""

print(5 < 3)  # False
print('a' < 'b')  # True
print(5 > 3)  # True
print('a' > 'b')  # False
print(5 <= 3)  # False
print('a' >= 'a')  # True
print(5 == 5)  # True
print('a' == 'b')  # False
print('a' != 'b')  # True

x = 3
y = 6
print(x <= y)  # True
x = 4
y = 3
print(x >= y)  # True
x = 'str'
y = 'stR'
print(x == y)  # False
x = 'str'
y = 'str'
print(x == y)  # True
x = 'str'
y = 'str'
print(x + x != y * 2)  # False
