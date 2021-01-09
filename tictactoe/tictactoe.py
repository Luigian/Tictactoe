"""
Tic Tac Toe Player
"""

import math
import copy

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
    # return [["O", "X", EMPTY],
    #         ["X", "O", EMPTY],
    #         ["O", "X", EMPTY]]


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


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     print(board)
    
#     moves = actions(board)
#     for move in moves:
#         print(move)
    
#     scores = dict()
#     print("---------------")
#     for move in moves:
#         scores[move] = 0
#     print(scores)
#     print("---------------")
#     for move in moves:
#         new_board = result(board, move)
#         print(new_board)
#         if terminal(new_board):
#             scores[move] += utility(new_board)
#     print(scores)
    
#     v = list(scores.values())
#     maxi = max(v)
#     mini = min(v)
#     k = list(scores.keys())
#     if player(board) == "X":
#         return k[v.index(maxi)]
#     else:
#         return k[v.index(mini)]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
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

# def mini_max(board):
#     """
#     """
#     print(board)
    
#     moves = actions(board)
#     for move in moves:
#         print(move)
    
#     scores = dict()
#     print("---------------")
#     for move in moves:
#         scores[move] = 0
#     print(scores)
#     print("---------------")
    
#     for move in moves:
#         helper(board, move, scores, move)
#     print(scores)
    
#     v = list(scores.values())
#     maxi = max(v)
#     mini = min(v)
#     k = list(scores.keys())
#     if player(board) == "X":
#         return k[v.index(maxi)]
#     else:
#         return k[v.index(mini)]

# def helper(board, move, scores, parent):
#     new_board = result(board, move)
#     print(new_board)
#     if not terminal(new_board):
#         emps = actions(new_board)
#         for emp in emps:
#             helper(new_board, emp, scores, parent)
#     else:
#         scores[parent] += utility(new_board)
#         print(scores)
