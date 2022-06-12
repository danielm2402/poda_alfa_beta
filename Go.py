import copy
import random as rnd
from GameState import GameState

class Go():
    def __init__(self):
        self.table = [-1] * 81
        self.nivel = 4

    def actions(self, state, player):
        board = state.board
        actions = []
        for i, value in enumerate(board):
            if self.checkLibertades(i, board, player):
                actions.append(i)
            else:
                if self.checkEncerrados(board,i, player):
                    actions.append(i)
        print(actions)



        return actions

    def result(self, state, action, player):
        board = state.board
        newboard = copy.deepcopy(board)
        newboard[action] = player
        n = state.nivel + 1
        newstate = GameState(newboard, nivel=n)
        return newstate

    def utility(self, state):
        board = state.board
        points=0
        capturadaspc = 0
        fichasenpeligro= 0
        #capturadas por computadora
        for i, element in enumerate(board):
            if element == 1 and not self.checkLibertades(i,board,2):
                capturadaspc=capturadaspc+1
        points= points + (capturadaspc*7)

        newboard = copy.deepcopy(board)
        for i, element in enumerate(newboard):
            if self.checkLibertades(i, board, 1):
               newboard[i] = 1
            else:
                result = []
                self.checkEncerrados([i], board, i, result, 1)
                if (all(result)):
                    newboard[i] = 1
        # atari
        for i, element in enumerate(newboard):
            if element == 2 and not self.checkLibertades(i,board,1):
                fichasenpeligro = fichasenpeligro + 1

        points = points - fichasenpeligro

        territorio = self.casillacontrolada(board) * 3

        points = points + territorio

        return points



    def terminal_test(self, state):
        if state.nivel == self.nivel:
            return True
        else:
            return False

    def checkLibertades(self, index, board, player):
        print(index, player)
        if board[index] == 0:
            if self.checkLibertadDerecha(index, board, player) or self.checkLibertadIzquierda(index, board, player) or self.checkLibertadArriba(index,
                                                                                                                 board, player) or self.checkLibertadAbajo(
                    index, board, player):
                return True
            else:
                return False
        return False

    def checkLibertadDerecha(self,index, board, player):
        if index + 1 < 81:
            if board[index + 1] != 0:
                if board[index + 1] == player:
                    n = (index + 1) + 1
                    while n < 81:
                        if board[n] != player:
                            return False
                        elif board[n] == 0:
                            return True
                        n = n + 1
                return False
            else:
                return True
        return False

    def checkLibertadIzquierda(self,index, board, player):
        if index - 1 >= 0:
            if board[index - 1] != 0:
                if board[index - 1] == player:
                    n = (index - 1) - 1
                    while n < 81:
                        if board[n] != player:
                            return False
                        elif board[n] == 0:
                            return True
                        n = n - 1
                return False
            else:
                return True
        return False

    def checkLibertadArriba(self,index, board, player):
        if index - 9 >= 0:
            if board[index - 9] != 0:
                if board[index - 9] == player:
                    n = (index - 9) - 9
                    while n > 0:
                        if board[n] != player:
                            return False
                        elif board[n] == 0:
                            return True
                        n = n - 9
                return False
            else:
                return True
        return False



    def checkLibertadAbajo(self,index, board, player):
        if index + 9 < 81:
            if board[index + 9] != 0:
                if board[index + 9] == player:
                    n = (index + 9) + 9
                    while n < 81:
                        if board[n] != player:
                            return False
                        elif board[n] == 0:
                            return True
                        n = n + 9
                return False
            else:
                return True
        return False

    def getLeft(self,index, board):
        try:
            return {"value": board[index - 1], "index": index - 1}
        except IndexError:
            return {"value": None, "index": None}

    def getRight(self,index, board):
        try:
            return {"value": board[index + 1], "index": index + 1}
        except IndexError:
            return {"value": None, "index": None}

    def getUp(self,index, board):
        try:
            return {"value": board[index - 9], "index": index - 9}
        except IndexError:
            return {"value": None, "index": None}

    def getDown(self,index, board):
        try:
            return {"value": board[index + 9], "index": index + 9}
        except IndexError:
            return {"value": None, "index": None}

    def casillacontrolada(self, board):
        count = 0
        for i, element in enumerate(board):
            if element == 0:
                l = self.getLeft(i, board).get('value')
                r = self.getRight(i, board).get('value')
                d = self.getDown(i, board).get('value')
                u = self.getUp(i, board).get('value')
                total = [l,r,d,u]
                totalEnemy = len([x for x in total if x == 1])
                total = len([x for x in total if x == 2])
                if total>totalEnemy:
                    count = count + 1
        return count

    def checkEncerrados(self, board, index, player):
        newboard = copy.deepcopy(board)
        newboard[index] = player
        close = []
        result = []
        enemy = 1 if player == 2 else 2
        l = self.getLeft(index, board).get('index')
        r = self.getRight(index, board).get('index')
        d = self.getDown(index, board).get('index')
        u = self.getUp(index, board).get('index')
        open=[l,r,d,u]
        while len(open) != 0:
            element = open.pop(0)
            close.append(element)
            list=[]
            l = self.getLeft(element, board).get('index')
            r = self.getRight(element, board).get('index')
            d = self.getDown(element, board).get('index')
            u = self.getUp(element, board).get('index')

            if l is not None and board[l] == enemy:
                list.append(l)
            if r is not None and board[r] == enemy:
                list.append(r)
            if d is not None and board[d] == enemy:
                list.append(d)
            if u is not None and board[u] == enemy:
                list.append(u)

            newlist = copy.copy(list)
            for i, a in enumerate(list):
                if a in open:
                    newlist.remove(a)
                if a in close:
                    newlist.remove(a)

            open.extend(newlist)
        for element in close:
            if self.checkLibertadDerecha(element, newboard, player) or self.checkLibertadIzquierda(element, newboard,
                                                                                                   player) or self.checkLibertadArriba(
                    element, newboard, player) or self.checkLibertadAbajo(element, newboard, player):
                result.append(True)
            else:
                result.append(False)
        print(result)
        return not any(result)