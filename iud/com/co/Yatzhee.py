from iud.com.co.Dados import Dados
from iud.com.co.Jugador import Jugador
import matplotlib.pyplot as plt


class Yatzhee:
    def __init__(self):
        self.dados = Dados()
        self.jugadores = [Jugador("Jugador 1"), Jugador("Jugador 2")]
        self.turno_actual = 0

    def turno(self, jugador):
        print(f"\nTurno de {jugador.nombre}")
        dados_fijos = []
        for _ in range(3):
            dados_a_lanzar = [i for i in range(5) if i not in dados_fijos]
            self.dados.lanzar_dados(dados_a_lanzar)
            print(f"Dados: {self.dados.mostrar_dados()}")
            if dados_a_lanzar:
                mantener = input("¿Qué dados quieres mantener? (índices separados por espacios): ")
                if mantener:
                    dados_fijos = list(map(int, mantener.split()))
        puntos = sum(self.dados.dados)
        print(f"Puntuación de este turno: {puntos}")
        jugador.actualizar_puntuacion(puntos)

    def jugar(self):
        for turno in range(3):
            print(f"\nTurno {turno + 1}")
            for jugador in self.jugadores:
                self.turno(jugador)
        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("\nResultados finales:")
        for jugador in self.jugadores:
            print(f"{jugador.nombre}: {jugador.puntuacion} puntos")

        nombres_jugadores = [jugador.nombre for jugador in self.jugadores]
        puntajes = [jugador.puntuacion for jugador in self.jugadores]
        plt.bar(nombres_jugadores, puntajes, color=['blue', 'green'])
        plt.xlabel('Jugador')
        plt.ylabel('Puntuación')
        plt.title('Puntuaciones Finales')
        plt.show()

        if self.jugadores[0].puntuacion > self.jugadores[1].puntuacion:
            print("¡Jugador 1 gana!")
        elif self.jugadores[0].puntuacion < self.jugadores[1].puntuacion:
            print("¡Jugador 2 gana!")
        else:
            print("¡Es un empate!")


if __name__ == "__main__":
    yatzhee = Yatzhee()
    yatzhee.jugar()
