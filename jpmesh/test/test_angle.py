"""
Tests for jpmesh.angle.
"""

import unittest

import jpmesh.angle


class TestAngle(unittest.TestCase):
    """
    Tests for jpmesh.angle.Angle.
    """

    def test_normal(self):
        """
        Normal test cases.
        """
        millisecond = 3600000
        angle = jpmesh.angle.Angle.from_millisecond(millisecond)
        self.assertEqual(angle.degree, float(millisecond) / 60 / 60 / 1000)
        self.assertEqual(angle.minute, float(millisecond) / 60 / 1000)
        self.assertEqual(angle.second, float(millisecond) / 1000)
        self.assertEqual(angle.millisecond, float(millisecond))
