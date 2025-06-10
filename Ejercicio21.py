def calcular_promedio(lista_numeros):
    suma = 0
    for n in lista_numeros:
        suma += n
    return suma/len(lista_numeros)    

numeros = []

while len(numeros) < 20:
    
    print("Ingresa un numero: ")
    
    numeros.append(int(input()))
else:
    print(f"El promedio de los numeros es {calcular_promedio(numeros)}")    