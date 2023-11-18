class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.imaginary_part == 0:
            return f"{self.real_part}"
        elif self.real_part == 0:
            return f"{self.imaginary_part}i"
        else:
            sign = "-" if self.imaginary_part < 0 else "+"
            return f"{self.real_part} {sign} {abs(self.imaginary_part)}i"

    def __repr__(self) -> str:
        """Returns a parsable string representation of the Vector."""
        return f"{self.__class__.__name__}({self.real_part}, {self.imaginary_part})"

    def re(self) -> float:
        return self.real_part

    def im(self) -> float:
        return self.imaginary_part

    def __eq__(self, other: "ComplexNumber") -> bool:
        return self.re() == other.re() and self.im() == other.im()

    def conjugate(self) -> "ComplexNumber":
        return ComplexNumber(self.real_part, -self.imaginary_part)

    def __neg__(self) -> "ComplexNumber":
        return ComplexNumber(-self.real_part, -self.imaginary_part)

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.re() + other.re(), self.im() + other.im())

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return self + (-other)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            self.re() * other.re() - self.im() * other.im(),
            self.re() * other.im() + self.im() * other.re(),
        )

    def inverse(self) -> "ComplexNumber":
        if self.real_part == self.imaginary_part == 0:
            raise ZeroDivisionError

        denominator = (self * self.conjugate()).re()
        return ComplexNumber(self.re() / denominator, -self.im() / denominator)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        return self * other.inverse()
