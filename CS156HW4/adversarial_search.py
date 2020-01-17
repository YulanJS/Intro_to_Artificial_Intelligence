# -----------------------------------------------------------------------------
# Name:     adversarial_search
# Purpose:  Homework5 - Implement adversarial search algorithms
#
# Author: Yulan Jin
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
import math


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
        if game_state.available(row, col):
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
    # make a function according to a known function with 2 variables, using lambda
    return max((move for move in game_state.possible_moves()),
        key=lambda move: value(game_state.successor(move, "AI"), "user"))


def value(game_state, player):
    """
    Calculate the minimax value for any state under the given agent's control
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    # whoever wins is 1? No. Previously, I wrote if game_state.is_win(player): return 1
    # only three terminal results: AI wins: 1, AI loses: -1, AI ties: 0
    # the value for terminal states don't depend on who controls the game at that moment
    if game_state.is_win("AI"):
        return 1
    if game_state.is_win("user"):
        return -1
    if game_state.is_tie():
        return 0
    # neither player wins nor a tie, in the process, who controls the game matters, use max or min function
    if player == "AI":
        return max_value(game_state)
    else:  # "user"
        return min_value(game_state)


def max_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    # v = -math.inf
    # all the successor states
    return max(value(game_state.successor(move, "AI"), "user") for move in game_state.possible_moves())


def min_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    return min(value(game_state.successor(move, "user"), "AI") for move in game_state.possible_moves())


def alphabeta(game_state):
    """
    Find the best move for our AI agent by applying the minimax algorithm
    with alpha beta pruning.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    return max((move for move in game_state.possible_moves()),
               key=lambda move: abvalue(game_state.successor(move, "AI"), "user", -math.inf, math.inf))


def abvalue(game_state, player, alpha, beta):
    """
    Calculate the minimax value for any state under the given agent's control
    using alpha beta pruning
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    if game_state.is_win("AI"):
        return 1
    if game_state.is_win("user"):
        return -1
    if game_state.is_tie():
        return 0
    # neither player wins nor a tie, in the process, who controls the game matters, use max or min function
    if player == "AI":
        return abmax_value(game_state, alpha, beta)
    else:  # "user"
        return abmin_value(game_state, alpha, beta)


def abmax_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    v = -math.inf
    for move in game_state.possible_moves():
        v = max(v, abvalue(game_state.successor(move, "AI"), "user", alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def abmin_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    v = math.inf
    for move in game_state.possible_moves():
        v = min(v, abvalue(game_state.successor(move, "user"), "AI", alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def abdl(game_state, depth):
    """
    Find the best move for our AI agent by limiting the alpha beta search to
    the given depth and using the evaluation function game_state.eval()
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    return max((move for move in game_state.possible_moves()),
               key=lambda move: abvalue_dl(game_state.successor(move, "AI"), "user", -math.inf, math.inf, depth))


def abvalue_dl(game_state, player, alpha, beta, depth):
    """
    Calculate the utility for any state under the given agent's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: GameState object - state may be terminal or non-terminal
    :param player: (string) 'user' or 'AI' - AI is max
    :return: (integer) utility of that state
    """
    # slides said iterative deepening
    # Enter your code here and remove the pass statement below
    # only non-terminal states needs estimation showing how close to win or lose.
    # Terminal states are determined already.
    # win: most desirable: higher values than all middle states
    if game_state.is_win("AI"):
        return game_state.size * 2 + 2
    if game_state.is_win("user"):
        return -game_state.size * 2 - 2
    if game_state.is_tie():
        return 0
    if depth == 0:
        return game_state.eval()
    # neither player wins nor a tie, in the process, who controls the game matters, use max or min function
    if player == "AI":
        return abmax_value_dl(game_state, alpha, beta, depth)
    else:  # "user"
        return abmin_value_dl(game_state, alpha, beta, depth)


def abmax_value_dl(game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Max's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    v = -math.inf
    for move in game_state.possible_moves():
        v = max(v, abvalue_dl(game_state.successor(move, "AI"), "user", alpha, beta, depth - 1))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def abmin_value_dl(game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Min's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    v = math.inf
    for move in game_state.possible_moves():
        v = min(v, abvalue_dl(game_state.successor(move, "user"), "AI", alpha, beta, depth - 1))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

