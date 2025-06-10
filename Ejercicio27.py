def contar_vocales(cadena):
    """
    Cuenta el número de vocales en una cadena de texto.
    
    Args:
        cadena (str): Cadena de texto en donde se contarán las vocales.
        
    Returns:
        int: Número de vocales en la cadena de texto.
    """
    
    vocales = "aeiou""AEIOU""áéíóú""ÁÉÍÓÚ"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

print("Contador de vocales en un texto\n")
cadena = input("Ingrese un texto: ")
num_vocales = contar_vocales(cadena)
print(f"Su texto contiene {num_vocales} vocales.")