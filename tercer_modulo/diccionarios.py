
# Definición de un diccionario
auto = {
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2025
}
print(auto)
# acceso a elementos
print(auto['marca'])      # Renault
print(auto.get('marca'))  # Renault

#Si quieres solo las claves o solo los valores:
print(auto.keys())    # dict_keys(['marca', 'modelo', 'año'])
print(auto.values())  # dict_values(['Renault', 'Clio', 2025])

# Modificar un valor existente
auto['año'] = 2020

# Agregar un nuevo par clave-valor
auto['color'] = 'verde'
print(auto)

# Con update puedes modificar y agregar en una sola línea:
auto.update({'año': 2022, 'litros gasolina': 4.5})
print(auto)

#Comprueba si una clave existe con in. Recuerda: es case sensitive.
if 'marca' in auto:
    print('Marca es una de las propiedades de este diccionario')

if 'MARCA' not in auto:  # no entra por sensibilidad a mayúsculas
    print('No esta en el diccionario')



auto['puertas'] = '4 puertas'
print(auto)

# Eliminar por clave
auto.pop('puertas')

# Eliminar el último par insertado
auto.popitem()

# Vaciar el diccionario por completo
auto.clear()
print(auto)  # {}


#¿Cómo recorrer claves, valores y parejas con for e items?

# Solo claves
for k in auto:
    print(k)

# Solo valores
for v in auto.values():
    print(v)

# Clave y valor al mismo tiempo
for clave, valor in auto.items():
    print(clave, valor)

#¿Qué son los diccionarios anidados y cómo acceder?
familia = {
    'hijo uno':  {'nombre': 'Pedro',   'edad': 8},
    'hijo dos':  {'nombre': 'Ana',     'edad': 7},
    'hijo tres': {'nombre': 'Marcelo', 'edad': 6}
}

print(familia['hijo uno']['nombre'])  # Pedro