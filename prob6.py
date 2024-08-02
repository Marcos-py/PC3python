# Prob6
class Producto:
  def __init__(self, nombre, precio, año):
    self.nombre = nombre
    self.precio = precio
    self.año = año

  def __str__(self):
    return f"{self.nombre} - ${self.precio} - {self.año}"

class Catalogo:
  def __init__(self):
    self.productos = []

  def agregar_producto(self, producto):
    self.productos.append(producto)

  def mostrar_productos(self):
    for producto in self.productos:
      print(producto)

  def filtrar_por_año(self, año):
    for producto in self.productos:
      if producto.año == año:
        print(producto)

  def filtrar_por_precio(self, precio_max):
    for producto in self.productos:
      if producto.precio <= precio_max:
        print(producto)

# Crear un catálogo
catalogo = Catalogo()

# Crear productos
producto1 = Producto("Laptop", 1200, 2023)
producto2 = Producto("Tablet", 300, 2022)
producto3 = Producto("Mouse", 25, 2023)

# Agregar productos al catálogo
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

# Mostrar todos los productos
print("Todos los productos:")
catalogo.mostrar_productos()

# Filtrar productos por año
print("\nProductos del año 2023:")
catalogo.filtrar_por_año(2023)

# Filtrar productos por precio
print("\nProductos con precio menor o igual a $500:")
catalogo.filtrar_por_precio(500)