#iterar en cadenas
#creando la cadena
text = "Hola mundo"
#creando el objeto iterador
iter_text = iter(text)

#iterar en la cadena
for char in iter_text:
    print(char)