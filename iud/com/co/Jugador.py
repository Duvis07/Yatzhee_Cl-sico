class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntuacion = 0

    def actualizar_puntuacion(self, puntos):
        self.puntuacion += puntos
