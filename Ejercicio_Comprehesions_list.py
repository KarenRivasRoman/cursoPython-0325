#1 Doble de los Números
#Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
numbers = [1, 2, 3, 4, 5]
doble = [x*2 for x in numbers]
print(numbers)
print(doble)

#2 Filtrar y Transformar en un Solo Paso
#Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
nuevas_palabras = [p.upper() for p in palabras if len(p) > 3]
print(nuevas_palabras)

#3 Crear un Diccionario con List Comprehension
#Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.

claves= ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

combinacion = {claves[i]: valores[i] for i in range(len(claves))}
print(combinacion)
#4 Calcula la matriz traspuesta utilizando una List Comprehension anidada.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)
matriz_trans = [[row[i] for row in matriz]for i in range(len(matriz[0]))]
print(matriz_trans)

#5 Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

lista = [dato for dato in personas if dato["ciudad"] == "Madrid" and dato["edad"] > 30  ]
print(lista)

#6 Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista
#  multiplicando por 2 los números pares y dejando los impares como están.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

transformados = [x * 2 if x%2 == 0 else x for x in n]
print(transformados)