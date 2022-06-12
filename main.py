from Go import Go
from GameState import GameState
import numpy as np


def alpha_beta_search(state, game):
    # Functions used by alpha_beta
    def max_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state)
        v = -np.inf
        for a in game.actions(state, 1):
            v = max(v, min_value(game.result(state, a, 2), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state)
        v = np.inf
        for a in game.actions(state, 2):
            v = min(v, max_value(game.result(state, a, 1), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alpha_beta_search:
    best_score = -np.inf
    beta = np.inf
    best_action = None
    print(game.actions(state, 2))
    for a in game.actions(state, 2):
        newstate = game.result(state, a, 2)

        v = min_value(newstate, best_score, beta)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action


go=Go()
state=GameState([
2,2,2,2,2,2,2,2,2, #d
2,0,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2, #D
2,1,1,1,1,1,1,1,2,
2,2,2,2,2,2,2,2,2
])
"""
"""
#go.utility(state)
#print(go.actions(state, 2))

#comp=alpha_beta_search(state,go)
#print(comp)
"""

#print(go.actions(state))
go.utility(state)
"""
"""
print(go.checkLibertades(29,[
0,0,0,0,0,0,0,0,0,
0,2,2,2,0,0,0,0,0,
2,2,2,2,2,0,0,0,0,
2,2,0,2,2,0,0,0,0,
2,2,2,2,0,0,0,0,0,
0,2,2,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0
]))

#state=GameState([2,-1,-1,-1,1,2,-1,-1,1])


print(checkLibertades(30, [
0,0,0,0,0,0,0,0,0,
0,1,1,1,0,0,0,0,0,
1,2,2,2,1,0,0,0,0,
1,2,0,2,1,0,0,0,0,
1,2,2,1,0,0,0,0,0,
0,1,1,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0
]))
"""
"""
result = []
checkEncerrados([19], [
0,0,0,0,0,0,0,0,0,
0,1,1,1,0,0,0,0,0,
1,0,2,2,0,0,0,0,0,
1,2,2,2,1,0,0,0,0,
1,2,2,1,0,0,0,0,0,
0,1,1,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0
],19,result)

print(all(result))

#comp=alpha_beta_search(state,tictactoe)
#print(comp)

"""

go=Go()
state=GameState([
2,2,2,2,2,2,2,2,2, #d
2,0,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2,
2,1,1,1,1,1,1,1,2, #D
2,1,1,1,1,1,1,1,2,
2,2,2,2,2,2,2,2,2
])

print(go.actions(state,2))