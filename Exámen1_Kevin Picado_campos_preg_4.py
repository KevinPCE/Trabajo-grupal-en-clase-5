#Desarrolle un programa que calcule la nota final de un estudiante en un curso

def calcular_nota_final():
# se debe ingresar el nombre del estudiante con el input
    nombre = input("Por favor ingrese su nombre: ")
# calificaciones de exámenes donde ingresamos la i para que cuente hasta 4 exámenes y se debe revisar que esté entre 0y 100
    print("\nEscriba las notas de los exámenes parciales (0-100):")
    parciales = []
    for i in range(4):
        while True:
            
                nota = float(input(f"Parcial {i+1}: "))
                if 0 <= nota <= 100:
                    parciales.append(nota)
                    break
                else:
                          print("Error: La nota debe estar entre 0 y 100.")
#se pide ingresar notas de las tareas donde se pide que sean 5  con la i y que los rangos sea de 0 a 100
    print("Escriba las notas de las tareas (0-10):")
    Tareas = []
    for i in range(5):
        while True:
            
             nota = float(input(f"tarea {i+1}: "))
             if 0 <= nota <= 10:
                    Tareas.append(nota)
                    break
             else:
                    print("Error: La nota debe estar entre 0 y 10.")
# se pide que se ponga la nota del proyecto no se utiliza el in range porque es solo una nota y se pide que sea de 0 a 100
    while True:
        
            proyecto = float(input("Escriba la nota del proyecto final (0-100): "))
            if 0 <= proyecto <= 100:
                break
            else:
                print("Error La nota debe estar entre 0 y 100.")
 # se solicita que se ingrese el resultado de la presentacion y según lo solicitado debe de ettar entre 0y100
    while True:
            presentacion = float(input("escriba la nota de la presentación oral (0-100): "))
            if 0 <= presentacion <= 100:
                break
            else:
                print("Error la nota debe estar entre 0 y 100.")
    # el promedio es la suma de los exámenes y se divide entre ellos al igual que las tareas 
    promedio_parciales = sum(parciales) / len(parciales)
    promedio_tareas = sum(Tareas) / len(Tareas)
    
    # la nota final se calcula de la suma entre la cantidad de exámenes por 0.4, kastareas se multiplica por 2 y proyevto y presentacion no se dividen ya qye es solo uno pero se multiplica por 0.3 y0.1
    nota_final = (sum(parciales) / len(parciales) * 0.4) + \
                 (sum(Tareas) / len(Tareas) * 2) + \
                 (proyecto * 0.3) + \
                 (presentacion * 0.1)
    
    #las calificaciones donde se define que para estar aprobado se debe de estar por encima del 70 y se calidica con las letras a, b,c,d,f cada una con su respectivo dato desd excelente hasta reprobado
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
    #resumen donde se dan todos los datos solicitadis y demás con slos prints  
    print("" + "="*50)
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
# Ejecuta el programa
calcular_nota_final()