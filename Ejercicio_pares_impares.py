def pares(limit):
    a = 2
    while a < limit:       
        yield a
        a +=2

def inpares(limit):
    a = 1
    while a < limit:       
        yield a
        a +=2
        

for par in pares(11):
    print(par)

print("-------------------------------")

for inpar in inpares(20):
    print(inpar)
