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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]:
        return X
    if (board[0].count(X) + board[1].count(X) + board[2].count(X)) > (board[0].count(O) + board[1].count(O) + board[2].count(O)):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                available_actions.add((i,j))
    return available_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    i,j = action
    if (-1 < i < 3) or (-1 < j < 3):
        raise ValueError
    newboard[i][j]=player(board)
    return newboard

#CAN BE BETTER
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    for i in range(3):
        c=0
        # checking row
        for j in range(3):
            if board[i][j] == EMPTY:
                break
            if c == 3:
                winner = X
                break
            if board[i][j] == X:
                c+=1
        else:
            winner=O
        # checking columns
        c=0
        for j in range(3):
            if board[j][i] == EMPTY:
                break
            if c == 3:
                winner = X
                break
            if board[j][i] == X:
                c+=1
        else:
            winner=O
    
    #checking diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] is not None:
        return board[1][1]

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    available_actions = actions(board)
    if winner(board) is not None:
        return True
    if bool(available_actions) == False:
        return False


def utility(board) -> float:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        winningPlayer = winner(board)
        if winningPlayer==X:
            return 1
        elif winningPlayer==O:
            return -1
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == X:

        best_score = -math.inf
        best_action = None

        for action in actions(board):
            score = minPlayer(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    else:

        best_score = math.inf
        best_action = None

        for action in actions(board):
            score = maxPlayer(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

        return best_action

def maxPlayer(board) -> float:
    """
    Returns the maximum score that can be achieved
    """
    if terminal(board):
        return utility(board)
    score = -math.inf
    for action in actions(board):
        score= max(score, minPlayer(result(board,action)))
    return score

def minPlayer(board) -> float:
    """
    Returns the maximum score that can be achieved
    """
    if terminal(board):
        return utility(board)
    score = math.inf
    for action in actions(board):
        score= min(score, maxPlayer(result(board,action)))
    return score
