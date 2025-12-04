
# Listas en Python
# Definición de una lista
frutas = ["manzana", "naranja", "mandarina"]
print(frutas)              # ['manzana', 'naranja', 'mandarina']
print(type(frutas))        # 
print(frutas[1])           # 'naranja' (índices desde 0)

# Modificar por índice (mutabilidad)
frutas[1] = "banana"
print(frutas[1])           # 'banana'
print(frutas)              # ['manzana', 'banana', 'mandarina']

# Duplicados
frutas.append("naranja")   # ahora hay otra 'naranja' al final
print(frutas)              # ['manzana', 'banana', 'mandarina', 'naranja']

# Listas pueden contener diferentes tipos de datos
mixta = ["TuNombre", 42, True]
print(mixta)        # ['TuNombre', 42, True]
print(type(mixta))  # lista

print(len(mixta))   # 3
print(len(frutas))  # 4

# Suponiendo frutas = ['manzana', 'banana', 'mandarina', 'naranja']
print(frutas[0:2])  # ['manzana', 'banana']
print(frutas[:2])   # ['manzana', 'banana']
print(frutas[1:])   # ['banana', 'mandarina', 'naranja']