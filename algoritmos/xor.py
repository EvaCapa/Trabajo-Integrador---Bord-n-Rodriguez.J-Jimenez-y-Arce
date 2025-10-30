def cifrar(texto, clave):
    res = ""
    for i in range(len(texto)):
        res += chr(ord(texto[i]) ^ ord(clave[i % len(clave)]))
    return res

def descifrar(texto, clave):
    # XOR se descifra igual que se cifra
    return cifrar(texto, clave)
