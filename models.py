# models.py

class Roupa:
    def __init__(self, nome, categoria, tamanho):
        self.nome = nome
        self.categoria = categoria
        self.tamanho = tamanho

    def __repr__(self):
        return f"{self.nome} ({self.categoria}, Tamanho: {self.tamanho})"
