# Prob3
import math

class CIRCULO:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    return math.pi * self.radio**2

# Crear dos objetos de tipo CIRCULO
circulo1 = CIRCULO(2)
circulo2 = CIRCULO(3)

# Calcular el área de cada círculo
area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

# Imprimir las áreas con un decimal
print(f"Área del círculo 1: {area1:.1f}")
print(f"Área del círculo 2: {area2:.1f}")