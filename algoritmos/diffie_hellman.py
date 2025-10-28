import random

def calcular(texto, clave_usuario):
    p = 23
    g = 5
    clave_otro = random.randint(1, p-2)
    clave_privada_usuario = int(clave_usuario)
    clave_publica_otro = pow(g, clave_otro, p)
    secreto = pow(clave_publica_otro, clave_privada_usuario, p)
    
    mensaje_cifrado = ""
    for c in texto:
        mensaje_cifrado += chr(ord(c) ^ (secreto % 256))
    
    return mensaje_cifrado, secreto

if __name__ == "__main__":
    mensaje = input("Ingresa el mensaje a cifrar: ")
    clave_usuario = input("Ingresa tu clave numérica secreta: ")
    cifrado, secreto = calcular(mensaje, clave_usuario)
    print(f"Mensaje cifrado: {cifrado}")
    print(f"Clave secreta compartida: {secreto}")
