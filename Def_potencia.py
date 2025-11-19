def potencia(base, exponente):
    r = 1
    for _ in range(exponente):
        r *= base
    return r
a = potencia(2,3)
print(a)