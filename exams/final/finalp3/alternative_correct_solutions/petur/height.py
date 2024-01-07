#!/usr/bin/python3


class Height:
    CM_PER_INCH = 2.54
    INCHES_PER_FEET = 12

    def __init__(self, feet: int, inches: int) -> None:
        self._inches = inches + Height.INCHES_PER_FEET * feet

    def __str__(self) -> str:
        feet, inches = divmod(self._inches, Height.INCHES_PER_FEET)
        return f"{feet} ft, {inches} in"

    def cm(self) -> int:
        """Convert the height to centimeters."""
        return round(self._inches * Height.CM_PER_INCH)

    def __gt__(self, other: "Height") -> bool:
        return self._inches > other._inches

    def __add__(self, other: "Height") -> "Height":
        return Height(0, self._inches + other._inches)
