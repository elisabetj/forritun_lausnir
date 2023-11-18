TOLERANCE = 0.000_000_1


class Vector:
    def __init__(self, what_parameters_do_you_need) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __abs__(self) -> float:
        raise NotImplementedError

    def __add__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __sub__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __eq__(self, other: "Vector") -> bool:
        raise NotImplementedError

    def __mul__(self, scalar: float) -> "Vector":
        raise NotImplementedError

    def __rmul__(self, scalar: float) -> "Vector":
        raise NotImplementedError

    def __repr__(self) -> str:
        """Returns a parsable string representation of the Vector.

        This means that Python will be able to recreate the object
        from the representation
        when repr() is used in conjunction with functions like eval().
        """

        raise NotImplementedError

    def __gt__(self, other: "Vector") -> bool:
        raise NotImplementedError

    def __ge__(self, other: "Vector") -> bool:
        raise NotImplementedError

    def __lt__(self, other: "Vector") -> bool:
        raise NotImplementedError

    def __le__(self, other: "Vector") -> bool:
        raise NotImplementedError

    def dot(self, other: "Vector") -> float:
        raise NotImplementedError

    def cross(self, other: "Vector") -> "Vector":
        raise NotImplementedError
