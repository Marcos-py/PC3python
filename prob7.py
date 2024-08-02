# prob7
# La clase Punto es una plantilla para crear objetos que representan puntos en un espacio bidimensional.
# Se tiene los atributos: x e y, que almacenan las coordenadas del punto.
# Se va a utilizar la Clase Punto para calcular la distancia del origen (0, 0) hasta el punto ingresado (x, y)
class Punto:
    def __init__(self):
        x = input("Ingresa la coordenada x del punto: ")
        y = input("Ingresa la coordenada y del punto: ")
        self.x = float(x)
        self.y = float(y)
# Se calcula la distancia del origen a la coordenada ingresada (x, y)
    def distancia_al_origen(self):
        return (self.x**2 + self.y**2) ** 0.5  # Calcula la raíz cuadrada
punto = Punto()
distancia = punto.distancia_al_origen()
# print("La distancia al origen es:", distancia)
print("La distancia al origen es: {:.2f}".format(distancia))  # Formato con dos decimales