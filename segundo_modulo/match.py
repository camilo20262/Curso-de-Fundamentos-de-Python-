## Ejemplo de uso de match-case en Python
## El siguiente código demuestra cómo utilizar la estructura match-case
## para realizar diferentes acciones basadas en el valor de una variable.
dia = 1

match dia:
    case 1:
        print("hoy es lunes")
    case 2:
        print("hoy es martes")
    case 3:
        print("hoy es miércoles")
    case _:
        print("No coincide con ninguna de las anteriores opciones")

# Ejemplo con marcas de autos de Fórmula 1
#

marca="Red Bull"

match marca:
    case "Mercedez":
        print("Lewis Hamilton")
    case "Red Bull":
        print("Max Verstappen")
    case "Ferrari":
        print("Charles Leclerc")
    case _:
        print("No conozco al piloto de esa marca")