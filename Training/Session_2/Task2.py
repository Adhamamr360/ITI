from math import inf as infinity
from random import choice

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score

def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state

def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP) or not empty_cells(state)

def empty_cells(state):
    return [[i, j] for i, row in enumerate(state) for j, cell in enumerate(row) if cell == 0]

def valid_move(x, y):
    return [x, y] in empty_cells(board)

def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False

def minimax(state, depth, player, alpha, beta):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player, alpha, beta)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score  # min value
            beta = min(beta, best[2])

        if beta <= alpha:
            break
    return best

def ai_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP, -infinity, infinity)
        x, y = move[0], move[1]

    set_move(x, y, COMP)

def human_turn(x, y):
    return set_move(x, y, HUMAN)

def reset_game():
    global board
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
