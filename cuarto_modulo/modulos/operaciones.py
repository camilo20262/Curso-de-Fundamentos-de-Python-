print("-----")
# devolver un valor
def sumar(a, b):
    return a + b
# usar el valor devuelto
resultado = sumar(2, 3)
print(resultado)  # 5



print("-----")
def restar(x,y):
    return x - y

resta=restar(10,4)
print(resta)  # 6

print("-----")

def dividir(a,b):
    if b == 0:
        return "Error: División por cero"
    return a / b

division_mala=dividir(10,0)
print(division_mala)  # Error: División por cero

divsion=dividir(10,2)
print(divsion)  # 5.0

print("-----")

def multiplicar(a,b):
    return a*b

multipliacion=multiplicar(4,5)
print(multipliacion)  # 20
