def generar_matriz(clave):
    clave = clave.upper().replace("J", "I")
    matriz = []
    for c in clave:
        if c not in matriz and c.isalpha():
            matriz.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matriz:
            matriz.append(c)
    return [matriz[i:i+5] for i in range(0, 25, 5)]

def preparar_texto(texto):
    texto = texto.upper().replace("J", "I")
    texto = "".join([c for c in texto if c.isalpha()])
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = texto[i + 1] if i + 1 < len(texto) else "X"
        if a == b:
            pares.append((a, "X"))
            i += 1
        else:
            pares.append((a, b))
            i += 2
    return pares

def buscar_pos(matriz, letra):
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == letra:
                return i, j
    return None

def cifrar_playfair(texto, clave):
    matriz = generar_matriz(clave)
    pares = preparar_texto(texto)
    resultado = ""
    for a, b in pares:
        fila_a, col_a = buscar_pos(matriz, a)
        fila_b, col_b = buscar_pos(matriz, b)
        if fila_a == fila_b:
            resultado += matriz[fila_a][(col_a + 1) % 5]
            resultado += matriz[fila_b][(col_b + 1) % 5]
        elif col_a == col_b:
            resultado += matriz[(fila_a + 1) % 5][col_a]
            resultado += matriz[(fila_b + 1) % 5][col_b]
        else:
            resultado += matriz[fila_a][col_b]
            resultado += matriz[fila_b][col_a]
    return resultado

def descifrar_playfair(texto, clave):
    matriz = generar_matriz(clave)
    pares = preparar_texto(texto)
    resultado = ""
    for a, b in pares:
        fila_a, col_a = buscar_pos(matriz, a)
        fila_b, col_b = buscar_pos(matriz, b)
        if fila_a == fila_b:
            resultado += matriz[fila_a][(col_a - 1) % 5]
            resultado += matriz[fila_b][(col_b - 1) % 5]
        elif col_a == col_b:
            resultado += matriz[(fila_a - 1) % 5][col_a]
            resultado += matriz[(fila_b - 1) % 5][col_b]
        else:
            resultado += matriz[fila_a][col_b]
            resultado += matriz[fila_b][col_a]
    return resultado
