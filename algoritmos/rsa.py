import random

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inversa_modular(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generar_primos(clave_usuario):
    primos = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    random.seed(int(clave_usuario))
    p = random.choice(primos)
    q = random.choice([x for x in primos if x != p])
    return p, q

def calcular(texto, clave_usuario):
    p, q = generar_primos(clave_usuario)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if mcd(e, phi) == 1:
            break
        e += 1

    d = inversa_modular(e, phi)
    if d is None:
        return calcular(texto, clave_usuario)

    mensaje_cifrado = [pow(ord(c), e, n) for c in texto]
    mensaje_descifrado = "".join([chr(pow(c, d, n)) for c in mensaje_cifrado])

    return mensaje_cifrado, mensaje_descifrado
