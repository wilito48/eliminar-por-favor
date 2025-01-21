diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)

"""
valor = diccionario['d']
print(valor)
"""

#get
#setdefault

"""
valor = diccionario.get('z', 'La llave no existe en el diccionario')
print(valor)
"""

valor = diccionario.setdefault('e', 5)
print(valor)
print(diccionario)
