#Leer archivo linea por linea
"""with open('cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las lineas en una lista
"""with open('cuento.txt', 'r') as file:
    lineas = file.readlines()
    print(lineas)"""
#añadir texto
"""with open('cuento.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#sobreescribir el texto
"""with open('cuento.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")"""

with open('cuento.txt', 'r') as file:
    n = file.readlines()
    print(len(n))
