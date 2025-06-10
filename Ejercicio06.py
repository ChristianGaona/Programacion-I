nombre = input("¿Cuál es su nombre? ")
numero_control = input("Ingrese su numero de control: ")

sueldo_diario = int(input("¿Cuál es su sueldo diario? "))
dias_trabajados = int(input("¿Cuántos días trabajó este mes? "))
salario_mensual = sueldo_diario * dias_trabajados

# Si el salario mensual pagado es menor a 5000, se aplicará un porcentaje extra.
if salario_mensual <= 5000:
    bono = salario_mensual * 0.15
    pago_bono = salario_mensual + bono
    print("\nNombre:",nombre,"\nNúmero de control:",numero_control,"\nSu salario mensual total es", pago_bono, "incluyendo un bono de 15%.")
# Si no es menor y es mayor o igual a 5000, no se aplicará ningún porcentaje.
else:
    print("\nNombre:",nombre,"\nNúmero de control:",numero_control,"\nSu salario mensual total es", salario_mensual)