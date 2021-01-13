"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = moves_counter(board)
    
    if count["x"] == count["o"]:
        return "X"
    return "O"


def moves_counter(board):
    """
    """
    count = {"x": 0, "o": 0, "empty": 0}

    for row in board:
        for move in row:
            if move == "X": 
                count["x"] += 1
            elif move == "O":
                count["o"] += 1
            else:
                count["empty"] += 1
    return count


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if board[i][j] is not None:
        raise NameError('Invalid action')

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    triplets = get_triplets(board)

    for triplet in triplets:
        if triplet.count("X") == 3:
            return "X"
        elif triplet.count("O") == 3:
            return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = moves_counter(board)
    
    if not count["empty"]:
        return True
    if count["x"] < 3 and count["o"] < 3:
        return False
    
    triplets = get_triplets(board)
    
    for triplet in triplets:
        if triplet.count("X") == 3 or triplet.count("O") == 3:
            return True
    return False
    
def get_triplets(board):
    """
    """
    triplets = list()
    diag_down = list()
    diag_up = list()

    for i in range(3):
        triplets.append((board[i][0], board[i][1], board[i][2]))
        triplets.append((board[0][i], board[1][i], board[2][i]))
        diag_down.append(board[i][i])
        diag_up.append(board[i][(i - 2) * -1])
    triplets.append(diag_down)
    triplets.append(diag_up)
    
    return triplets


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0


def empty(board):
    """
    """
    for row in board:
        for move in row:
            if move:
                return False
    return True

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if empty(board):
        i = random.randrange(3)
        j = random.randrange(3)
        return (i, j)

    if terminal(board):
        return None

    values = dict()
    
    if player(board) == "X":
        for action in actions(board):
            values[action] = min_value(result(board, action))
        return max(values, key=values.get)
    else:
        for action in actions(board):
            values[action] = max_value(result(board, action))
        return min(values, key=values.get)


def max_value(board):
    """
    """
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    """
    """
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value

# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     if empty(board):
#         i = random.randrange(3)
#         j = random.randrange(3)
#         return (i, j)

#     if terminal(board):
#         return None

#     values = dict()
    
#     if player(board) == "X":
#         for action in actions(board):
#             values[action] = min_value(result(board, action))
#         return max(values, key=values.get)
#     else:
#         for action in actions(board):
#             values[action] = max_value(result(board, action))
#         return min(values, key=values.get)


# def max_value(board):
#     """
#     """
#     if terminal(board):
#         return utility(board)
#     value = -math.inf
#     for action in actions(board):
#         value = max(value, min_value(result(board, action)))
#     return value


# def min_value(board):
#     """
#     """
#     if terminal(board):
#         return utility(board)
#     value = math.inf
#     for action in actions(board):
#         value = min(value, max_value(result(board, action)))
#     return value