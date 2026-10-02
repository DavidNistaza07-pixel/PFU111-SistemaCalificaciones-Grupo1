# ============================================
# Sistema de Registro de Calificaciones
# Estudiante: Apaza Nistaza David Abraham (Grupo 1)
# PFU-111 - Programación Fundamental Semana 9 
# Versión final: código organizado en modulos
# ============================================

NOTA_MINIMA, NOTA_MAXIMA, NOTA_APROBACION, CANTIDAD_NOTAS = 0, 100, 51, 3


def pedir_nombre():
    """Pide el nombre hasta que no esté vacío."""
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            return nombre
        print("ERROR: El nombre no puede estar vacío.")


def pedir_calificacion(numero):
    """Pide una calificación válida entre 0 y 100."""
    while True:
        try:
            val = input(f"Ingrese la calificación {numero}: ").strip()
            calificacion = float(val)
            if NOTA_MINIMA <= calificacion <= NOTA_MAXIMA:
                return calificacion
            print(f"ERROR: Debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}.")
        except ValueError:
            print("ERROR: Debe ingresar un número, no texto.")


def preguntar_continuar():
    """Pregunta si se registra otro estudiante (s/n)."""
    while True:
        resp = input("\n¿Desea registrar otro estudiante? (s/n): ").strip().lower()
        if resp in ("s", "n"):
            return resp == "s"
        print("ERROR: Responda solamente con s o n.")


def main():
    print(" BIENVENIDO AL SISTEMA DE REGISTRO DE CALIFICACIONES ")
    estudiantes = []

    while True:
        print()

        nombre = pedir_nombre()

        calificaciones = []
        for i in range(1, CANTIDAD_NOTAS + 1):
            calificaciones.append(pedir_calificacion(i))


        promedio = sum(calificaciones) / len(calificaciones)
        estado = "APROBADO" if promedio >= NOTA_APROBACION else "REPROBADO"

        print("\n--- RESULTADO ---")
        print(f"Estudiante     : {nombre}")
        print(f"Calificaciones : {calificaciones}")
        print(f"Promedio       : {promedio:.2f}")
        print(f"Estado         : {estado}")

        estudiantes.append((nombre, promedio, estado))

        if not preguntar_continuar():
            break

    if estudiantes:
        print("\n===== RESUMEN DE ESTUDIANTES =====")
        for nom, prom, est in estudiantes:
            print(f"{nom:<20} {prom:>6.2f}   {est}")
        print(f"Total registrados: {len(estudiantes)}")

    print("Programa finalizado.")


if __name__ == "__main__":
    main()