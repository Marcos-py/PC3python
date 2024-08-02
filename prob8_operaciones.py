# prob8
# operaciones.py
def suma(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    return "Tipo de dato no válido"
  return a + b

def resta(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    return "Tipo de dato no válido"
  return a - b

def producto(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    return "Tipo de dato no válido"
  return a * b

def division(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    return "Tipo de dato no válido"
  if b == 0:
    return "No es posible dividir entre cero"
  return a / b

