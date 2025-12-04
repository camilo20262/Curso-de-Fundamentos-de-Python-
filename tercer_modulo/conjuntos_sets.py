# Definición de un conjunto (set)
frutas = {"manzana", "naranja", "mandarina", "naranja"}
print(frutas)        # {'manzana', 'naranja', 'mandarina'} (el duplicado se ignora)
print(type(frutas))  # 
print(len(frutas))   # 3

# ciclor sobre un conjunto
for item in frutas:
    print(item)  # Puede salir en cualquier orden.

# diferentes tipos de datos en un conjunto
conjunto = {"Python", 156, True}
print(conjunto)      # Orden no garantizado.
print(type(conjunto))#

# comprobar si un elemento está en el conjunto
print("manzana" in frutas)  # True
print("pera" in frutas)     # False


frutas.add("pera") # agrega un elemento
frutas_tropicales = {"piña", "mango"} # agrega varios elementos
frutas.update(frutas_tropicales)  # #agrega varios elementos 
print(frutas)

frutas.add("Sandia")# agrega un elemento
print(frutas)


# eliminar elementos
frutas.remove("mango")   # ok si "mango" está; error si no.
frutas.discard("pera")   # ok esté o no esté "pera".
print(frutas)


# eliminar un elemento al azar
eliminado = frutas.pop()  # elemento al azar
print(eliminado) # el elemento eliminado
frutas.clear()
print(frutas)             # set()

# operaciones con conjuntos
A = {"A", "B", "C"}
B = {"C", "D", "E"}
# uniones, intersecciones y diferencias
C_union = A.union(B)             # {'A', 'B', 'C', 'D', 'E'}
I_inter = A.intersection(B)      # {'C'}
D_diff  = A.difference(B)        # {'A', 'B'}

print(C_union)
print(I_inter)
print(D_diff)