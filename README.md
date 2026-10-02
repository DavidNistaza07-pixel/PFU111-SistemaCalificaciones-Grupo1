Sistema de Registro de Calificaciones

Proyecto individual de PFU-111 Programación Fundamental — Tema 6: Buenas prácticas en el desarrollo seguro de software.

Autor: David Abraham Apaza Nistaza — Grupo 1

Descripción

Programa de consola que registra las calificaciones de estudiantes y muestra su rendimiento académico. Resuelve el problema de que un programa que solo funciona con datos correctos puede dar resultados inválidos o detenerse cuando el usuario escribe algo inesperado. Por eso el programa valida cada dato antes de usarlo y controla los errores sin cerrarse.

Funcionalidades
Registrar el nombre de un estudiante.
Registrar tres calificaciones.
Calcular el promedio.
Determinar si el estudiante aprobó o reprobó (nota de aprobación: 51).
Mostrar los resultados.
Registrar varios estudiantes y mostrar un resumen final.
Validaciones:
Entrada                                                        	Regla
Nombre                                                         	No puede estar vacío ni tener solo espacios.
Calificaciones	                                                Deben ser números entre 0 y 100.
Respuesta para continuar	                                      Solo se acepta s o n (mayúscula o minúscula).

Si un dato no cumple la regla, el programa muestra un mensaje de error y lo solicita nuevamente.

Manejo de errores
Texto en una calificación: float() produce un ValueError. Se controla con try/except y se vuelve a pedir el dato.
Calificación fuera de rango: se detecta con una condición y se vuelve a pedir.
División entre cero: la función del promedio comprueba que haya calificaciones antes de dividir.
Entrada interrumpida (Ctrl+C / Ctrl+Z): se controlan KeyboardInterrupt y EOFError para terminar de forma ordenada mostrando el resumen.
Pruebas realizadas
N.º	Prueba	                             Entrada	                                                          Resultado
1	Datos válidos	                         Ana, 80, 75, 90	                                                  Promedio 81.67 — APROBADO
2	Calificación negativa                  -10	                                                              Mensaje de error y se pide de nuevo
3	Calificación superior al máximo	       150	                                                              Mensaje de error y se pide de nuevo
4	Nombre vacío                         	(Enter)	                                                            Mensaje de error y se pide de nuevo
5	Entrada inesperada	                   abc	                                                              Mensaje de error y se pide de nuevo
Tecnologías utilizadas
Python 3
Git
GitHub
