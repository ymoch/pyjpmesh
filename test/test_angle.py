"""
Tests for jpmesh.angle.
"""

import unittest

from jpmesh import Angle


class TestAngle(unittest.TestCase):
    """
    Tests for jpmesh.Angle.
    """

    def test_properties(self):
        """
        Test for properties.
        """
        millisecond = 3600000
        angle = Angle.from_millisecond(millisecond)
        self.assertEqual(angle.degree, float(millisecond) / 60 / 60 / 1000)
        self.assertEqual(angle.minute, float(millisecond) / 60 / 1000)
        self.assertEqual(angle.second, float(millisecond) / 1000)
        self.assertEqual(angle.millisecond, float(millisecond))

    def test_operators(self):
        """
        Test for operators.
        """
        angle1 = Angle.from_millisecond(1.0)
        angle2 = Angle.from_millisecond(1.0)
        angle3 = Angle.from_millisecond(2.0)
        self.assertEqual(
            (angle1 + angle2).degree, angle1.degree + angle2.degree)
        self.assertEqual(
            (angle1 - angle2).degree, angle1.degree - angle2.degree)
        self.assertEqual((angle1 * 2).degree, angle1.degree * 2)
        self.assertEqual((angle1 / 2).degree, angle1.degree / 2)
        self.assertEqual((angle1 / 2.0).degree, angle1.degree / 2.0)
        self.assertEqual((+angle1).degree, +angle1.degree)
        self.assertEqual((-angle1).degree, -angle1.degree)
        self.assertEqual(abs(angle1).degree, abs(angle1.degree))
        self.assertTrue(angle1 == angle2)
        self.assertFalse(angle1 == angle3)
        self.assertFalse(angle1 != angle2)
        self.assertTrue(angle1 != angle3)

        # Call __div__ and __truediv__ expressly.
        self.assertEqual(
            angle1.for_test_div(2.0).degree, angle1.degree / 2.0)
        self.assertEqual(
            angle1.for_test_truediv(2.0).degree, angle1.degree / 2.0)
