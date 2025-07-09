import tkinter as tk
from tkinter import messagebox

# Preguntas, opciones y respuestas correctas
lista_preguntas = [
    "¿Qué tipo de datos devuelve la función len() en Python?",
    "¿Cómo se comenta una sola línea de código en Python?",
    "¿Qué hace la instrucción return dentro de una función en Python?",
    "¿Qué pasa si no se deja espacio dentro de una función en Python?",
    "¿Qué significa Float en Python?",
    "¿Para qué se utiliza el def?",
    "¿Qué función se utiliza para mostrar texto en la consola en Python?",
    "¿Cómo se define una lista en Python?",
    "¿Qué método se usa para añadir un elemento al final de una lista?",
    "¿Qué operador se usa para la potencia en Python?"
]

lista_opciones = [
    ["float", "int", "str"],
    ["/* comentario */", "// comentario", "# comentario"],
    ["Termina el programa", "Devuelve un valor", "Repite un ciclo"],
    ["El código funciona normal", "Da un error al ejecutar", "Solo se salta esa parte"],
    ["Números decimales", "Números enteros", "Letras"],
    ["Imprimir una variable", "Crear una suma", "Definir una función"],
    ["print()", "echo()", "display()"],
    ["Con corchetes []", "Con llaves {}", "Con paréntesis ()"],
    [".append()", ".add()", ".insert()"],
    ["^", "**", "*"]
]

respuestas_correctas = [1, 2, 1, 1, 0, 2, 0, 0, 0, 1]

# Variables globales
numero_pregunta = 0
puntaje = 0
nombre = ""

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Quiz de Python")
ventana_principal.geometry("600x400")

opcion_elegida = tk.IntVar()

# Limpiar ventana
def limpiar_ventana():
    for elemento in ventana_principal.winfo_children():
        elemento.destroy()

# Iniciar quiz
def empezar_quiz():
    global nombre
    nombre = entrada_nombre.get()
    if nombre.strip() == "":
        messagebox.showerror("Error", "Por favor escribe tu nombre.")
    else:
        mostrar_pregunta_actual()

# Mostrar pregunta actual
def mostrar_pregunta_actual():
    limpiar_ventana()
    global numero_pregunta, opcion_elegida

    if numero_pregunta < len(lista_preguntas):
        tk.Label(ventana_principal, text=f"Pregunta {numero_pregunta + 1} de 10", font=("Arial", 14)).pack(pady=10)
        tk.Label(ventana_principal, text=lista_preguntas[numero_pregunta], font=("Arial", 12), wraplength=500).pack(pady=10)

        opcion_elegida.set(-1)

        for i in range(3):
            tk.Radiobutton(
                ventana_principal,
                text=lista_opciones[numero_pregunta][i],
                variable=opcion_elegida,
                value=i,
                font=("Arial", 11)
            ).pack(anchor="w", padx=100)

        tk.Button(ventana_principal, text="Responder", command=verificar_respuesta).pack(pady=20)
    else:
        mostrar_resultado()

# Verificar respuesta
def verificar_respuesta():
    global numero_pregunta, puntaje
    eleccion = opcion_elegida.get()

    if eleccion == -1:
        messagebox.showwarning("Advertencia", "Debes elegir una opción.")
        return

    if eleccion == respuestas_correctas[numero_pregunta]:
        puntaje += 1
        messagebox.showinfo("Correcto", "¡Respuesta correcta!")
    else:
        correcta = lista_opciones[numero_pregunta][respuestas_correctas[numero_pregunta]]
        messagebox.showinfo("Incorrecto", f"Respuesta incorrecta.\nLa correcta era: {correcta}")

    numero_pregunta += 1
    mostrar_pregunta_actual()

# Mostrar resultado final
def mostrar_resultado():
    limpiar_ventana()
    tk.Label(ventana_principal, text="¡Has terminado el quiz!", font=("Arial", 16)).pack(pady=20)
    tk.Label(ventana_principal, text=f"{nombre}, tu puntaje fue:", font=("Arial", 14)).pack()
    tk.Label(ventana_principal, text=f"{puntaje} de 10", font=("Arial", 24)).pack(pady=10)
    tk.Button(ventana_principal, text="Volver a empezar", command=mostrar_inicio).pack(pady=20)

# Pantalla de inicio
def mostrar_inicio():
    global numero_pregunta, puntaje
    numero_pregunta = 0
    puntaje = 0
    limpiar_ventana()

    tk.Label(ventana_principal, text="Bienvenido al Quiz de Python", font=("Arial", 16)).pack(pady=20)
    tk.Label(ventana_principal, text="Escribe tu nombre:").pack()
    global entrada_nombre
    entrada_nombre = tk.Entry(ventana_principal)
    entrada_nombre.pack(pady=10)
    tk.Button(ventana_principal, text="Comenzar", command=empezar_quiz).pack(pady=10)

# Iniciar la app
mostrar_inicio()
ventana_principal.mainloop()