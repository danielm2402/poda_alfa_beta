class Game(object):
    # Identificar cuales son los movimientos o jugadas posibles de un jugador
    def actions(self, state):
        raise NotImplementedError

    # Ejecutar un movimiento o jugada y retornar el nuevo estado
    def result(self, state, move):
        raise NotImplementedError

    # Calcular la función de utilidad
    def utility(self, state):
        raise NotImplementedError

    # Condición de parada (profundidad, ganador )
    def terminal_test(self, state):
        return not self.actions(state)

    # Ejecutar el juego
    def play_game(self, *players):
        raise NotImplementedError
