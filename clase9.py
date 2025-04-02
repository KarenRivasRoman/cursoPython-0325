a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
#slice
c = a[:]
print(c)
print(id(c))
a.append(6)
print(a)
print(b)
print(c)

#matriz
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
print(matrix[1][2])
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])
numbers[0] = 'unos'
print(numbers)