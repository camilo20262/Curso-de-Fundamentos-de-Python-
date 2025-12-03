# Comillas dentro de comillas
print("Hola 'mundo'")
print('Hola "mundo"')

# Múltiples líneas con comillas triples
multiples = """Hola
Mundo
este 
soy 
yo"""
print(multiples)

# Contar caracteres
palabra = "murciélago"
print(len(palabra))  # 10

# Búsqueda de palabras
texto = "Este curso es de fundamentos de Python"
print("Este" in texto)   # True
print("python" in texto)   # False (por *case sensitive*)
print("JavaScript" not in texto)  # True


texto = "Este curso es de fundamentos de Python"

# Transformación de texto
mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula)
print(minuscula)

# La última asignación prevalece
texto2 = texto.upper()
texto2 = texto2.lower()
print(texto2)  # se ve en minúscula

# Limpieza de espacios
espacios = "   este es el texto   "
sin_espacios = espacios.strip()
print(sin_espacios) # es una forma 
print(espacios.strip()) # es otra forma 


#
texto = "Este es un texto"
print(texto[0])   # E
print(texto[5])   # e


print(texto[0:4])   # Este
# Hasta el final contando manualmente: cuidado con la última letra
print(texto[0:15])  # falta la 'o' final si 15 apunta a esa posición


print(texto[:7])   # "Este es"
print(texto[5:])   # desde la "e" de "es" hasta el final
# De la "e" de "es" hasta incluir la "x": fin como -2 para abarcar la X
print(texto[5:-2])

curso = "Este curso es de JavaScript" # "Este curso es de Python" Si hubiera múltiples "JavaScript", las reemplaza todas
print(curso.replace("JavaScript", "Python"))

texto_dividido = texto.split(" ")
print(texto_dividido)  # ['Este', 'es', 'un', 'texto']


texto3 = "Este Texto tiene MAYÚSCULAS y minúsculas"
buscado = "mayúsculas"
print(buscado in texto3)  # False
print(buscado.lower() in texto3.lower())  # True

print("texto".lower() in texto3.lower())# busca TEXTO lo convierte en lower y lo encuentra 


