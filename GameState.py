import copy
import itertools
import random
from collections import namedtuple


class GameState():
    def __init__(self, board, utility=None, nivel=0):
        self.__board = board
        self.__utility = utility
        self.__nivel = nivel


    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, value):
        self.__board = value

    @property
    def utility(self):
        return self.__utility

    @utility.setter
    def utility(self, value):
        self.__utility = value

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, value):
        self.__nivel = value