from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, sidelength):
        super().__init__(width=sidelength, height=sidelength)
