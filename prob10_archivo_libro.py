# prob10
# archivo libro.py

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} (Autor: {self.autor}, ISBN: {self.isbn})"