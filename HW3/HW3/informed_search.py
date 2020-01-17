# -----------------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 3 - Implement astar and some heuristics
#
# Author:
#
# -----------------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation 

Your task for homework 3 is to implement:
1.  astar
2.  single_heuristic 
3.  better_heuristic
4.  gen_heuristic  
"""
import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    # Enter your code here and remove the pass statement below
    pass


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*. 
    Running A* with this null heuristic, gives us uniform cost search
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    Fill in the docstring here
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: 
    """
    # Enter your code here and remove the pass statement below
    pass


def better_heuristic(state, problem):
    """
    Fill in the docstring here
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: 
    """
    # Enter your code here and remove the pass statement below
    pass


def gen_heuristic(state, problem):
    """
    Fill in the docstring here
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: 
    """
    # Enter your code here and remove the pass statement below
    pass