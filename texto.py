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