"""
Tests for jpmesh.coordinate.
"""

import unittest

from nose.tools import ok_, eq_
from nose.tools import raises

from jpmesh import FirstMesh, SecondMesh, ThirdMesh
from jpmesh import HalfMesh, QuarterMesh, OneEighthMesh
from jpmesh import parse_mesh_code
from jpmesh import Coordinate
from jpmesh import Angle


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
    Tests for jpmesh.FirstMesh.
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

    @staticmethod
    @raises(ValueError)
    def test_invalid_lat_number():
        """
        An invalid latitude number causes a ValueError.
        """
        FirstMesh(100, 0)

    @staticmethod
    @raises(ValueError)
    def test_invalid_lon_number():
        """
        An invalid longitude number causes a ValueError.
        """
        FirstMesh(0, 100)

    @staticmethod
    @raises(ValueError)
    def test_invalid_code():
        """
        Invalid mesh code causes a ValueError.
        """
        FirstMesh.from_code('53393')


class TestSecondMesh(unittest.TestCase):
    """
    Tests for jpmesh.SecondMesh.
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

    @raises(ValueError)
    def test_invalid_lat_number(self):
        """
        An invalid latitude number causes a ValueError.
        """
        SecondMesh(self.SOUTH_WEST, 9, 0)

    @raises(ValueError)
    def test_invalid_lon_number(self):
        """
        An invalid longitude number causes a ValueError.
        """
        SecondMesh(self.SOUTH_WEST, 0, 9)

    @staticmethod
    @raises(ValueError)
    def test_invalid_code():
        """
        Invalid mesh code causes a ValueError.
        """
        SecondMesh.from_code('5339356')


class TestThirdMesh(unittest.TestCase):
    """
    Tests for jpmesh.ThirdMesh.
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

    @raises(ValueError)
    def test_invalid_lat_number(self):
        """
        An invalid latitude number causes a ValueError.
        """
        ThirdMesh(self.SOUTH_WEST, 10, 0)

    @raises(ValueError)
    def test_invalid_lon_number(self):
        """
        An invalid longitude number causes a ValueError.
        """
        ThirdMesh(self.SOUTH_WEST, 0, 10)

    @staticmethod
    @raises(ValueError)
    def test_invalid_code():
        """
        Invalid mesh code causes a ValueError.
        """
        ThirdMesh.from_code('533935379')


class TestHalfMesh(unittest.TestCase):
    """
    Tests for jpmesh.HalfMesh.
    """
    ORG_CODE = '5339-35-96-4'
    CODE = '533935964'
    SOUTH_WEST = Coordinate(
        lon=Angle.from_millisecond(502942500.0),
        lat=Angle.from_millisecond(128385000.0))

    def test_from_code(self):
        """
        Test for jpmesh.coordinate.HalfMesh.from_code.
        """
        _test_from_code(HalfMesh, self.ORG_CODE, self.CODE, self.SOUTH_WEST)

    def test_from_coordinate(self):
        """
        Test for jpmesh.coordinate.HalfMesh.from_coordinate.
        """
        _test_from_coordinate(HalfMesh, self.CODE, self.SOUTH_WEST)

    @raises(ValueError)
    def test_invalid_div_index(self):
        """
        An invalid division index causes a ValueError.
        """
        HalfMesh(self.SOUTH_WEST, 5)

    @staticmethod
    @raises(ValueError)
    def test_invalid_code():
        """
        Invalid mesh code causes a ValueError.
        """
        HalfMesh.from_code('53393537')


class TestQuarterMesh(unittest.TestCase):
    """
    Tests for jpmesh.QuarterMesh.
    """
    ORG_CODE = '5339-35-96-1-4'
    CODE = '5339359614'
    SOUTH_WEST = Coordinate(
        lon=Angle.from_millisecond(502931250.0),
        lat=Angle.from_millisecond(128377500.0))

    def test_from_code(self):
        """
        Test for jpmesh.coordinate.QuarterMesh.from_code.
        """
        _test_from_code(QuarterMesh, self.ORG_CODE, self.CODE, self.SOUTH_WEST)

    def test_from_coordinate(self):
        """
        Test for jpmesh.coordinate.QuarterMesh.from_coordinate.
        """
        _test_from_coordinate(QuarterMesh, self.CODE, self.SOUTH_WEST)

    # Skip the error variations because these are common to HalfMesh.


class TestOneEighthMesh(unittest.TestCase):
    """
    Tests for jpmesh.OneEighthMesh.
    """
    ORG_CODE = '5339-35-96-1-1-4'
    CODE = '53393596114'
    SOUTH_WEST = Coordinate(
        lon=Angle.from_millisecond(502925625.0),
        lat=Angle.from_millisecond(128373750.0))

    def test_from_code(self):
        """
        Test for jpmesh.coordinate.OneEighthMesh.from_code.
        """
        _test_from_code(OneEighthMesh, self.ORG_CODE, self.CODE, self.SOUTH_WEST)

    def test_from_coordinate(self):
        """
        Test for jpmesh.coordinate.OneEighthMesh.from_coordinate.
        """
        _test_from_coordinate(OneEighthMesh, self.CODE, self.SOUTH_WEST)

    # Skip the error variations because these are common to HalfMesh.


class TestParseMeshCode(unittest.TestCase):
    """
    Tests for jpmesh.parse_mesh_code.
    """
    @staticmethod
    def test_validcode():
        """
        Returns correct meshes if valid mesh codes are given.
        """
        ok_(isinstance(parse_mesh_code('5339'), FirstMesh))
        ok_(isinstance(parse_mesh_code('533935'), SecondMesh))
        ok_(isinstance(parse_mesh_code('53393573'), ThirdMesh))
        ok_(isinstance(parse_mesh_code('533935731'), HalfMesh))
        ok_(isinstance(parse_mesh_code('5339357312'), QuarterMesh))
        ok_(isinstance(parse_mesh_code('53393573123'), OneEighthMesh))

    @staticmethod
    @raises(ValueError)
    def test_empty_code():
        """
        Raises ValueError if empty mesh codes are given.
        """
        isinstance(parse_mesh_code(''), FirstMesh)

    @staticmethod
    @raises(ValueError)
    def test_invalid_code():
        """
        Raises ValueError if invalid mesh codes are given.
        """
        isinstance(parse_mesh_code('533935731234'), FirstMesh)
