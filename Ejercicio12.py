def calcular_volumen(largo, ancho, alto):
    return largo * ancho * alto

def calcular_total(precio, numero_cajas):
    return precio * numero_cajas

try:
    largo = float(input("Ingrese el largo de la caja:\n"))
    
    ancho = float(input("Ingrese el ancho de la caja:\n"))
    
    altura = float(input("Ingrese la altura de la caja:\n"))
    
    numero_cajas = int(input("Ingrese el número de cajas:\n"))
    
    volumen = calcular_volumen(largo, ancho, altura)
    
    if volumen < 1000000:
        precio = 100
    elif volumen >= 1000000 and volumen <= 5000000:
        precio = 300
    else:
        precio= 500
        
    precio_total = calcular_total(precio, numero_cajas)

    print("-----------------------------------")
    print("CENTÍMETROS CÚBICOS POR CAJA:", volumen)
    print("NÚMERO DE CAJAS A ENVIAR:",  numero_cajas)
    print("-----------------------------------")
    print("TOTAL A PAGAR:", precio_total)

except ValueError:
    print("Solo valores numéricos pueden ser ingresados.")