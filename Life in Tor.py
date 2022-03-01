import copy
import pygame
from Tor import  Board


class Life(Board):
    def __init__(self, width, height, left, top, cell_size):
        super().__init__(width, height, left, top, cell_size)

    def on_click(self, cell):
        if self.board[cell[1]][cell[0]] == 0:
            self.board[cell[1]][cell[0]] = 1
        elif self.board[cell[1]][cell[0]] == 1:
            self.board[cell[1]][cell[0]] = 0

    def render(self, screen):
        for i in range(self.height):
            for k in range(self.width):
                first = i * self.cell_size + self.left
                second = k * self.cell_size + self.top
                if self.board[k][i] == 1:
                    pygame.draw.rect(screen, pygame.Color("green"), (first, second, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, pygame.Color("black"), (first, second, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color("white"), (first, second, self.cell_size, self.cell_size), 1)

    def next_move(self):
        self.board2 = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(len(self.board)):
            for k in range(len(self.board[i])):
                sum = self.raschet_sosed(i, k)
                if sum not in (2, 3) and self.board[i][k] == 1:
                    self.board2[i][k] = 0
                elif sum == 3 and self.board[i][k] == 0:
                    self.board2[i][k] = 1
                else:
                    self.board2[i][k] = self.board[i][k]
        self.board = copy.deepcopy(self.board2)

    def raschet_sosed(self, i, k):
        sum = 0
        for x in range(i - 1, i + 2):
            for y in range(k - 1, k + 2):
                if x < 0:
                    x = len(self.board) - 1
                elif x >= len(self.board):
                    x = 0
                if y < 0:
                    y = len(self.board[x]) - 1
                elif y >= len(self.board[x]):
                    y = 0
                if i == x and k == y:
                    continue
                elif self.board[x][y] == 1:
                    sum += 1
        return sum


if __name__ == '__main__':
    pygame.init()
    width_tiles = height_tiles = 30
    left = top = 10
    cell_size = 15
    board = Life(width_tiles, height_tiles, left, top, cell_size)
    board.set_view(left, top, cell_size)
    width = left + width_tiles * cell_size + left
    height = top + height_tiles * cell_size + top
    size = width, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра «Жизнь»')
    clock = pygame.time.Clock()

    run_life = False
    speed_life = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                run_life = not run_life
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                speed_life += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                speed_life -= 1

        screen.fill(pygame.Color('black'))
        board.render(screen)
        if speed_life < 0:
            speed_life = 0
        elif speed_life > 40:
            speed_life = 40

        if run_life:
            board.next_move()

        pygame.display.flip()
        clock.tick(speed_life)
