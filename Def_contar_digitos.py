def contar_digitos(n):
    n = abs(n)
    c = 1
    while n >= 10:
        n //= 10
        c += 1
    return c
x = contar_digitos(100)
print (x)