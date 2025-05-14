import random
import time
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        if seed:
            self.seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(4, 3)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        self._cells[i][j].has_left_wall = False
        self._cells[i][j].has_right_wall = False
        self._cells[i][j].has_top_wall = False
        self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)
        while True:
            cells_to_visit = []
            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    cells_to_visit.append((i - 1, j))
            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    cells_to_visit.append((i, j - 1))
            if i + 1 < self.num_cols:
                if not self._cells[i + 1][j].visited:
                    cells_to_visit.append((i + 1, j))
            if j + 1 < self.num_rows:
                if not self._cells[i][j + 1].visited:
                    cells_to_visit.append((i, j + 1))

            if len(cells_to_visit) == 0:
                self._draw_cell(i, j)
                return
            new_i, new_j = random.choice(cells_to_visit)
            print(new_i, new_j)

            #  TODO
            # Break the walls between the current cell and the chosen cell
            # Move to the chosen cell

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return

        c = self._cells[i][j]

        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        c.draw(x1, y1, x2, y2)

        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows -
                                       1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows -
                        1)

    def _animate(self):
        if self.win is None:
            return

        self.win.redraw()
        time.sleep(0.05)
