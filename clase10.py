numbers = {
    1:"uno",
    2:"dos",
    3:"tres"
}

print(numbers[2])
information = {
    "nombre":"Karen",
    "Apellido":"Rivas",
    "Altura":1.58,
    "Edad":27
}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = information = {
    "karen":{"Apellido":"Rivas",
    "Altura":1.58,
    "Edad":27},
    "Diego":{
    "Apellido":"Antezana",
    "Altura":1.80,
    "Edad":32},
    }

print(contacts["karen"])

