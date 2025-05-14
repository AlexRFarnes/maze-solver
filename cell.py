from graphics import Point, Line


class Cell:
    def __init__(self, win=None):
        self.win = win
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def get_color_for_wall(self, has_wall):
        return "black" if has_wall else "white"

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        p0 = Point(x1, y1)
        p1 = Point(x2, y1)
        p2 = Point(x2, y2)
        p3 = Point(x1, y2)

        top_wall = Line(p0, p1)
        fill_color = self.get_color_for_wall(self.has_top_wall)
        self.win.draw_line(
            top_wall, fill_color)

        right_wall = Line(p1, p2)
        fill_color = self.get_color_for_wall(self.has_right_wall)
        self.win.draw_line(
            right_wall, fill_color)

        bottom_wall = Line(p2, p3)
        fill_color = self.get_color_for_wall(self.has_bottom_wall)
        self.win.draw_line(
            bottom_wall, fill_color)

        left_wall = Line(p3, p0)
        fill_color = self.get_color_for_wall(self.has_left_wall)
        self.win.draw_line(
            left_wall, fill_color)

    def get_center(self, x1, y1, x2, y2):
        center_x = abs(x2 - x1) // 2 + x1
        center_y = abs(y2 - y1) // 2 + y1
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return

        from_center = self.get_center(self._x1, self._y1, self._x2, self._y2)
        to_center = to_cell.get_center(
            to_cell._x1, to_cell._y1, to_cell._x2, to_cell._y2)

        fill_color = "gray" if undo else "red"

        line = Line(from_center, to_center)

        self.win.draw_line(line, fill_color)
