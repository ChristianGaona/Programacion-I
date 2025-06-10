# Ciclo para encontrar años biciestos
year = int(input("Ingrese un año bisiesto inicial: "))
for a in range(year, 2023):
    if a%4 ==0:
        print(a)