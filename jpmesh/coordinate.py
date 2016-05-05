"""
Coordinate package.
"""

class Coordinate(object):
    """
    Coordinate class.
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
