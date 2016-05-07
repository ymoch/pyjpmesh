"""
Tests for jpmesh.coordinate.
"""

import unittest

from jpmesh import Coordinate


class TestCoordinate(unittest.TestCase):
    """
    Tests for jpmesh.Coordinate.
    """

    def test_operators(self):
        """
        Test for operators.
        """
        coord1 = Coordinate(lon=1.0, lat=2.0)
        coord2 = Coordinate(lon=5.0, lat=6.0)
        self.assertEqual(
            coord1 + coord2,
            Coordinate(lon=coord1.lon + coord2.lon, lat=coord1.lat + coord2.lat)
        )
        self.assertEqual(
            coord1 - coord2,
            Coordinate(lon=coord1.lon - coord2.lon, lat=coord1.lat - coord2.lat)
        )
        self.assertEqual(
            coord1 * 2, Coordinate(lon=coord1.lon * 2, lat=coord1.lat * 2))
        self.assertEqual(
            coord1 / 2, Coordinate(lon=coord1.lon / 2, lat=coord1.lat / 2))
        self.assertEqual(
            coord1 / 2.0,
            Coordinate(lon=coord1.lon / 2.0, lat=coord1.lat / 2.0))
        self.assertEqual(
            coord1 // 2, Coordinate(lon=coord1.lon // 2, lat=coord1.lat // 2))
        self.assertEqual(+coord1, Coordinate(lon=+coord1.lon, lat=+coord1.lat))
        self.assertEqual(-coord1, Coordinate(lon=-coord1.lon, lat=-coord1.lat))
        self.assertNotEqual(coord1, coord2)

        # Call __div__ and __truediv__ expressly.
        self.assertEqual(
            coord1.for_test_div(2.0),
            Coordinate(lon=coord1.lon / 2.0, lat=coord1.lat / 2.0))
        self.assertEqual(
            coord1.for_test_truediv(2.0),
            Coordinate(lon=coord1.lon / 2.0, lat=coord1.lat / 2.0))
