def maximo_de_tres(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


x=int(input("Ingrese un numero: "))
y=int(input("Ingrese un numero: "))
z=int(input("Ingrese un numero: "))
w = maximo_de_tres(x,y,z)
print ("EL numero mayor es: ", w)
