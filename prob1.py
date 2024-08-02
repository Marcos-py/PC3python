# Prob1
def calcular_porcentaje():
  while True:
    try:
      entrada = input("Ingrese los valores de X/Y: ")
      X, Y = map(int, entrada.split('/'))
      if X <= Y and Y != 0:
        porcentaje = (X / Y) * 100
        if porcentaje < 1:
          print("E")
        elif porcentaje > 99:
          print("F")
        else:
          print(f"{porcentaje:.0f}%")
        break
      elif X > Y:
        raise ValueError
      elif Y == 0:
        raise ZeroDivisionError
    except ValueError:
      print("ValueError")
    except ZeroDivisionError:
      print("ZeroDivisionError")

calcular_porcentaje()