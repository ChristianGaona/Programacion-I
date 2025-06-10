def calcular_impuesto(tipo, valor):
    if tipo == "IVA":
        return float(valor) * 0.16
    # elif = else if
    elif tipo == "ISR":
        return float(valor) * 0.33
    elif tipo == "IEPS":
        return float(valor) * 0.15
    elif tipo == "ISN":
        return float(valor) * 0.10
    else:
        return 0
    
tipo = input("Ingrese el tipo de impuesto: ")
valor = input("Ingrese el valor: ")

impuesto = calcular_impuesto(tipo.upper(), valor)
total = float(valor) + float(impuesto)

print("El precio es de", valor)
print("El impuesto es de", impuesto)
print("El total es", total)