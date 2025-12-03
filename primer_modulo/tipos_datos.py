texto1 = 'este es un texto'
texto2 = "este es un texto"
texto3 = '''este es un texto'''
texto4 = """este es un texto"""

print(texto1)
print(texto2)
print(texto3)
print(texto4)

# Tipos de datos en Python
# Números, cadenas, listas, tuplas, diccionarios, conjuntos y boolean
A = 42          # entero
B = 3.14        # flotante (usa punto, no coma)
C = 5 + 2j      # complejo, parte imaginaria con J
# Cadenas de texto
print(A)
print(B)
print(C)

# Mostrar tipo de dato
lista = [0, 1, 2, 3, 4, 5]      # ordenada y mutable

# tupla ordenada e inmutable
tupla = ('A', 'B', 'C')

#diccionario clave:valor
diccionario = {
    'nombre': 'Ada',
    'edad': 36
}


#conjunto = {1, 2, 3}  # no ordenado y sin duplicados
conjunto = {1, 1, 2, 2, 3}
# Output esperado: {1, 2, 3}

#booleanos

booleano_verdadero = True
booleano_falso = False

#tipo de dato none 
x = None
print(x)           # Muestra: None
print(type(x))     # Muestra: <class 'NoneType'>

# Mostrar tipos de datos
print(type(" "))   # String vacío.
print(type(0))     # Número cero.
print(type(False)) # Booleano false.
print(type([]))    # Lista vacía.