# Asignación básica
y = 5  # y ahora vale 5

# Sumar y reasignar (forma larga vs. corta)
x = 5
x = x + 3   # x ahora vale 8
x = 5       # reiniciamos
x += 3      # mismo resultado: 8

# Restar y reasignar
x -= 3      # vuelve a 5

# Multiplicar y reasignar
x = 5
x *= 3      # 15
x /= 3      # 5.0  ← al dividir, el resultado es flotante (tipo *float*).

# Dividir y reasignar
x = 5.0     # x quedó flotante tras la división
x %= 2      # 1.0  ← el resto también es flotante.

# Potencia y reasignar
y = 20
y //= 2     # 10

# Si y fuera 21: y //= 2 → 10 (ignora la parte decimal).

# Exponente (elevar al cubo)
y = 10
y **= 3     # 1000 (10 * 10 * 10)


# Asignar dentro del print
print(z := 3)  # imprime 3 y, además, z queda asignada con 3
print(z)       # 3 (ya estaba guardado)

