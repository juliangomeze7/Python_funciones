def invertir(cadena):
    if cadena == "":
        return ""
    return invertir(cadena[1:]) + cadena[0]
x = invertir("hola")
print (x)