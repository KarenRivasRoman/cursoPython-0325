def Sumatoria(n):
    if n == 0:
        return 0
    else:
        return n + (Sumatoria(n -1))


print(Sumatoria(4))