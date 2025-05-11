from graphics import Point, Line


class Cell:
    def __init__(self, window):
        self._window = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        p0 = Point(self._x1, self._y1)
        p1 = Point(self._x2, self._y1)
        p2 = Point(self._x2, self._y2)
        p3 = Point(self._x1, self._y2)

        if self.has_left_wall:
            left_wall = Line(p0, p3)
            self._window.draw_line(left_wall)

        if self.has_top_wall:
            top_wall = Line(p0, p1)
            self._window.draw_line(top_wall)

        if self.has_right_wall:
            right_wall = Line(p1, p2)
            self._window.draw_line(right_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(p2, p3)
            self._window.draw_line(bottom_wall)
