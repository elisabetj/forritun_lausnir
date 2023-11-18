from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)
