try:
    lista = ["Oscar", "Martin", "Cesar"]

    lista.append("Emiliano")  # Anexar un elemento al final de la lista.
    lista.append("Angel")
    lista.append("Jostyn")
    print(lista)

    lista.insert(3, "Dylan")  # Anexar un elemento en una posición específica.
    print(lista)

    lista.remove("Angel")  # Elimina un elemento de la lista dependiendo de su valor.
    print(lista)
    
    # Si intentamos remover un elemento que no existe en la lista, prvocará un ValueError.
    # lista.remove("Akane")
    
    removido = lista.pop(4)  # Remover un elemento por su índice.
    print(removido)
    print(lista)
    
    lista.pop()  # Si no especificamos un índice, removerá el último valor.
    print(lista)

    lista.pop(-2)  # Se puede remover a partir del último elemento contando en negativo.
    print(lista)
    
    # Si intentamos remover un índice que no existe, arrojará error.
    # lista.pop(80)
    
    del lista[2]
    print(lista)
    
    lista.append("Carlos")
    lista.append("Luis")
    lista.append("Ramon")
    lista.insert(3, "Alexandro")
    lista.append("Dahir")
    print(lista)
    
    del lista[2:5]  # del nos permite eliminar su índice.
    print(lista)
    
    lista.clear()  # Eliminar o limpiar toda la lista.
    print(lista)
    
except ValueError:
    print("El valor que esta intentando remover no existe.")    
except IndexError:
    print("El indice ingresado no existe.")
except:
    print("Ocurrio un error.")