# Definición de una tupla
tecnologias = ("Python", "JavaScript", "Go")
print(tecnologias)                 # ('Python', 'JavaScript', 'Go')
print(tecnologias[1])              # 'JavaScript'

#contar elementos
tecnologias = ("Python", "JavaScript", "Go", "Python")
print(len(tecnologias))            # 4

# Tipo de dato
tecnologias = ("Python", "JavaScript", "Go")
print(type(tecnologias))           #  tupla

fruta = ("manzana")
print(type(fruta))                 # string

fruta = ("manzana",)
print(type(fruta))                 #tupla

# diferentes tipos de datos en una tupla
tupla = ("Python", 5, True)
print(tupla)                       # ('Python', 5, True)
print(type(tupla))                 # tupla

# Desempaquetado de tuplas
tupla = ("Python", 5, True)
x, y, z = tupla
print(x, y, z)                     # Python 5 True


# concatenar y duplicar elementos
tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5)
tupla3 = tupla1 + tupla2
print(tupla3)                      # (1, 2, 3, 3, 4, 5)

print(tupla * 2)                   # ('Python', 5, True, 'Python', 5, True)