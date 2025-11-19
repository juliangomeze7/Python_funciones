def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)
x = mcd(2,13) , mcm(2,18
                    )
print(x)