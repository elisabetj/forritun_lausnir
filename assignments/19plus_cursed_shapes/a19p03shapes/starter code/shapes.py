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


# Add your shape classes below
