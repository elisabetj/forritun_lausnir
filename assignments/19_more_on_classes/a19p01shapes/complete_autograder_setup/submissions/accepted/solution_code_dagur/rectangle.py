class Rectangle:
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f"{type(self).__name__} with area of {self.get_area():.2f} and perimeter of {self.get_perimeter():.2f}"
