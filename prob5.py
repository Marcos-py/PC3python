# Prob5
class ALUMNO:
  def __init__(self, nombre, numero_registro):
    self.nombre = nombre
    self.numero_registro = numero_registro

  def display(self):
    print("Nombre:", self.nombre)
    print("Número de registro:", self.numero_registro)
    print("Edad:", self.edad) # Se agregó esta línea

  def setAge(self, edad):
    self.edad = edad

  def setNota(self, notas):
    self.notas = notas

# Ejemplo de uso
alumno = ALUMNO("Juan Perez", "12345")
alumno.setAge(20)
alumno.setNota(85)
alumno.display()