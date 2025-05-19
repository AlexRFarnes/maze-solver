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
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def __create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                cells_to_visit.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                cells_to_visit.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                cells_to_visit.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                cells_to_visit.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(cells_to_visit) == 0:
                self.__draw_cell(i, j)
                return

            # randomly pick the next direction to go
            new_i, new_j = random.choice(cells_to_visit)

            # knock out walls between this cell and the next cell(s)
            # left
            if new_i < i:
                self._cells[new_i][new_j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            # right
            if new_i > i:
                self._cells[new_i][new_j].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            # up
            if new_j < j:
                self._cells[new_i][new_j].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            # down
            if new_j > j:
                self._cells[new_i][new_j].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False

            # recursively visit the next cells
            self.__break_walls_r(new_i, new_j)

    def __draw_cell(self, i, j):
        if self.win is None:
            return
        c = self._cells[i][j]
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        c.draw(x1, y1, x2, y2)
        self._animate()

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows -
                                       1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows -
                         1)

    def _animate(self):
        if self.win is None:
            return

        self.win.redraw()
        time.sleep(0.05)
