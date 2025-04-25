def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def muliply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Selecciones una operacion")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. salir")

        option = input("Ingrese su opcion (1,2,3,4,5):")
        print(type(option))
        if option == "5":
            print("Esta saliendo de la calculdora")
            break
        if option in ["1","2","3","4"]:
            num1 = float(input( "ingrese el primer numero: "))
            num2 = float(input( "ingrese el segundo numero: "))

            if option == "1":
                print("La suma es:", add(num1,num2))
            elif option=="2":
                print("La resta es:", substract(num1,num2))
            elif option=="3":
                print("La multiplicacion es:", muliply(num1,num2))
            else:
                print("La division es:", divide(num1,num2))
        else:
            print("opción no válido por favor intenta de nuevo")

calculator()


