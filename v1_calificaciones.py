# Sistema de Registro de Calificaciones
# Version inicial

nombre = input("Ingrese el nombre del estudiante: ")

c1 = float(input("Ingrese la calificacion 1: "))
c2 = float(input("Ingrese la calificacion 2: "))
c3 = float(input("Ingrese la calificacion 3: "))

promedio = (c1 + c2 + c3) / 3

print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 51:
    print("Estado: APROBADO")
else:
    print("Estado: REPROBADO")
 