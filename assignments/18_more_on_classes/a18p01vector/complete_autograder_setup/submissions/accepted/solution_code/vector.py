TOLERANCE = 0.000_000_1


class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        """Initializes the three coordinates of the Vector."""
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        """Returns a readable custom string representation of the Vector."""
        return f"[[ {self.x} {self.y} {self.z} ]]"

    def __repr__(self) -> str:
        """Returns a parsable string representation of the Vector.

        This means that Python will be able to recreate the object
        from the representation
        when repr() is used in conjunction with functions like eval().
        """

        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def __add__(self, other: "Vector") -> "Vector":
        """Returns a new Vector that is the sum of self and other."""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector") -> "Vector":
        """Returns a new Vector that is the difference of self and other."""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vector":
        """Returns the result of scaling the original by the scalar."""
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        """Returns the result of scaling the original by the scalar."""
        return self * scalar

    def dot(self, other: "Vector") -> float:
        """Returns the dot product of the two Vectors."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector") -> "Vector":
        """Returns the cross product of the two Vectors."""
        return Vector(
            x=(self.y * other.z - self.z * other.y),
            y=(self.z * other.x - self.x * other.z),
            z=(self.x * other.y - self.y * other.x),
        )

    def __abs__(self) -> float:
        """Returns the length of the Vector."""
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __eq__(self, other: "Vector") -> bool:
        """Checks if the two Vectors are equal, or near enough."""
        return abs(self - other) < TOLERANCE

    def __gt__(self, other: "Vector") -> bool:
        """Checks if the Vector is longer than the other Vector."""
        return abs(self) > abs(other)

    def __ge__(self, other: "Vector") -> bool:
        """Checks if the Vector has greater or equal length than the other Vector."""
        return abs(self) >= abs(other)

    def __lt__(self, other: "Vector") -> bool:
        """Checks if the Vector is shorter than the other Vector."""
        return abs(self) < abs(other)

    def __le__(self, other: "Vector") -> bool:
        """Checks if the Vector has smaller or equal length than the other Vector."""
        return abs(self) <= abs(other)


def main():
    v = Vector(12, 3, 4)
    u = Vector(12, 4, 3)

    O = Vector()
    s = sum([u, v], start=O)

    print(u == v)


if __name__ == "__main__":
    main()
