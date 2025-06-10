alumnos = ["Sebastian", "Joaquin", "Pedro"]

alumnos.append("Emiliano")
alumnos.append(input("Escribe tu nombre: "))
for a in alumnos:
    print(a)
else:
    print(f"La lista contiene {len(alumnos)} alumnos")  # len inicia en 1 y el index en 0    