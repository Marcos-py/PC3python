# archivo main.py
from libro import Libro
from gestion import GestionBiblioteca

def main():
    biblioteca = GestionBiblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar un libro")
        print("2. Listar los libros")
        print("3. Buscar un libro por título")
        print("4. Buscar un libro por autor")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(nuevo_libro)
            print("Libro agregado correctamente.")
        elif opcion == "2":
            biblioteca.listar_libros()
        elif opcion == "3":
            titulo_buscar = input("Introduce el título a buscar: ")
            libro_encontrado = biblioteca.buscar_por_titulo(titulo_buscar)
            if libro_encontrado:
                print(f"Libro encontrado: {libro_encontrado}")
            else:
                print("Libro no encontrado.")
        elif opcion == "4":
            autor_buscar = input("Introduce el autor a buscar: ")
            libro_encontrado = biblioteca.buscar_por_autor(autor_buscar)
            if libro_encontrado:
                print(f"Libro encontrado: {libro_encontrado}")
            else:
                print("Libro no encontrado.")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()