"""
Angle package.
"""

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
