#!/usr/bin/python3


class Height:
    CM_PER_INCH = 2.54
    INCHES_PER_FEET = 12

    def __init__(self, feet, inches):
        """Initialize the instance."""
        self._feet = feet
        self._inches = inches
        self._standardize()

    def _standardize(self):
        """Make sure that the inches in the instance are 11 at the maximum."""
        self._feet += self._inches // self.INCHES_PER_FEET
        self._inches %= self.INCHES_PER_FEET

    def __str__(self):
        """Return a string representation of the instance."""
        return f"{self._feet} ft, {self._inches} in"

    def __add__(self, other: "Height") -> "Height":
        """Return a new instance which is the sum of self and other."""
        feet = self._feet + other._feet
        inches = self._inches + other._inches
        return Height(feet, inches)

    def __gt__(self, other: "Height") -> bool:
        """Return True if self > other, otherwise False."""
        return self.get_total_inches() > other.get_total_inches()

    def cm(self) -> int:
        """Return the height in centimeters, rounded to the nearest integer."""
        return round(Height.CM_PER_INCH * self.get_total_inches())

    def get_total_inches(self) -> float:
        """Get the total height in inches."""
        return self._feet * Height.INCHES_PER_FEET + self._inches
