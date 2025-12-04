
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
