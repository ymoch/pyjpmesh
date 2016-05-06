"""
Mesh package.
"""

import re

from jpmesh.coordinate import Coordinate
from jpmesh.angle import Angle

class JapanMesh(object):
    """
    Japan mesh base class.
    """
    def __init__(self, code, south_west):
        """
        Initialize

        :param code: The mesh code.
        :param south_west: The coordinate at the south-west border.
        """
        self.__code = code
        self.__south_west = south_west

    @property
    def code(self):
        """
        Returns the mesh code.
        """
        return self.__code

    @property
    def south_west(self):
        """
        Returns the coordinate at the south-west border.
        """
        return self.__south_west


class FirstMesh(JapanMesh):
    """
    1st mesh (about 80km square).
    """
    code_pattern_re = re.compile(r'^([0-9]{2})([0-9]{2})$')

    @staticmethod
    def size():
        """
        Returns the mesh size.
        """
        return Coordinate(lon=Angle.from_minute(60), lat=Angle.from_minute(40))

    @staticmethod
    def code_pattern():
        """
        Returns the mesh code pattern.
        """
        return r'[0-9]{4}'

    def __init__(self, lon_number, lat_number):
        """
        Initialize.

        Note: Calling from_code() or from_coordinate() instead of __init__
              is recommended.

        :param lon_number: A longitude number for 1st meshes.
        :param lat_number: A latitude number for 1st meshes.

        When the 1st mesh code is '5339',
        the `lat_number` is 39 and the `lon_number` is 39.
        """
        if lon_number < 0 or lon_number >= 100:
            raise ValueError(
                'Invalid longitude number for {0}: {1:d}'
                .format(self.__class__.__name__, lon_number))
        if lat_number < 0 or lat_number >= 100:
            raise ValueError(
                'Invalid latitude number for {0}: {1:d}'
                .format(self.__class__.__name__, lat_number))

        code = '{0:2d}{1:2d}'.format(lat_number, lon_number)
        south_west = Coordinate(
            lon=Angle.from_degree(lon_number + 100),
            lat=Angle.from_minute(lat_number * 40))
        JapanMesh.__init__(self, code, south_west)

    @classmethod
    def from_code(cls, code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = cls.code_pattern_re.match(code)
        if not matches:
            raise ValueError(
                'Invalid mesh code for {0}: {1}'
                .format(cls.__name__, code))
        lat_number = int(matches.group(1))
        lon_number = int(matches.group(2))
        return cls(lon_number, lat_number)

    @classmethod
    def from_coordinate(cls, coord):
        """
        Create an instance from a coordinate.

        :param coord: A coordinate.
        """
        lon_number = int(coord.lon.degree) - 100
        lat_number = int(coord.lat.degree * 1.5)
        return cls(lon_number, lat_number)


class NumberDividedMesh(JapanMesh):
    """
    Mesh class divided with number (which are 0-9).

    Note: Class variables below must be implemented dynamically:
        - ParentMesh: The divided parent mesh.
        - divide_num: The number of division [0-9].
    """
    ParentMesh = None
    divide_num = None

    @classmethod
    def size(cls):
        """
        Returns the mesh size.
        """
        return cls.ParentMesh.size() / cls.divide_num

    @classmethod
    def code_pattern(cls):
        """
        Returns the mesh code pattern.
        """
        return cls.ParentMesh.code_pattern() + r'-?[0-9]{2}'

    @classmethod
    def code_match_pattern(cls):
        """
        Returns the mesh code pattern for matching.
        """
        return r'^({0})-?([0-{1:d}])([0-{1:d}])$'.format(
            cls.ParentMesh.code_pattern(), cls.divide_num - 1)

    def __init__(self, parent_mesh, lon_number, lat_number):
        """
        Initialize.

        Note: Calling from_code() or from_coordinate() instead of __init__
              is recommended.

        :param parent_mesh: A parent mesh.
        :param lon_number: A longitude number for 1st meshes.
        :param lat_number: A latitude number for 1st meshes.

        In the case of a 2nd mesh '5339-45',
        the `lat_number` is 4 and the `lon_number` is 5.
        """
        if lon_number < 0 or lon_number >= self.divide_num:
            raise ValueError(
                'Invalid longitude number for {0}: {1:d}'
                .format(self.__class__.__name__, lon_number))
        if lat_number < 0 or lat_number >= self.divide_num:
            raise ValueError(
                'Invalid latitude number for {0}: {1:d}'
                .format(self.__class__.__name__, lat_number))

        size = self.size()
        code = '{0}{1:1d}{2:1d}'.format(
            parent_mesh.code, lat_number, lon_number)
        south_west = parent_mesh.south_west + Coordinate(
            lon=size.lon * lon_number, lat=size.lat * lat_number)
        JapanMesh.__init__(self, code, south_west)

    @classmethod
    def from_code(cls, code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = re.match(cls.code_match_pattern(), code)
        if not matches:
            raise ValueError(
                'Invalid mesh code for {0}: {1}'
                .format(cls.__name__, code))
        parent_mesh = cls.ParentMesh.from_code(matches.group(1))
        lat_number = int(matches.group(2))
        lon_number = int(matches.group(3))
        return cls(parent_mesh, lon_number, lat_number)

    @classmethod
    def from_coordinate(cls, coord):
        """
        Create an instance from a coordinate.

        :param coord: A coordinate.
        """
        parent_mesh = cls.ParentMesh.from_coordinate(coord)
        remaining = coord - parent_mesh.south_west
        size = cls.size()
        lon_number = int(remaining.lon.ratio_in(size.lon))
        lat_number = int(remaining.lat.ratio_in(size.lat))
        return cls(parent_mesh, lon_number, lat_number)


class IndexDividedMesh(JapanMesh):
    """
    Mesh class divided with indexes (which are 1-4).

    Note: Class variables below must be implemented dynamically:
        - ParentMesh: The divided parent mesh.
    """
    ParentMesh = None

    @classmethod
    def size(cls):
        """
        Returns the mesh size.
        """
        return cls.ParentMesh.size() / 2

    @classmethod
    def code_pattern(cls):
        """
        Returns the mesh code pattern.
        """
        return cls.ParentMesh.code_pattern() + r'-?[1-4]'

    @classmethod
    def code_match_pattern(cls):
        """
        Returns the mesh code pattern for matching.
        """
        return r'^({0})-?([1-4])$'.format(cls.ParentMesh.code_pattern())

    def __init__(self, parent_mesh, div_index):
        """
        Initialize.

        Note: Calling from_code() or from_coordinate() instead of __init__
              is recommended.

        :param parent_mesh: A parent mesh.
        :param div_index: A divide index (see below).

        In the case of a half mesh '5339-45-00-1',
        the `div_index` is the last 1.
        """
        if div_index < 1 or div_index > 4:
            raise ValueError(
                'Invalid divide index for {0}: {1:d}'
                .format(self.__class__.__name__, div_index))

        code = '{0}{1:1d}'.format(parent_mesh.code, div_index)
        size = self.size()
        south_west = parent_mesh.south_west + Coordinate(
            lon=size.lon * ((div_index - 1) % 2),
            lat=size.lat * ((div_index - 1) // 2)
        )
        JapanMesh.__init__(self, code, south_west)

    @classmethod
    def from_code(cls, code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = re.match(cls.code_match_pattern(), code)
        if not matches:
            raise ValueError(
                'Invalid mesh code for {0}: {1}'
                .format(cls.__name__, code))
        parent_mesh = cls.ParentMesh.from_code(matches.group(1))
        div_index = int(matches.group(2))
        return cls(parent_mesh, div_index)

    @classmethod
    def from_coordinate(cls, coord):
        """
        Create an instance from a coordinate.

        :param coord: A coordinate.
        """
        parent_mesh = cls.ParentMesh.from_coordinate(coord)
        remaining = coord - parent_mesh.south_west
        size = cls.size()
        lon_number = int(remaining.lon.ratio_in(size.lon))
        lat_number = int(remaining.lat.ratio_in(size.lat))
        div_index = lat_number * 2 + lon_number + 1
        return cls(parent_mesh, div_index)


def create_number_devided_mesh(name, parent_mesh, divide_num):
    """
    Create a class derived from NumberDividedMesh.

    :param name: The class name.
    :param parent_mesh: The parent mesh class.
    :param divide_num: The number of division.
    """
    return type(name, (NumberDividedMesh,), {
        'ParentMesh': parent_mesh,
        'divide_num': divide_num,
    })


def create_index_divided_mesh(name, parent_mesh):
    """
    Create a class derived from IndexDividedMesh.

    :param name: The class name.
    :param parent_mesh: The parent mesh class.
    """
    return type(name, (IndexDividedMesh,), {
        'ParentMesh': parent_mesh,
    })


# Ignore name errors because these names are classes.
SecondMesh = create_number_devided_mesh('SecondMesh', FirstMesh, 8) # pylint: disable=C0103
ThirdMesh = create_number_devided_mesh('ThirdMesh', SecondMesh, 10) # pylint: disable=C0103
HalfMesh = create_index_divided_mesh('HalfMesh', ThirdMesh) # pylint: disable=C0103
QuarterMesh = create_index_divided_mesh('QuarterMesh', HalfMesh) # pylint: disable=C0103
OneEighthMesh = create_index_divided_mesh('QuarterMesh', QuarterMesh) # pylint: disable=C0103
