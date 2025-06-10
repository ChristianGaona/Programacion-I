print("Ingrese la base del triangulo:")
base = int(input())  # Pide al usuario que ingrese un valor entero para la base.

print("ingrese altura del triangulo:")
altura = int(input())  # Ahora entrará el valor de la altura.

area = (base * altura) / 2  # Calcula el área del triángulo usando la fórmula.

# Muestra el resultado del cálculo usando una cadena de texto con el valor calculado.
print("El área del triangulo es " + str(area))
# También se puede expresar de la siguiente manera:
print(f"El área del triangulo es {area}")  # Cadena f permite insertar variables dentro de una cadena de texto.