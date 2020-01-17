# -----------------------------------------------------------------------------
# Name:         testhomework1
# Purpose:      Test functions for homework 1
#
# Author:       Rula Khayrallah
# -----------------------------------------------------------------------------
import homework1
import unittest


class TestHomework1(unittest.TestCase):
    """
    Test case for the 4 functions
    """

    def test_manhattan_distance(self):
        """ test the manhattan_distance function"""
        self.assertEqual(homework1.manhattan_distance((2, 7), (1, 3)), 5)
        self.assertEqual(homework1.manhattan_distance((0, 1), (1, 3)), 3)
        self.assertEqual(homework1.manhattan_distance((2, 7), (4, 2)), 7)
        self.assertEqual(homework1.manhattan_distance((5, 2), (4, 4)), 3)
        self.assertEqual(homework1.manhattan_distance((1, 5), (1, 5)), 0)


    def test_max_distance(self):
        """ test the max_distance function"""
        self.assertEqual(homework1.max_distance((3, 4),
                                                ((1, 2), (4, 5),
                                                 (4, 3), (9, 2), (0, 1))),
                        8)
        self.assertEqual(homework1.max_distance((3, 4), ()), 0)
        self.assertEqual(homework1.max_distance((3, 4),
                                                ((1, 2), (4, 5), (4, 3), (0, 1))),
                         6)
        self.assertEqual(homework1.max_distance((3, 4),
                                                ((1, 2), (4, 5), (4, 3))),

                        4)

    def test_closest_point(self):
        """ test the closest_point function"""
        self.assertEqual(homework1.closest_point((3, 4),
                                                 ((1, 2),
                                                  (4, 5),
                                                  (9, 2),
                                                  (0, 1))),
                         (4, 5))
        self.assertIsNone(homework1.closest_point((3, 4), ()))
        self.assertEqual(homework1.closest_point((3, 4),
                                                 ((1, 2),
                                                  (4, 5),
                                                  (3, 4),
                                                  (0, 1))),
                         (3, 4))
        self.assertEqual(homework1.closest_point((3, 4),
                                                 ((1, 2),
                                                  (3, 3),
                                                  (4, 3))),
                         (3, 3))

    def test_farthest_points_distance(self):
        """ test the farthest_points_distance function"""
        self.assertEqual(homework1.farthest_points_distance(((1, 2),
                                                             (4, 3),
                                                             (9, 2),
                                                             (4, 5),
                                                             (0, 1))),
                         10)

        self.assertEqual(homework1.farthest_points_distance(()), 0)


if __name__ == '__main__':
    unittest.main()
