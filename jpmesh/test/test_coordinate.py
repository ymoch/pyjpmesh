"""
Tests for jpmesh.coordinate.
"""

import unittest

from jpmesh.coordinate import Coordinate


class TestCoordinate(unittest.TestCase):
    """
    Tests for jpmesh.coordinate.Coordinate.
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
