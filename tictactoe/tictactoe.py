"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]
    return [["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "X"]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = moves_counter(board)
    
    if count["x"] == count["o"]:
        return "X"
    return "O"


def moves_counter(board):
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
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    diag_down = list()
    diag_up = list()
    triplets = list()

    count = moves_counter(board)
    if not count["empty"]:
        return True
    if count["x"] < 3 and count["o"] < 3:
        return False
    
    for i in range(3):
        triplets.append((board[i][0], board[i][1], board[i][2]))
        triplets.append((board[0][i], board[1][i], board[2][i]))
        diag_down.append(board[i][i])
        diag_up.append(board[i][(i - 2) * -1])
    triplets.append(diag_down)
    triplets.append(diag_up)
    
    for triplet in triplets:
        if triplet.count("X") == 3 or triplet.count("O") == 3:
            return True
    return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
