x = 5
y = 3
z = 5 

# Comparaciones 
if(x==5):
    print("x es igual a 5")


# Comparaciones con and
if(x>y and z<x ):
    print(x,"es igual que igual a ",z)
elif(y<z and z>x):
        print(y,"es menor que ",z," y ",z," es mayor que ",x)
else:
        print("Ninguna condición se cumple")            

# verdadero: imprime
if 5 > 3:
    print("5 es mayor a 3")

# falso: no imprime
if 2 > 3:
    print("2 es mayor a 3")

x = 5
y = 3

if x > y:
    print("x es mayor a y")  # se ejecuta

if x < y:
    print("x es menor a y")  # no se ejecuta



x = 5
y = 5

if x > y:
    print("x es mayor a y")
else:
    if x == y:
        print("x es igual a y")
    else:
        print("ninguna de las condiciones anteriores se cumplió")


x = 5
y = 3
z = 1

if x > y and x > z:
    print("x es mayor a y y x es mayor a z")  # ambas verdaderas
else:
    print("ninguna de las condiciones anteriores se cumplió")


# Ejemplo con variables de texto
a = "Python"
b = "JavaScript"
c = "Python"

# igualdad y diferencia
if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")

# comparación con anidación
if a == c:
    if a != b:
        print("a es igual a c, pero es distinto a b")
    else:
        print("estoy saliendo por el else del if interno")