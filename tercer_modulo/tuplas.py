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