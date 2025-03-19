x = 10
y = 5.678
#z = 1.2e6
#a = 1.2E-6
print(type( x))
print(type(y))
print(x + x)
print(x +y)
print(y +y )
is_true = True
is_false = False
print(is_true)
print(type(is_true))

print("Nunca", "pares", "de", "aprender", sep="_ ")
#end=
print("Nunca", end=" ")
print("pares de aprender")
#f-strings
frase = "Nunca pares de aprender"
author = "Platzi"
print(f"Frase: {frase}, Autor: {author}")
#format
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase: {}, Autor: {}".format(frase, author))
#cantidad decimales
valor = 3.14159
print("Valor: {:.2f}".format(valor))
#salto
print("Hola\nmundo")
#caracter especial
print('Hola soy \'Carli\'')
#url
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")