#!/usr/bin/python3


class Height:
    CENTIMETERS_IN_FOOT = 30.48
    CENTIMETERS_IN_INCH = 2.54
    INCHES_IN_FEET = 12

    def __init__(self, feet, inches):
        """Initializes the instance."""
        self.__feet = feet
        self.__inches = inches

        self.fix()

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"{self.__feet} ft, {self.__inches} in"

    def __add__(self, other):
        """Returns a new instance which is the result of adding
        self to other."""
        feet = self.__feet + other.__feet
        inches = self.__inches + other.__inches
        return Height(feet, inches)

    def __gt__(self, other):
        """Returns True if self > other, otherwise False."""
        if self.__feet > other.__feet:
            return True
        elif self.__feet < other.__feet:
            return False
        else:
            return self.__inches > other.__inches

    def fix(self):
        """Makes sure that the inches in the instance are 11 at the maximum."""
        if self.__inches >= self.INCHES_IN_FEET:
            self.__feet += self.__inches // self.INCHES_IN_FEET
            self.__inches = self.__inches % self.INCHES_IN_FEET

    def cm(self):
        """Returns the given height in centimeters,
        rounded to the nearest integer."""
        cm_float = (
            self.__feet * self.CENTIMETERS_IN_FOOT
            + self.__inches * self.CENTIMETERS_IN_INCH
        )
        return round(cm_float)
