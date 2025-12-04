

# Sin manejo:
#resultado = 10 / 0  # Provoca ZeroDivisionError


# Con manejo específico:
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero.")


# Sin manejo:
#print(x)  # Provoca NameError
print("---")
# Con manejo específico:
try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida.")


#bloque finally
# Con error presente:
try:
    print(x)  # x no definida
except NameError:
    print("Esta variable no ha sido definida.")
finally:
    print("Esto se ejecuta siempre.")


print("---")
# Sin error:
x = 1
try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida.")
finally:
    print("Esto se ejecuta siempre.")