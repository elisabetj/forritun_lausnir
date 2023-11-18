class Shape:
    def __init__(self):
        pass

    def __str__(self):
        return f"{self.__get_name()} with area of {self.get_area():.2f} and perimeter of {self.get_perimeter():.2f}"

    def __get_name(self):
        return type(self).__name__

    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        raise NotImplementedError
