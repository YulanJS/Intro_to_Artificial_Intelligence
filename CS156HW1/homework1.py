# -----------------------------------------------------------------------------
# Name:        homework1
# Purpose:     Practice writing Python functions
#
# Author: Yulan Jin
# -----------------------------------------------------------------------------
"""
Implement some helper functions that will be useful in subsequent assignments
"""


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


def max_distance(point1, other_points):
    """
    Find the maximum Manhattan distance from point1 to the other points
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param other_points(tuple of tuples) representing several points in a 
    plane 
    :return: (integer) maximum Manhattan distance from point1 to the other 
    points
    """
    # Enter your code here and remove the pass statement below
    if other_points:
        return max(manhattan_distance(point1, a_point) for a_point in other_points)
    else:
        return 0


def closest_point(point1, other_points):
    """
    Find the coordinates of the closest point to point1
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param other_points(tuple of tuples) representing several points i a plane 
    :return: (tuple) the coordinates of the closest point to point1

    """
    # Enter your code here and remove the pass statement below
    if other_points:
        return min(other_points, key=lambda a_point: manhattan_distance(point1, a_point))
    else:
        return None


def farthest_points_distance(points):
    """
    Find the maximum Manhattan distance between all the points given
    :param other_points(tuple of tuples) representing several points in a 
    plane 
    :return: (integer) maximum Manhattan distance between any two points
    """
    # Enter your code here and remove the pass statement below
    if points:
        return max(max_distance(a_point, points) for a_point in points)
    else:
        return 0
