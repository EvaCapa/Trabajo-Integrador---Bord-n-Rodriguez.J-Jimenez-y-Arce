def cifrar(texto, clave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + clave) % 26 + base)
        else:
            resultado += char
    return resultado

def descifrar(texto, clave):
    return cifrar(texto, -clave)
