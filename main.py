from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)

    # p1 = Point(50, 50)
    # p2 = Point(150, 300)
    # p3 = Point(500, 500)
    # p4 = Point(700, 40)
    # l1 = Line(p1, p2)
    # l2 = Line(p1, p4)
    # l3 = Line(p3, p4)
    # l4 = Line(p2, p3)

    # win.draw_line(l1, "red")
    # win.draw_line(l2, "orange")
    # win.draw_line(l3, "green")
    # win.draw_line(l4, "blue")

    c1 = Cell(win)
    c1.draw(100, 100, 200, 200)

    c2 = Cell(win)
    c2.draw(200, 100, 300, 200)
    c2.draw_move(c1, True)

    # c = Cell(win)
    # c.has_left_wall = False
    # c.draw(300, 300, 400, 400,)

    # c = Cell(win)
    # c.has_bottom_wall = False
    # c.draw(500, 450, 600, 550)

    # c = Cell(win)
    # c.has_right_wall = False
    # c.draw(420, 50, 520, 150)

    # c = Cell(win)
    # c.has_top_wall = False
    # c.draw(320, 150, 420, 250)

    win.wait_for_close()


if __name__ == "__main__":
    main()
