# Prob2
def procesar_calificaciones():
  while True:
    try:
      calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
      calificaciones_lista = calificaciones_str.split(",")
      calificaciones = [int(calificacion.strip()) for calificacion in calificaciones_lista]
      print("Calificaciones:", calificaciones)
      break
    except ValueError:
      print("Error: Ingrese calificaciones válidas separadas por comas.")

procesar_calificaciones()