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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = sum(row.count(X) for row in board)
    o = sum(row.count(O) for row in board)

    if x <= o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_actions.add((i, j))

    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid action: Cell is not empty")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if all(cell == X for cell in board[i]):
            return X
        if all(cell == O for cell in board[i]):
            return O
        
    transposed_board = list(zip(*board))
    for i in range(3):
        if all(cell == X for cell in transposed_board[i]):
            return X
        if all(cell == O for cell in transposed_board[i]):
            return O
    
    if all(board[i][i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)):
        return O
    if all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][2 - i] == O for i in range(3)):
        return O
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    if all(cell is not EMPTY for row in board for cell in row):
            return True
    
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        _, action = max_value(board)  # Get the best value and action
        return action
    elif player(board) == O:
        _, action = min_value(board)  # Get the best value and action
        return action


def max_value(board):
    if terminal(board):
        return utility(board), None  # Return utility value and no action

    v = float('-inf')  # Initialize to negative infinity
    best_action = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))  # Get value from min_value
        if min_val > v:
            v = min_val
            best_action = action  # Update the best action
    return v, best_action


def min_value(board):
    if terminal(board):
        return utility(board), None  # Return utility value and no action

    v = float('inf')  # Initialize to positive infinity
    best_action = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))  # Get value from max_value
        if max_val < v:
            v = max_val
            best_action = action  # Update the best action
    return v, best_action