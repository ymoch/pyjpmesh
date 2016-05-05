"""
Tests for jpmesh.coordinate.
"""

import unittest

from nose.tools import eq_

from jpmesh.mesh import FirstMesh, SecondMesh, ThirdMesh
from jpmesh.coordinate import Coordinate
from jpmesh.angle import Angle


def _test_from_code(test_class, org_code, code, south_west):
    """
    Tests for SomeMesh.from_code.
    """
    mesh = test_class.from_code(org_code)
    eq_(mesh.code, code)
    eq_(mesh.south_west, south_west)


def _test_from_coordinate(test_class, code, south_west):
    """
    Tests for SomeMesh.from_coordinate.
    """
    mesh = test_class.from_coordinate(south_west)
    eq_(mesh.code, code)
    eq_(mesh.south_west, south_west)


class TestFirstMesh(unittest.TestCase):
    """
    Tests for jpmesh.coordinate.FirstMesh.
    """
    ORG_CODE = '5339'
    CODE = ORG_CODE
    SOUTH_WEST = Coordinate(
        lon=Angle.from_millisecond(500400000.0),
        lat=Angle.from_millisecond(127200000.0))

    def test_from_code(self):
        """
        Test for jpmesh.coordinate.FirstMesh.from_code.
        """
        _test_from_code(FirstMesh, self.ORG_CODE, self.CODE, self.SOUTH_WEST)

    def test_from_coordinate(self):
        """
        Test for jpmesh.coordinate.FirstMesh.from_coordinate.
        """
        _test_from_coordinate(FirstMesh, self.CODE, self.SOUTH_WEST)


class TestSecondMesh(unittest.TestCase):
    """
    Tests for jpmesh.coordinate.SecondMesh.
    """
    ORG_CODE = '5339-45'
    CODE = '533945'
    SOUTH_WEST = Coordinate(
        lon=Angle.from_millisecond(502650000.0),
        lat=Angle.from_millisecond(128400000.0))

    def test_from_code(self):
        """
        Test for jpmesh.coordinate.SecondMesh.from_code.
        """
        _test_from_code(SecondMesh, self.ORG_CODE, self.CODE, self.SOUTH_WEST)

    def test_from_coordinate(self):
        """
        Test for jpmesh.coordinate.SecondMesh.from_coordinate.
        """
        _test_from_coordinate(SecondMesh, self.CODE, self.SOUTH_WEST)


class TestThirdMesh(unittest.TestCase):
    """
    Tests for jpmesh.coordinate.ThirdMesh.
    """
    ORG_CODE = '5339-35-96'
    CODE = '53393596'
    SOUTH_WEST = Coordinate(
        lon=Angle.from_millisecond(502920000.0),
        lat=Angle.from_millisecond(128370000.0))

    def test_from_code(self):
        """
        Test for jpmesh.coordinate.ThirdMesh.from_code.
        """
        _test_from_code(ThirdMesh, self.ORG_CODE, self.CODE, self.SOUTH_WEST)

    def test_from_coordinate(self):
        """
        Test for jpmesh.coordinate.ThirdMesh.from_coordinate.
        """
        _test_from_coordinate(ThirdMesh, self.CODE, self.SOUTH_WEST)
