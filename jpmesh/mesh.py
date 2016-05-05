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
    CODE_PATTERN = re.compile(r'^([0-9]{2})([0-9]{2})$')
    SIZE = Coordinate(lon=Angle.from_minute(60), lat=Angle.from_minute(40))

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
                'Invalid longitude number: {0:d}'.format(lon_number))
        if lat_number < 0 or lat_number >= 100:
            raise ValueError(
                'Invalid latitude number: {0:d}'.format(lat_number))

        code = '{0:2d}{1:2d}'.format(lat_number, lon_number)
        south_west = Coordinate(
            lon=Angle.from_degree(lon_number + 100),
            lat=Angle.from_minute(lat_number * 40))
        JapanMesh.__init__(self, code, south_west)

    @staticmethod
    def from_code(code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = FirstMesh.CODE_PATTERN.match(code)
        if not matches:
            raise ValueError('Invalid 1st mesh code: {0}'.format(code))
        lat_number = int(matches.group(1))
        lon_number = int(matches.group(2))
        return FirstMesh(lon_number, lat_number)

    @staticmethod
    def from_coordinate(coord):
        """
        Create an instance from a coordinate.

        :param coord: A coordinate.
        """
        lon_number = int(coord.lon.degree) - 100
        lat_number = int(coord.lat.degree * 1.5)
        return FirstMesh(lon_number, lat_number)


class SecondMesh(JapanMesh):
    """
    2nd mesh (about 10km square).
    """
    CODE_PATTERN = re.compile(r'^([0-9]{4})-?([0-9])([0-9])$')
    SIZE = FirstMesh.SIZE / 8

    def __init__(self, first_mesh, lon_number, lat_number):
        """
        Initialize.

        Note: Calling from_code() or from_coordinate() instead of __init__
              is recommended.

        :param first_mesh: A first mesh.
        :param lon_number: A longitude number for 1st meshes.
        :param lat_number: A latitude number for 1st meshes.

        When the 2nd mesh code is '533945',
        the `lat_number` is 4 and the `lon_number` is 5.
        """
        if lon_number < 0 or lon_number >= 8:
            raise ValueError(
                'Invalid longitude number: {0:d}'.format(lon_number))
        if lat_number < 0 or lat_number >= 8:
            raise ValueError(
                'Invalid latitude number: {0:d}'.format(lat_number))

        code = '{0}{1:1d}{2:1d}'.format(first_mesh.code, lat_number, lon_number)
        south_west = first_mesh.south_west + Coordinate(
            lon=self.SIZE.lon * lon_number, lat=self.SIZE.lat * lat_number)
        JapanMesh.__init__(self, code, south_west)

    @staticmethod
    def from_code(code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = SecondMesh.CODE_PATTERN.match(code)
        if not matches:
            raise ValueError('Invalid 2nd mesh code: {0}'.format(code))
        first_mesh = FirstMesh.from_code(matches.group(1))
        lat_number = int(matches.group(2))
        lon_number = int(matches.group(3))
        return SecondMesh(first_mesh, lon_number, lat_number)

    @staticmethod
    def from_coordinate(coord):
        """
        Create an instance from a coordinate.

        :param coord: A coordinate.
        """
        first_mesh = FirstMesh.from_coordinate(coord)
        remaining = coord - first_mesh.south_west
        lon_number = int(remaining.lon.ratio_in(SecondMesh.SIZE.lon))
        lat_number = int(remaining.lat.ratio_in(SecondMesh.SIZE.lat))
        return SecondMesh(first_mesh, lon_number, lat_number)


class ThirdMesh(JapanMesh):
    """
    3rd mesh (about 1km square).
    """
    CODE_PATTERN = re.compile(r'^([0-9]{4}-?[0-9]{2})-?([0-9])([0-9])$')
    SIZE = SecondMesh.SIZE / 10

    def __init__(self, second_mesh, lon_number, lat_number):
        """
        Initialize.

        Note: Calling from_code() or from_coordinate() instead of __init__
              is recommended.

        :param second_mesh: A second mesh.
        :param lon_number: A longitude number for 1st meshes.
        :param lat_number: A latitude number for 1st meshes.

        When the 3rd mesh code is '53394501',
        the `lat_number` is 0 and the `lon_number` is 1.
        """
        if lon_number < 0 or lon_number >= 10:
            raise ValueError(
                'Invalid longitude number: {0:d}'.format(lon_number))
        if lat_number < 0 or lat_number >= 10:
            raise ValueError(
                'Invalid latitude number: {0:d}'.format(lat_number))

        code = '{0}{1:1d}{2:1d}'.format(
            second_mesh.code, lat_number, lon_number)
        south_west = second_mesh.south_west + Coordinate(
            lon=self.SIZE.lon * lon_number, lat=self.SIZE.lat * lat_number)
        JapanMesh.__init__(self, code, south_west)

    @staticmethod
    def from_code(code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = ThirdMesh.CODE_PATTERN.match(code)
        if not matches:
            raise ValueError('Invalid 3rd mesh code: {0}'.format(code))
        second_mesh = SecondMesh.from_code(matches.group(1))
        lat_number = int(matches.group(2))
        lon_number = int(matches.group(3))
        return ThirdMesh(second_mesh, lon_number, lat_number)

    @staticmethod
    def from_coordinate(coord):
        """
        Create an instance from a coordinate.

        :param coord: A coordinate.
        """
        second_mesh = SecondMesh.from_coordinate(coord)
        remaining = coord - second_mesh.south_west
        lon_number = int(remaining.lon.ratio_in(ThirdMesh.SIZE.lon))
        lat_number = int(remaining.lat.ratio_in(ThirdMesh.SIZE.lat))
        return ThirdMesh(second_mesh, lon_number, lat_number)
