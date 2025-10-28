def generar_matriz(clave):
    # Eliminamos espacios y pasamos a mayúsculas
    clave = clave.replace(" ", "").upper()
    # Reemplazamos la J por I (regla del cifrado Playfair)
    clave = clave.replace("J", "I")

    # Creamos la lista de letras del alfabeto sin la J
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matriz = []

    # Agregamos las letras de la clave primero, sin repetir
    for letra in clave:
        if letra not in matriz and letra in alfabeto:
            matriz.append(letra)

    # Agregamos el resto de las letras del alfabeto
    for letra in alfabeto:
        if letra not in matriz:
            matriz.append(letra)

    # Devolvemos la matriz en forma de lista de listas 5x5
    return [matriz[i:i+5] for i in range(0, 25, 5)]


def preparar_texto(texto):
    # Pasamos a mayúsculas y quitamos espacios
    texto = texto.replace(" ", "").upper()
    texto = texto.replace("J", "I")  # Regla Playfair

    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = ""
        if i + 1 < len(texto):
            b = texto[i + 1]
        if a == b:
            pares.append(a + "X")  # Si las letras son iguales, agregamos una X
            i += 1
        else:
            if b:
                pares.append(a + b)
                i += 2
            else:
                pares.append(a + "X")
                i += 1
    return pares


def buscar_posicion(matriz, letra):
    for i, fila in enumerate(matriz):
        for j, val in enumerate(fila):
            if val == letra:
                return i, j
    return None


def cifrar_playfair(texto, clave):
    matriz = generar_matriz(clave)
    pares = preparar_texto(texto)
    resultado = ""

    for par in pares:
        a, b = par[0], par[1]
        fila_a, col_a = buscar_posicion(matriz, a)
        fila_b, col_b = buscar_posicion(matriz, b)

        # Caso 1: mismas filas
        if fila_a == fila_b:
            resultado += matriz[fila_a][(col_a + 1) % 5]
            resultado += matriz[fila_b][(col_b + 1) % 5]

        # Caso 2: mismas columnas
        elif col_a == col_b:
            resultado += matriz[(fila_a + 1) % 5][col_a]
            resultado += matriz[(fila_b + 1) % 5][col_b]

        # Caso 3: rectángulo
        else:
            resultado += matriz[fila_a][col_b]
            resultado += matriz[fila_b][col_a]

    return resultado


# Si querés probarlo directamente desde consola, descomentá esto:
# if __name__ == "__main__":
#     texto = input("Texto a cifrar: ")
#     clave = input("Clave: ")
#     print("Texto cifrado:", cifrar_playfair(texto, clave))
