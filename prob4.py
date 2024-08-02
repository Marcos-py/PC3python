# Prob4
class RECTANGULO:
  def __init__(self, largo, ancho):
    self.largo = largo
    self.ancho = ancho

  def calcular_area(self):
    return self.largo * self.ancho

class CUADRADO(RECTANGULO):
  def __init__(self, lado):
    super().__init__(lado, lado)

# Crear un objeto de tipo RECTANGULO
rectangulo = RECTANGULO(3, 8)

# Crear un objeto de tipo CUADRADO
cuadrado = CUADRADO(5)

# Calcular e imprimir las áreas
print("Área del rectángulo:", rectangulo.calcular_area())
print("Área del cuadrado:", cuadrado.calcular_area())