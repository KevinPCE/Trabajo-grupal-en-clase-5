#Desarrolle un programa que calcule la nota final de un estudiante en un curso

def calcular_nota_final():
   # nombre del estudiante
    nombre = input("Por favor ingrese su nombre: ")
    
    # Validación de nombre no vacío
    #while not nombre.strip():
        #print("Error: El nombre no puede estar vacío.")
        #nombre = input("Por favor ingrese su nombre: ")
    
    # calificaciones de exámenes
    print("\nEscriba las notas de los exámenes parciales (0-100):")
    parciales = []
    for i in range(4):
        while True:
            #try:
                nota = float(input(f"Parcial {i+1}: "))
                if 0 <= nota <= 100:
                    parciales.append(nota)
                    break
                else:
                          print("Error: La nota debe estar entre 0 y 100.")
            #except ValueError:
                print("Error: Ingrese un valor numérico válido.")
    
    #calificaciones de tareas
    print("\nEscriba las notas de las tareas (0-10):")
    Tareas = []
    for i in range(5):
        while True:
            #try:
             nota = float(input(f"tarea {i+1}: "))
             if 0 <= nota <= 10:
                    Tareas.append(nota)
                    break
             else:
                    print("Error: La nota debe estar entre 0 y 10.")
            #except ValueError:
             print("Error: Ingrese un valor numérico válido.")
    
    # calificación del proyecto
    while True:
        try:
            proyecto = float(input("\nEscriba la nota del proyecto final (0-100): "))
            if 0 <= proyecto <= 100:
                break
            else:
                print("Error La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Eror Escriba un valor mumérico valido.")
    
    # calificación de presentación oral
    while True:
        #try:
            presentacion = float(input("escriba la nota de la presentación oral (0-100): "))
            if 0 <= presentacion <= 100:
                break
            else:
                print("Error la nota debe estar entre 0 y 100.")
        #except ValueError:
            print("Eror ingrese un valor numerico valido")
    
    # calcular
    promedio_parciales = sum(parciales) / len(parciales)
    promedio_tareas = sum(Tareas) / len(Tareas)
    
    # Calcular nota final con pesos expuestos en el problema
    nota_final = (sum(parciales) / len(parciales) * 0.4) + \
                 (sum(Tareas) / len(Tareas) * 2) + \
                 (proyecto * 0.3) + \
                 (presentacion * 0.1)
    
    #estado y calificación segun letras
    estado = "aprobado" if nota_final >= 70 else "reprobado"
    
    if 90 <= nota_final <= 100:
        letra = "A (excelente)"
    elif 80 <= nota_final < 90:
        letra = "B (Nnotable)"
    elif 70 <= nota_final < 80:
        letra = "C (aprobado)"
    elif 60 <= nota_final < 70:
        letra = "D (Iinsuficiente)"
    else:
        letra = "F (Reprobado)"
    
    #resumen 
    print("\n" + "="*50)
    print("Resumen".center(50))
    print("="*50)
    print(f"Nombre del estudiante: {nombre}")
    print(f"Promedio de parciales: {promedio_parciales:.2f}")
    print(f"romedio de tareas: {promedio_tareas:.2f} (convertido a escala 0-100: {promedio_tareas*10:.2f})")
    print(f"Nta del proyecto final: {proyecto:.2f}")
    print(f"Nota de la presentacn : {presentacion:.2f}")
    print("-"*50)
    print(f"NOTA FINAL: {nota_final:.2f}")
    print(f"calificación alfabetica: {letra}")
    print(f"estado: {estado}")
    print("="*50)

# Ejecutar el programa
calcular_nota_final()