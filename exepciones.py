try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: el divisor no puede ser 0")
    print("a ocurrido un error",e)
except ValueError as e:
    print("Error: debes introducir un numero valido")
    print("a ocurrido un error",e)



def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
