"""
Angle package.
"""

class Angle(object):
    """
    Angles.
    """
    def __init__(self, degree):
        """
        Initialize with degrees.
        """
        self.__degree = float(degree)

    @property
    def degree(self):
        """
        Get the angle in degrees.
        """
        return self.__degree

    @property
    def minute(self):
        """
        Get the angle in minutes.
        """
        return self.degree * 60.0

    @property
    def second(self):
        """
        Get the angle in seconds.
        """
        return self.minute * 60.0

    @property
    def millisecond(self):
        """
        Get the angle in milliseconds.
        """
        return self.second * 1000.0

    def __add__(self, that):
        return Angle.from_degree(self.degree + that.degree)

    def __sub__(self, that):
        return Angle.from_degree(self.degree - that.degree)

    def __mul__(self, that):
        return Angle.from_degree(self.degree * that)

    def __div__(self, that):
        return Angle.from_degree(self.degree / that)

    def __truediv__(self, that):
        return Angle.from_degree(self.degree / that)

    def __floordiv__(self, that):
        return Angle.from_degree(self.degree // that)

    def __pos__(self):
        return Angle.from_degree(self.degree)

    def __neg__(self):
        return Angle.from_degree(-self.degree)

    def __abs__(self):
        return Angle.from_degree(abs(self.degree))

    @staticmethod
    def from_degree(degree):
        """
        Create from an angle in degrees.
        """
        return Angle(degree)

    @staticmethod
    def from_minute(minute):
        """
        Create from an angle in minutes.
        """
        return Angle.from_degree(float(minute) / 60.0)

    @staticmethod
    def from_second(second):
        """
        Create from an angle in seconds.
        """
        return Angle.from_minute(float(second) / 60.0)

    @staticmethod
    def from_millisecond(millisecond):
        """
        Create from an angle in milliseconds.
        """
        return Angle.from_second(float(millisecond) / 1000.0)
