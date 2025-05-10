from graphics import Window, Line, Point


def main():
    win = Window(800, 600)

    p1 = Point(50, 50)
    p2 = Point(150, 300)
    p3 = Point(500, 500)
    p4 = Point(700, 40)
    l1 = Line(p1, p2)
    l2 = Line(p1, p4)
    l3 = Line(p3, p4)
    l4 = Line(p2, p3)

    win.draw_line(l1, "red")
    win.draw_line(l2, "orange")
    win.draw_line(l3, "green")
    win.draw_line(l4, "blue")

    win.wait_for_close()


if __name__ == "__main__":
    main()
