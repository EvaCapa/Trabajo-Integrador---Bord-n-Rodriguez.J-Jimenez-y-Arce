import tkinter as tk
from tkinter import messagebox
from algoritmos import cesar, xor, vigenere, playfair, diffie_hellman, rsa

def abrir_algoritmo(nombre):
    ventana = tk.Toplevel()
    ventana.title(nombre)
    ventana.geometry("400x300")

    tk.Label(ventana, text=f"{nombre} - Cifrado", font=("Arial", 14, "bold")).pack(pady=10)
    
    tk.Label(ventana, text="Texto:").pack()
    entrada_texto = tk.Entry(ventana, width=40)
    entrada_texto.pack(pady=5)

    tk.Label(ventana, text="Clave:").pack()
    entrada_clave = tk.Entry(ventana, width=40)
    entrada_clave.pack(pady=5)

    resultado = tk.Text(ventana, height=5, width=40)
    resultado.pack(pady=10)

    def cifrar_texto():
        texto = entrada_texto.get()
        clave = entrada_clave.get()
        if nombre == "Cifrado César":
            res = cesar.cifrar(texto, int(clave))
        elif nombre == "Cifrado XOR":
            res = xor.cifrar(texto, clave)
        elif nombre == "Cifrado Vigenère":
            res = vigenere.cifrar(texto, clave)
        elif nombre == "Cifrado Playfair":
            res = playfair.cifrar_playfair(texto, clave)
        elif nombre == "Diffie-Hellman":
            res = diffie_hellman.calcular(texto, clave)
        elif nombre == "RSA":
            res = rsa.calcular(texto, clave)
        else:
            res = "Algoritmo no encontrado"

        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, res)

    tk.Button(ventana, text="Cifrar", command=cifrar_texto).pack(pady=5)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=5)

def mostrar_interfaz():
    root = tk.Tk()
    root.title("Elegí el algoritmo")
    root.geometry("350x400")

    tk.Label(root, text="Elegí un algoritmo de cifrado", font=("Arial", 16, "bold")).pack(pady=15)

    tk.Button(root, text="Cifrado César", width=25, command=lambda: abrir_algoritmo("Cifrado César")).pack(pady=5)
    tk.Button(root, text="Cifrado XOR", width=25, command=lambda: abrir_algoritmo("Cifrado XOR")).pack(pady=5)
    tk.Button(root, text="Cifrado Vigenère", width=25, command=lambda: abrir_algoritmo("Cifrado Vigenère")).pack(pady=5)
    tk.Button(root, text="Cifrado Playfair", width=25, command=lambda: abrir_algoritmo("Cifrado Playfair")).pack(pady=5)
    tk.Button(root, text="Diffie-Hellman", width=25, command=lambda: abrir_algoritmo("Diffie-Hellman")).pack(pady=5)
    tk.Button(root, text="RSA", width=25, command=lambda: abrir_algoritmo("RSA")).pack(pady=5)

    root.mainloop()
