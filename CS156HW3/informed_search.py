# -----------------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 3 - Implement astar and some heuristics
#
# Author: Yulan Jin
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
import math

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
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue()
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root, heuristic(state, problem))
    while True:
        if fringe.empty():
            return None  # Failure - fringe is empty and no solution was found
        node = fringe.pop()
        if problem.is_goal(node.state):
            # print(heuristic(node.state, problem)) should be 0
            return node.solution()
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.successors(
                    node.state):
                # action_cost: parent's single step cost
                child_node = data_structures.Node(child_state, node, action)
                child_node.cumulative_cost = node.cumulative_cost + action_cost
                # set the child's cumulative_cost here
                fringe.push(child_node, child_node.cumulative_cost + heuristic(child_state, problem))
                # should be accumulated cost from the root


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
    Use Manhattan_distance as heuristic because it is admissible and consistent
    Note that there is only one medal in the maze
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: manhattan distance to the only medal
    """
    # Enter your code here and remove the pass statement below
    # current position state[0]
    # only one medal, problem.start_state()[1] (a tuple of all medals' positions)
    return manhattan_distance(state[0], problem.start_state()[1][0])


# helper function for single_heuristic
def manhattan_distance(point1, point2):
    """
    Compute the Manhattan distance between two points.
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param point2 (tuple) representing the coordinates of a point in a plane
    :return: (integer)  The Manhattan distance between the two points
    """
    # Enter your code here and remove the pass statement below
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def better_heuristic(state, problem):
    """
    estimates the remaining cost from current position to the goal
    remember that different directions have different cost and x,y = position means row, col
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: 
    """
    # Enter your code here and remove the pass statement below
    return least_cost_remained(state[0], problem.start_state()[1][0])


# helper function
# estimate the cost remained to the goal, and use this as a heuristic funciton
def least_cost_remained(point1, point2):
    # x,y means row,col(Not mathematical coordinates)
    x1, y1 = point1
    x2, y2 = point2
    if y2 > y1:
        return 5 * (y2 - y1) + 2 * abs(x1 - x2)
    else:
        return 1 * (y1 - y2) + 2 * abs(x1 - x2)


def gen_heuristic(state, problem):
    """
    use least_cost_remained, getting the max "distance" between current position and all remaining medals
    an optimistic and consistent heuristic
    :param 
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest 
    :return: the "distance" between current position and the "farthest" medal
    # no matter how we choose the optimal path, we have to get the farthest medal. Going through
    # other points results in a total distance larger than the distance to the farthest medal.
    """
    # Enter your code here and remove the pass statement below
    position, medals_position = state
    # medals_position only record all the remaining medals' positions
    if medals_position:
        return max(least_cost_remained(position, medal_position) for medal_position in medals_position)
    else:
        return 0
