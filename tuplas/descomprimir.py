# * -> lista
# _ -> Omitir valor

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
uno, dos, tres, cuatro, cinco, *resto_valores, ocho, nueve = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(resto_valores)
print(ocho)
print(nueve)