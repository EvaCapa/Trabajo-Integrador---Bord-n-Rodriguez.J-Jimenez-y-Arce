def cifrar(texto, clave):
    resultado = ""
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + clave) % 26 + base)
        else:
            resultado += c
    return resultado
