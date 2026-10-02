# Sistema de Registro de Calificaciones
# Versión 3: se corrigen los errores detectados durante las pruebas
#   - La presencia de texto en una calificación ya no detiene el programa
#   - Un nombre con solo espacios ya no se acepta
#   - La respuesta s/n se valida y acepta mayúsculas

continuar = "s"

while continuar == "s":
    # El nombre: no debe estar vacío ni tener solo espacios
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    while nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        nombre = input("Ingrese nuevamente el nombre: ").strip()

    # Las calificaciones deben ser números y estar en un rango entre 0 y 100
    suma = 0
    for i in range(1, 4):
        mensaje = "Ingrese la calificación " + str(i) + ": "
        valida = False
        while not valida:
            try:
                calificacion = float(input(mensaje))
                if calificacion < 0 or calificacion > 100:
                    print("ERROR: La calificación debe estar entre 0 y 100.")
                else:
                    valida = True
            except ValueError:
                print("ERROR: Debe ingresar un número, no texto.")
            mensaje = "Ingrese nuevamente la calificación: "
        suma = suma + calificacion

    promedio = suma / 3

    print("Estudiante:", nombre)
    print("Promedio:", round(promedio, 2))

    if promedio >= 51:
        print("Estado: APROBADO")
    else:
        print("Estado: REPROBADO")

    # Validación de la respuesta para continuar
    continuar = input("¿Desea registrar otro estudiante? (s/n): ").strip().lower()
    while continuar != "s" and continuar != "n":
        print("ERROR: Responda solamente con s o n.")
        continuar = input("¿Desea registrar otro estudiante? (s/n): ").strip().lower()
