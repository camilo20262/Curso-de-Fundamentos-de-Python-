
try:
    f = open("archivo.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print("---")
# Al escribir con w, el contenido previo se pierde. Luego puedes leer lo recién escrito.
try:
    with open("archivo2.txt", "w", encoding="utf-8") as f: #
        f.write("hola mundo desde write en el with\n")
except FileNotFoundError:
    print("No se ha encontrado el archivo")

with open("archivo2.txt", "a", encoding="utf-8") as f:
    f.write("\n")
    f.write("ESTA MUY BUENO ESTO")

with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.read())  # Lee todo el archivo