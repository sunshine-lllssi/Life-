import pygame


class  Board:
    def __init__(self, width, height, left, top, cell_size):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size

        self.board = [[0] * width for _ in range(height)]
        self.set_view(left, top, cell_size)

    def render(self, screen):
        pass

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_coords):
        x = (mouse_coords[0] - self.left) // self.cell_size
        y = (mouse_coords[1] - self.top) // self.cell_size
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return (x, y)

    def get_click(self, mouse_coords):
        cell = self.get_cell(mouse_coords)
        if cell:
            self.on_click(cell)
