def calcular_volumen(largo, ancho, altura):
    return largo * ancho * altura

def calcular_precio(volumen):
    if volumen < 1000000:
        return 100
    elif 1000000 <= volumen <= 5000000:
        return 300
    else:
        return 500
        
def operacion():
    print("Servicio de paquetería.\n")
    print("Indique las dimensiones del paquete que desee enviar.\n")
    print("--------------DATOS--------------\n")
    largo = float(input("Ingrese el largo de la caja: "))
    ancho = float(input("Ingrese el ancho de la caja: "))
    altura = float(input("Ingrese la altura de la caja: "))
    num_cajas = int(input("Cantidad de cajas que desea: "))
    volumen_por_caja = calcular_volumen(largo, ancho, altura)
    total_volumen = volumen_por_caja * num_cajas
    total_precio = calcular_precio(total_volumen)
    cantidad = num_cajas * total_precio
    
    print("\n-----------INFORMACIÓN-----------")
    print(f"\nDesglose de cm³ por caja: {volumen_por_caja} cm³.")
    print(f"Cantidad de cajas: {num_cajas} unidades.")
    print("\n*********************************")
    print(f"\nCosto total de envío: ${cantidad} pesos.")
    print("\n*********************************")
    
operacion()