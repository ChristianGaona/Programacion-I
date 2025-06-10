try:
    lista = ["Oscar", "Martin", "César", "Pedro", "Christian", "Sebastian", "Julian", "Miguel", "Akane"]
    a = lista[3]
    print(a)
    
    lista.sort()
    print(lista)
    
    lista.reverse()
    print(lista)
    
    animales = "perro elefante koala gato pajaro liebre"
    lista_animales = animales.split()
    print(lista_animales)
    
    if animales.startswith("pa"):
        print("Si inicia con pa")
    else:
        print("No inicia con pa")    
    
except ValueError:
    print("Valor inválido")    
except Exception as error:
    print("Ocurrió un error")