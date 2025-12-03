B = True
F = False
print(B)   # True
print(F)   # False
print(type(B))  ## <class 'bool'>
print(type(F))  ## <class 'bool'>

# Comparisons   
print(5 > 3)  # True
print(3 > 5)  # False

# Boolean values in conditions
print(bool("hola mundo"))           # True -> *string* con contenido
print(bool(1))                       # True -> número con contenido
print(bool(2))                       # True
print(bool(3))                       # True
print(bool(["manzana", "pera"]))   # True -> *list* con elementos



# Falsy values
print(bool(""))     # False -> *string* vacío
print(bool(0))       # False -> cero
print(bool([]))      # False -> *list* vacía
print(bool(None))    # False -> *None*


# Checking types with isinstance
x = 3
print(isinstance(x, int))   # True -> es entero

x = 0.5
print(isinstance(x, int))   # False -> ahora es flotante (*float*)



