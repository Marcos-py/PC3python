# Prob9
import math

class CIRCULO:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    return math.pi * self.radio**2

class RECTANGULO:
  def __init__(self, largo, ancho):
    self.largo = largo
    self.ancho = ancho

  def calcular_area(self):
    return self.largo * self.ancho

class CUADRADO(RECTANGULO):
  def __init__(self, lado):
    super().__init__(lado, lado)

def validar_numero(numero, positivo=True):
  try:
    numero = float(numero)
    if positivo and numero <= 0:
      print("El número debe ser positivo.")
      return False
    return True
  except ValueError:
    print("Ingrese un número válido.")
    return False

while True:
  print("\nMenú:")
  print("1. Calcular el área de un círculo")
  print("2. Calcular el área de un rectángulo")
  print("3. Calcular el área de un cuadrado")
  print("4. Salir")

  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    radio = input("Ingrese el radio del círculo: ")
    if validar_numero(radio):
      circulo = CIRCULO(float(radio))
      print("El área del círculo es:", circulo.calcular_area())

  elif opcion == "2":
    largo = input("Ingrese el largo del rectángulo: ")
    ancho = input("Ingrese el ancho del rectángulo: ")
    if validar_numero(largo) and validar_numero(ancho):
      rectangulo = RECTANGULO(float(largo), float(ancho))
      print("El área del rectángulo es:", rectangulo.calcular_area())

  elif opcion == "3":
    lado = input("Ingrese el lado del cuadrado: ")
    if validar_numero(lado):
      cuadrado = CUADRADO(float(lado))
      print("El área del cuadrado es:", cuadrado.calcular_area())

  elif opcion == "4":
    print("Saliendo del programa...")
    break

  else:
    print("Opción inválida. Intente nuevamente.")