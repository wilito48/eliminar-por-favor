nombre = "Kervyn Willy"
apellido = "Rojas"

#nombre_completo = "Mr. " + nombre + " " + apellido

#nombre_completo = "Mr. %s %s %s." %(nombre, apellido, "Perez")

"""nombre_completo = "Mr. {nombre} {primer_apellido} {segundo_apellido}.".format(
    nombre=nombre,
    primer_apellido = apellido,
    segundo_apellido = "Perez" 
)
"""

nombre_completo = f"Mr. {nombre} {apellido} {"Perez"}"
print(nombre_completo)