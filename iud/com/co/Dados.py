import random


class Dados:
    def __init__(self):
        self.dados = [0] * 5

    def lanzar_dados(self, dados_a_lanzar=None):
        if dados_a_lanzar is None:
            dados_a_lanzar = range(5)
        for i in dados_a_lanzar:
            self.dados[i] = random.randint(1, 6)
        return self.dados

    def mostrar_dados(self):
        return " ".join(map(str, self.dados))
