# -----------------------------------------------------------------------------
# Name:     beliefs
# Purpose:  Homework 7
#
# Author: Yulan Jin
#
# -----------------------------------------------------------------------------
"""
Module to track the belief distribution over all possible grid positions

Your task for homework 7 is to implement:
1.  update
2.  recommend_sensing
"""
import utils

class Belief(object):
    """
    Belief class used to track the belief distribution based on the sensing
    evidence we have so far.
    Arguments:
        size (int): the number of rows/columns in the grid

    Attributes:
        open (set of tuples):  set containing all the positions that have not
            been observed so far.
        tprob (dictionary): probability distribution based on the evidence
            acquired so far.
            The keys of the dictionary are the possible grid positions
            The values represent the (conditional) probability that the
            treasure is found at that position given the evidence (sensor data)
            accumulated so far.
    """
    def __init__(self, size):
        # Initially all positions are open - have not been observed
        self.open = {(x, y) for x in range(size)
                     for y in range(size)}
        # Initialize the treasure probability to a uniform distribution
        self.tprob = {pos: 1 / (size ** 2) for pos in self.open}

    def get_beliefs(self):
        """
        Accessor method for the belief distribution
        Note: to be used in treasurehunt.py only for a cleaner interface
        You do not need to use it inside the Belief class.
        :return:
          dictionary representing the belief distribution given the evidence
          accumulated so far.
        """
        return self.tprob

    def update(self, sensor_position, color, model):
        """
        Update the belief distribution based on new evidence:  our agent
        detected the given color at sensor location: sensor_position.
        :param sensor_position: (tuple) position of the sensor
        :param color: (string) color detected
        :param model (Model object) models the relationship between the
             treasure location and the sensor data
        :return: None
        """
        # Iterate over ALL positions in the grid and update the probability
        # of finding the treasure at that position - given the new evidence
        # The probability of the evidence given the Manhattan distance to the
        # treasure may be accessed by calling model.get_pcolorgivendist.
        # Don't forget to normalize.
        # Don't forget to update self.open since sensor_position has now been
        # observed.

        # !!! update all positions instead of open positions
        # iterate over all keys
        # ??? If updating all probabilities, why need to update self.open?  What is that for? for recommend?
        sum = 0;
        for any_position in self.tprob:
            # multiply P(effect_k|cause), then normalize
            # estimate the probability of treasure in open_position given all effects
            m_dist = utils.manhattan_distance(any_position, sensor_position)
            # should be proportional to this value
            self.tprob[any_position] *= model.get_pcolorgivendist(color, m_dist)
            #sum(dict.values())
            sum += self.tprob[any_position]
        self.tprob = {k: v/sum for k,v in self.tprob.items()}
        self.open.discard(sensor_position)

    def recommend_sensing(self):
        """
        Recommend where we should take the next measurement in the grid.
        The position should be the most promising unobserved location.
        If all remaining unobserved locations have a probability of 0, return
        the unobserved location that is closest to the (observed) location with
        the highest probability.

        :return: tuple representing the position where we should take the
           next measurement
        """
        # Enter your code and remove the statement below
        # should select from unobserved location
        # unobserved = open: with largest probability
        best_unobserved = max(self.open, key=lambda position: self.tprob[position])
        # if max is 0, then unobserved ones all have zero probabilities
        if self.tprob[best_unobserved] != 0:
            return best_unobserved
        # directly using max, will return the max key in a dictionary
        # should find observed locations instead of all positions
        # all locations - unobserved locations = observed locations
        # tprob.keys() is views, which can be used as set
        best_observed = max(self.tprob.keys() - self.open, key=lambda position: self.tprob[position])
        return utils.closest_point(best_observed, self.open)
