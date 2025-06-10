try:
    print("Ingrese números de telefono separados por coma: ")
    telefonos = input()
    tels = telefonos.split(",")

    guaymas = 0
    hermosillo = 0
    obregon = 0
    otro = 0

    for t in tels:
        if t.startswith("622"):
            guaymas += 1
        elif t.startswith("644"):
            obregon += 1
        elif t.startswith("662"):
            hermosillo += 1
        else:
            otro += 1

    print(f"Existen {guaymas} números de Guaymas")                    
    print(f"Existen {obregon} números de Obregón")
    print(f"Existen {hermosillo} números de Hermosillo")
    print(f"Existen {otro} números de otras ciudades")
    
except:
    print("Ocurrió un error")    