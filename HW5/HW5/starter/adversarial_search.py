# -----------------------------------------------------------------------------
# Name:     adversarial_search
# Purpose:  Homework5 - Implement adversarial search algorithms
#
# Author:
#
# -----------------------------------------------------------------------------
"""
Adversarial search algorithms implementation

Your task for homework 5 is to implement:
1.  minimax
2.  alphabeta
3.  abdl (alpha beta depth limited)
"""
import random
import sys

def rand(game_state):
    """
    Generate a random move.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the random move
    """
    found = False
    while not found:
        row = random.randint(0, game_state.size - 1)
        col = random.randint(0, game_state.size - 1)
        if game_state.available(row,col):
            found = True
    return row, col


def minimax(game_state):
    """
    Find the best move for our AI agent by applying the minimax algorithm
    (searching the entire tree from the current game state)
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    raise NotImplementedError

def value(game_state, player):
    """
    Calculate the minimax value for any state under the given agent's control
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    pass

def max_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    pass

def min_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    pass



def alphabeta(game_state):
    """
    Find the best move for our AI agent by applying the minimax algorithm
    with alpha beta pruning.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    raise NotImplementedError


def abvalue(game_state, player, alpha, beta):
    """
    Calculate the minimax value for any state under the given agent's control
    using alpha beta pruning
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    pass


def abmax_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    pass


def abmin_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    pass


def abdl(game_state, depth):
    """
    Find the best move for our AI agent by limiting the alpha beta search to
    the given depth and using the evaluation function game_state.eval()
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    raise NotImplementedError



def abvalue_dl(game_state, player, alpha, beta, depth):
    """
    Calculate the utility for any state under the given agent's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) utility of that state
    """
    # Enter your code here and remove the pass statement below
    pass


def abmax_value_dl(game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Max's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    pass


def abmin_value_dl( game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Min's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    pass

