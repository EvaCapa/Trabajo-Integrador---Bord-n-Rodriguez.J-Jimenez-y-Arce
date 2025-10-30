# Implementación educativa de RSA

def generar_claves():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  # exponente público
    d = pow(e, -1, phi)  # inverso modular (clave privada)
    return (e, n), (d, n)

def cifrar(mensaje, clave_publica):
    e, n = clave_publica
    cifrado = [pow(ord(c), e, n) for c in mensaje]
    return cifrado

def descifrar(cifrado, clave_privada):
    d, n = clave_privada
    texto = ''.join(chr(pow(c, d, n)) for c in cifrado)
    return texto

def calcular(texto, clave):
    try:
        clave_publica, clave_privada = generar_claves()
        cifrado = cifrar(texto, clave_publica)
        descifrado = descifrar(cifrado, clave_privada)
        return f"""
Claves generadas:
Pública: {clave_publica}
Privada: {clave_privada}

Texto original: {texto}
Texto cifrado (números): {cifrado}
Texto descifrado: {descifrado}
"""
    except Exception as e:
        return f"Error en RSA: {e}"
