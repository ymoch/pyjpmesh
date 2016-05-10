"""
Japan grid square code (JIS X 0410) utility for Python.
"""

import re


# Meta informations.
__version__ = '1.0.1'
__author__ = 'Yu Mochizuki'
__author_email__ = 'ymoch.dev@gmail.com'


def _code_pattern_regex(pattern):
    """
    Create the mesh pattern regular expression.

    :param pattern: A mesh code.
    """
    return re.compile(r'^{0}$'.format(pattern))


class Angle(object):
    """
    Angles.
    """
    def __init__(self, millisecond):
        """
        Initialize with degrees.
        """
        self.__millisecond = float(millisecond)

    @property
    def degree(self):
        """
        Get the angle in degrees.
        """
        return self.minute / 60.0

    @property
    def minute(self):
        """
        Get the angle in minutes.
        """
        return self.second / 60.0

    @property
    def second(self):
        """
        Get the angle in seconds.
        """
        return self.__millisecond / 1000.0

    @property
    def millisecond(self):
        """
        Get the angle in milliseconds.
        """
        return self.__millisecond

    def __add__(self, that):
        return Angle.from_millisecond(self.millisecond + that.millisecond)

    def __sub__(self, that):
        return Angle.from_millisecond(self.millisecond - that.millisecond)

    def __mul__(self, that):
        return Angle.from_millisecond(self.millisecond * that)

    def __div__(self, that):
        return Angle.from_millisecond(self.millisecond / that)

    def __truediv__(self, that):
        return Angle.from_millisecond(self.millisecond / that)

    def __pos__(self):
        return Angle.from_millisecond(self.millisecond)

    def __neg__(self):
        return Angle.from_millisecond(-self.millisecond)

    def __abs__(self):
        return Angle.from_millisecond(abs(self.millisecond))

    def __eq__(self, that):
        return self.millisecond == that.millisecond

    def __ne__(self, that):
        return self.millisecond != that.millisecond

    def ratio_in(self, base):
        """
        Returns the ratio of this angle in the 'base' angle.

        :param base: The 'base' angle.
        """
        return self.millisecond / base.millisecond

    @staticmethod
    def from_degree(degree):
        """
        Create from an angle in degrees.
        """
        return Angle.from_minute(float(degree) * 60.0)

    @staticmethod
    def from_minute(minute):
        """
        Create from an angle in minutes.
        """
        return Angle.from_second(float(minute) * 60.0)

    @staticmethod
    def from_second(second):
        """
        Create from an angle in seconds.
        """
        return Angle.from_millisecond(float(second) * 1000.0)

    @staticmethod
    def from_millisecond(millisecond):
        """
        Create from an angle in milliseconds.
        """
        return Angle(millisecond)

    def for_test_div(self, that):
        """
        Call __div__() expressly.
        """
        return self.__div__(that)

    def for_test_truediv(self, that):
        """
        Call __truediv__() expressly.
        """
        return self.__truediv__(that)


class Coordinate(object):
    """
    Coordinates with longitude and latitude.
    """
    def __init__(self, lon, lat):
        """
        Initialize.

        :param lon: A longitude angle.
        :param lat: A latitude angle.
        """
        self.__lon = lon
        self.__lat = lat

    @property
    def lon(self):
        """
        Get the longitude.
        """
        return self.__lon

    @property
    def lat(self):
        """
        Get the latitude.
        """
        return self.__lat

    def __add__(self, that):
        return Coordinate(lon=self.lon + that.lon, lat=self.lat + that.lat)

    def __sub__(self, that):
        return Coordinate(lon=self.lon - that.lon, lat=self.lat - that.lat)

    def __mul__(self, that):
        return Coordinate(lon=self.lon * that, lat=self.lat * that)

    def __div__(self, that):
        return Coordinate(lon=self.lon / that, lat=self.lat / that)

    def __truediv__(self, that):
        return Coordinate(lon=self.lon / that, lat=self.lat / that)

    def __floordiv__(self, that):
        return Coordinate(lon=self.lon // that, lat=self.lat // that)

    def __pos__(self):
        return Coordinate(lon=self.lon, lat=self.lat)

    def __neg__(self):
        return Coordinate(lon=-self.lon, lat=-self.lat)

    def __eq__(self, that):
        return self.lon == that.lon and self.lat == that.lat

    def __ne__(self, that):
        return not self == that

    def for_test_div(self, that):
        """
        Call __div__() expressly.
        """
        return self.__div__(that)

    def for_test_truediv(self, that):
        """
        Call __truediv__() expressly.
        """
        return self.__truediv__(that)


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


class NumberDividedMesh(JapanMesh):
    """
    Mesh class divided with number (which are 0-9).

    Note:
        Class variables below must be defined for each subclass.

        - ParentMesh: The parent mesh.
        - divide_num: The number of division for the parent mesh.
        - size: The mesh size.
        - code_pattern: The code pattern.
        - code_regex: The code regular expression
        - code_parse_regex: The regular expression for parsing mesh code.
            - The first match is the parent mesh code.
            - The second match is the latitude number.
            - The third match is the longitude number
    """
    # To improve performance,
    # these variables will be injected precalculated.
    ParentMesh = None
    divide_num = None
    size = None
    code_pattern = None
    code_regex = None
    code_parse_regex = None

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

        code = '{0}{1:01d}{2:01d}'.format(
            parent_mesh.code, lat_number, lon_number)
        south_west = parent_mesh.south_west + Coordinate(
            lon=self.size.lon * lon_number, lat=self.size.lat * lat_number)
        JapanMesh.__init__(self, code, south_west)

    @classmethod
    def from_code(cls, code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = cls.code_parse_regex.match(code)
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
        lon_number = int(remaining.lon.ratio_in(cls.size.lon))
        lat_number = int(remaining.lat.ratio_in(cls.size.lat))
        return cls(parent_mesh, lon_number, lat_number)


class IndexDividedMesh(JapanMesh):
    """
    Mesh class divided with indexes (which are 1-4).

    Note:
        Class variables below must be defined for each subclass.

        - ParentMesh: The parent mesh.
        - size: The mesh size.
        - code_pattern: The code pattern.
        - code_regex: The code regular expression
        - code_parse_regex: The regular expression for parsing mesh code.
            - The first match is the parent mesh code.
            - The second match is the divide index.
    """
    ParentMesh = None
    size = None
    code_pattern = None
    code_regex = None
    code_parse_regex = None

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

        code = '{0}{1:01d}'.format(parent_mesh.code, div_index)
        south_west = parent_mesh.south_west + Coordinate(
            lon=self.size.lon * ((div_index - 1) % 2),
            lat=self.size.lat * ((div_index - 1) // 2))
        JapanMesh.__init__(self, code, south_west)

    @classmethod
    def from_code(cls, code):
        """
        Create an instance from a mesh code.

        :param code: A mesh code.
        """
        matches = cls.code_parse_regex.match(code)
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
        lon_number = int(remaining.lon.ratio_in(cls.size.lon))
        lat_number = int(remaining.lat.ratio_in(cls.size.lat))
        div_index = lat_number * 2 + lon_number + 1
        return cls(parent_mesh, div_index)


class FirstMesh(JapanMesh):
    """
    1st mesh (about 80km square).
    """
    size = Coordinate(lon=Angle.from_minute(60), lat=Angle.from_minute(40))
    code_pattern = r'[0-9]{4}'
    code_regex = _code_pattern_regex(code_pattern)
    code_parse_regex = re.compile(r'^([0-9]{2})([0-9]{2})$')

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

        code = '{0:02d}{1:02d}'.format(lat_number, lon_number)
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
        matches = FirstMesh.code_parse_regex.match(code)
        if not matches:
            raise ValueError(
                'Invalid mesh code for {0}: {1}'
                .format(FirstMesh.__name__, code))
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


def create_number_devided_mesh(name, parent_mesh, divide_num):
    """
    Create a class derived from NumberDividedMesh.

    :param name: The class name.
    :param parent_mesh: The parent mesh class.
    :param divide_num: The number of division.
    """
    size = parent_mesh.size / divide_num
    code_pattern = parent_mesh.code_pattern + r'-?[0-9]{2}'
    code_regex = _code_pattern_regex(code_pattern)
    code_parse_regex = re.compile(
        r'^({0})-?([0-{1:d}])([0-{1:d}])$'
        .format(parent_mesh.code_pattern, divide_num - 1))

    return type(name, (NumberDividedMesh,), {
        'ParentMesh': parent_mesh,
        'divide_num': divide_num,
        'size': size,
        'code_pattern': code_pattern,
        'code_regex': code_regex,
        'code_parse_regex': code_parse_regex
    })


def create_index_divided_mesh(name, parent_mesh):
    """
    Create a class derived from IndexDividedMesh.

    :param name: The class name.
    :param parent_mesh: The parent mesh class.
    """
    size = parent_mesh.size / 2
    code_pattern = parent_mesh.code_pattern + r'-?[1-4]'
    code_regex = _code_pattern_regex(code_pattern)
    code_parse_regex = re.compile(
        r'^({0})-?([1-4])$'.format(parent_mesh.code_pattern))

    return type(name, (IndexDividedMesh,), {
        'ParentMesh': parent_mesh,
        'size': size,
        'code_pattern': code_pattern,
        'code_regex': code_regex,
        'code_parse_regex': code_parse_regex
    })


# Ignore name errors because these names are classes.
SecondMesh = create_number_devided_mesh('SecondMesh', FirstMesh, 8) # pylint: disable=C0103
ThirdMesh = create_number_devided_mesh('ThirdMesh', SecondMesh, 10) # pylint: disable=C0103
HalfMesh = create_index_divided_mesh('HalfMesh', ThirdMesh) # pylint: disable=C0103
QuarterMesh = create_index_divided_mesh('QuarterMesh', HalfMesh) # pylint: disable=C0103
OneEighthMesh = create_index_divided_mesh('OneEighthMesh', QuarterMesh) # pylint: disable=C0103

MESH_CLASSES = [
    FirstMesh, SecondMesh, ThirdMesh,
    HalfMesh, QuarterMesh, OneEighthMesh
]


def parse_mesh_code(code):
    """
    Returns the mesh instance for the given mesh code.

    :param code: A mesh code.
    """
    for mesh_class in MESH_CLASSES:
        if mesh_class.code_regex.match(code):
            return mesh_class.from_code(code)
    raise ValueError('Invalid mesh code: {0}'.format(code))
