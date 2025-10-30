# Simulación básica del intercambio de claves Diffie-Hellman

def calcular(texto, clave):
    try:
        # Convertimos a enteros (parámetros públicos)
        p = 23  # número primo
        g = 5   # base (raíz primitiva)
        a = int(texto)  # clave privada del usuario A
        b = int(clave)  # clave privada del usuario B

        # Claves públicas
        A = (g ** a) % p
        B = (g ** b) % p

        # Claves compartidas
        clave_A = (B ** a) % p
        clave_B = (A ** b) % p

        return f"""
Parámetros públicos:
p = {p}, g = {g}

Claves privadas:
a = {a}, b = {b}

Claves públicas:
A = {A}, B = {B}

Clave compartida generada (igual para ambos):
Clave_A = {clave_A}
Clave_B = {clave_B}
"""
    except Exception as e:
        return f"Error en el cálculo: {e}"

def descifrar(texto, clave):
    return "Diffie-Hellman no cifra texto directamente. Sirve para generar una clave compartida."
