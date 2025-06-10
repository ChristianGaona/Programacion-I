saldo = 1000

def depositar(cantidad):  # Operación de deposito con .5% de IVA
    global saldo
    monto_real = cantidad - (cantidad * 0.005)
    saldo += monto_real
    print(f"Ha depositado ${monto_real}. Su saldo ahora es ${saldo}.")

def retirar(cantidad):  # Operación de retiro con .7% de IVA
    global saldo
    if cantidad <= saldo:
        monto_real = cantidad - (cantidad * 0.007)
        saldo -= monto_real
        print(f"Ha retirado ${monto_real}. Su saldo ahora es ${saldo}.")
    else:
        print("No cuenta con suficiente saldo para realizar esta operación.")

# Interfaz de usuario
while True:
    print("Opciones:")
    print("(1) Depositar")
    print("(2) Retirar")
    print("(3) Salir")

    opcion = input("Indique la opción que desee realizar: ")

    if opcion == '1':
        cantidad = float(input("Ingrese la cantidad que desee depositar: "))
        depositar(cantidad)
    elif opcion == '2':
        cantidad = float(input("Ingrese la cantidad que deseae retirar: "))
        retirar(cantidad)
    elif opcion == '3':
        print("Gracias, que tenga buen día.")
        break
    else:
        print("Opción no existente. Seleccione de nuevo.")