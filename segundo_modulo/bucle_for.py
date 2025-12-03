# Bucle for iterando sobre una cadena de texto
palabra = "Python"
for letra in palabra:
    print(letra)
# P
# y
# t
# h
# o
# n
print("-----")
# lista de letras 
frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    print(fruta)
# manzana
# naranja
# kiwi

print("-----")

# Usando break para salir del bucle
frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    if fruta == "kiwi":
        break
    print(fruta)
# manzana
# naranja

print("-----")
# Usando continue para saltar una iteración
frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    if fruta == "naranja":
        continue
    print(fruta)
# manzana
# kiwi
print("-----")
# Usando else con for
frutas = ["manzana", "naranja", "kiwi"]
for fruta in frutas:
    if fruta == "naranja":
        continue
    print(fruta)
else:
    print("Ya hemos terminado el bucle for")
# manzana
# kiwi
# Ya hemos terminado el bucle for

print("-----")
# Rango de números de 0 a 9
for i in range(10):
    print(i)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print("-----")
# Rango de números de 3 a 4
for i in range(3, 5):
    print(i)
# 3, 4
print("-----")
# Rango de números de 0 a 10 con paso de 2
for i in range(0, 11, 2):
    print(i)
# 0, 2, 4, 6, 8, 10
print("-----")
# Bucles anidados 
frutas = ["manzana", "naranja", "kiwi"]
adjetivos = ["rica", "saludable"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)
# manzana rica
# naranja rica
# kiwi rica
# manzana saludable
# naranja saludable
# kiwi saludable

print("-----")


frutas = ["manzana", "naranja", "kiwi"]
adjetivos = ["rica", "saludable"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)


