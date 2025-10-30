def generar_clave(texto, clave):
    clave = list(clave)
    if len(texto) == len(clave):
        return "".join(clave)
    else:
        for i in range(len(texto) - len(clave)):
            clave.append(clave[i % len(clave)])
    return "".join(clave)

def cifrar(texto, clave):
    texto = texto.upper()
    clave = generar_clave(texto, clave.upper())
    cifrado = ""
    for i in range(len(texto)):
        if texto[i].isalpha():
            cifrado += chr((ord(texto[i]) + ord(clave[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            cifrado += texto[i]
    return cifrado

def descifrar(texto, clave):
    texto = texto.upper()
    clave = generar_clave(texto, clave.upper())
    descifrado = ""
    for i in range(len(texto)):
        if texto[i].isalpha():
            descifrado += chr((ord(texto[i]) - ord(clave[i]) + 26) % 26 + ord('A'))
        else:
            descifrado += texto[i]
    return descifrado
