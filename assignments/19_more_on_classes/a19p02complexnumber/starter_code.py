class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def re(self) -> float:
        raise NotImplementedError

    def im(self) -> float:
        raise NotImplementedError

    def __eq__(self, other: "ComplexNumber") -> bool:
        raise NotImplementedError

    def conjugate(self) -> "ComplexNumber":
        raise NotImplementedError

    def __neg__(self) -> "ComplexNumber":
        raise NotImplementedError

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        raise NotImplementedError

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        raise NotImplementedError

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        raise NotImplementedError

    def inverse(self) -> "ComplexNumber":
        raise NotImplementedError

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        raise NotImplementedError
