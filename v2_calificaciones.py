# Sistema de Registro de Calificaciones
# Versión 2: se agrega validación de entradas y registro de varios estudiantes

continuar = "s"

while continuar == "s":
    # Validación del nombre: no debe estar vacío
    nombre = input("Ingrese el nombre del estudiante: ")
    while nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        nombre = input("Ingrese nuevamente el nombre: ")

    #Las calificaciones deben estar entre 0 y 100
    suma = 0
    for i in range(1, 4):
        calificacion = float(input("Ingrese la calificación " + str(i) + ": "))
        while calificacion < 0 or calificacion > 100:
            print("ERROR: La calificación debe estar entre 0 y 100.")
            calificacion = float(input("Ingrese nuevamente la calificación: "))
        suma = suma + calificacion

    promedio = suma / 3

    print("Estudiante:", nombre)
    print("Promedio:", round(promedio, 2))

    if promedio >= 51:
        print("Estado: APROBADO")
    else:
        print("Estado: REPROBADO")

    continuar = input("¿Desea registrar otro estudiante? (s/n): ")
