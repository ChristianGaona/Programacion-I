edad = int(input("¿Cuál es su edad? "))
if (edad >= 18 and edad < 70):  # La edad admitida es a partir de 18, pero menor que 70.
    print("Usted aplica para una licencia de conducir.")
else:
    print("Usted no aplica para una licencia de conducir.")


color = input("Menciona un color de la bandera de japón: ")
if (color == "rojo" or color == "blanco"):  # Se pregunta si los datos ingresados son igual que los esperados.
    print("El color esta en la bandera de Japón.")
else:  # Si el color ingresado no es ninguno de los dos:
    print("Ese color no esta en la bandera de Japón.")