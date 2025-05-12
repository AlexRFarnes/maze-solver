from graphics import Point, Line


class Cell:
    def __init__(self, win):
        self._win = win
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        p0 = Point(self._x1, self._y1)
        p1 = Point(self._x2, self._y1)
        p2 = Point(self._x2, self._y2)
        p3 = Point(self._x1, self._y2)

        if self.has_top_wall:
            top_wall = Line(p0, p1)
            self._win.draw_line(top_wall)

        if self.has_right_wall:
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(p2, p3)
            self._win.draw_line(bottom_wall)

        if self.has_left_wall:
            left_wall = Line(p3, p0)
            self._win.draw_line(left_wall)

    def get_center(self, x1, y1, x2, y2):
        center_x = abs(x2 - x1) // 2 + x1
        center_y = abs(y2 - y1) // 2 + y1
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        from_center = self.get_center(self._x1, self._y1, self._x2, self._y2)
        to_center = to_cell.get_center(
            to_cell._x1, to_cell._y1, to_cell._x2, to_cell._y2)

        fill_color = "gray" if undo else "red"

        line = Line(from_center, to_center)

        self._win.draw_line(line, fill_color)
