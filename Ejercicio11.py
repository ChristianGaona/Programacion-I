try:  # Código que puede generar un error.
    resultado = 5/0  # Intentará dividir entre cero, pero no podrá.
    print("El resultado", resultado)
except ValueError:
    print("El valor ingresado es incorrecto.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except:  # Código que se ejecuta si ocurre una excepción:
    print("Ocurrio un error, intente de nuevo.")