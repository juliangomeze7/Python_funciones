def invertir(cadena):
    if len(cadena) <= 1:
        return cadena
    return invertir(cadena[1:]) + cadena[0]

def es_palindromo(cadena):
    s = cadena.replace(" ", "").lower()
    return s == invertir(s)

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("Sí es palíndroma.")
else:
    print("No es palíndroma.")