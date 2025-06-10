precios = []

def calcular_iva(precio):
    precio * .16
    try:
        while len(precios) < 20:
            print("Ingrese un precio o 'fin' para terminar: ")
            entrada = input().lower()
            if entrada == 'fin':
                break
            else:
                precios.append(float(entrada))
                
        for p in precio:
            print(p)
            iva = calcular_iva(p)
            print(iva)
            print(p + iva)
                
    except ValueError:
        print("El valor ingresado no es un número válido")            