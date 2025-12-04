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