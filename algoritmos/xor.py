def cifrar(texto, clave):
    resultado = []
    for i in range(len(texto)):
        xor_val = ord(texto[i]) ^ ord(clave[i % len(clave)])
        resultado.append(format(xor_val, '02x'))  # convierte a hexadecimal
    return ''.join(resultado)
