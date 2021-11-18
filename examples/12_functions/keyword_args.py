"""
Esempio di utilizzo dei keyword arguments.
"""


def func(a, b=5, c=10):
    print('A è', a, 'B è', b, 'e C è', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)
