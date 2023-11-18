from abc import ABC, abstractmethod


class Canvas(ABC):
    @abstractmethod
    def draw_backslash(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_upper_left_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_upper_right_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_lower_left_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_lower_right_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_vertical_line(self, x: int, y: int, length: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_horizontal_line(self, x: int, y: int, length: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_color(self, color_index: int) -> None:
        raise NotImplementedError


class Shape:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int) -> None:
        self.x = pos_x
        self.y = pos_y
        self.width = max(1, width)
        self.height = max(1, height)

    def move(self, delta_x: int = 0, delta_y: int = 0):
        self.x += delta_x
        self.y += delta_y

    def draw(self, canvas: Canvas) -> None:
        pass

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width - 1

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height - 1


class Rectangle(Shape):
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int) -> None:
        super().__init__(pos_x, pos_y, max(width, 2), max(height, 2))

    def draw(self, canvas: Canvas) -> None:
        canvas.draw_upper_left_corner(x=self.left, y=self.top)
        canvas.draw_upper_right_corner(x=self.right, y=self.top)
        canvas.draw_lower_left_corner(x=self.left, y=self.bottom)
        canvas.draw_lower_right_corner(x=self.right, y=self.bottom)
        if self.width > 2:
            canvas.draw_horizontal_line(self.left + 1, self.top, self.width - 2)
            canvas.draw_horizontal_line(self.left + 1, self.bottom, self.width - 2)
        if self.height > 2:
            canvas.draw_vertical_line(self.left, self.top + 1, self.height - 2)
            canvas.draw_vertical_line(self.right, self.top + 1, self.height - 2)


class Square(Rectangle):
    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)


class Triangle(Shape):
    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)

    def draw(self, canvas: Canvas) -> None:
        canvas.draw_lower_left_corner(x=self.left, y=self.bottom)
        if self.width > 1:
            canvas.draw_horizontal_line(self.left + 1, self.bottom, self.width - 1)
        if self.height > 1:
            canvas.draw_vertical_line(self.left, self.top, self.height - 1)
        for i in range(1, self.width - 1):
            x = self.left + i
            y = self.top + i
            canvas.draw_backslash(x, y)


class HorizontalLine(Shape):
    def __init__(self, pos_x: int, pos_y: int, length: int) -> None:
        super().__init__(pos_x, pos_y, width=length, height=1)

    def draw(self, canvas: Canvas) -> None:
        canvas.draw_horizontal_line(x=self.x, y=self.y, length=self.width)


class VerticalLine(Shape):
    def __init__(self, pos_x: int, pos_y: int, length: int) -> None:
        super().__init__(pos_x, pos_y, width=1, height=length)

    def draw(self, canvas: Canvas) -> None:
        canvas.draw_vertical_line(x=self.x, y=self.y, length=self.height)
