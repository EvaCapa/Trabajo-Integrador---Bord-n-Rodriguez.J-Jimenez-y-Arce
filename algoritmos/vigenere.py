def cifrar(texto, clave):
    texto = texto.upper()
    clave = clave.upper()
    resultado = ""
    for i, c in enumerate(texto):
        if c.isalpha():
            resultado += chr((ord(c) + ord(clave[i % len(clave)]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            resultado += c
    return resultado
