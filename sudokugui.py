import pygame
pygame.init()

font = pygame.font.SysFont('timesnewroman', 30)
windowSize = (500, 500)


class SudokuCube:
    def __init__(self, column, row, width, height, number):
        self.cube = pygame.Rect(column, row, width, height)  # column, row
        self.number = number

    def displayCube(self, sudokuWindow):
        color = "white"
        pygame.draw.rect(sudokuWindow, (0, 0, 0), self.cube, 1)
        if self.number != 0:
            numberDisplayed = font.render(
                str(self.number), True, (0, 0, 0))
            centreXCube, centreYCube = self.cube.center
            # print(centreXCube, centreYCube)
            sudokuWindow.blit(
                numberDisplayed, (centreXCube - 10, centreYCube - 10))


class SudokuBoard:
    def __init__(self, row, column, width, height, sudokuBoard):
        self.allCubes = []
        for i in range(9):
            for j in range(9):
                cubeWidth = width / 9
                cubeHeight = height / 9
                number = sudokuBoard[i][j]
                singleCube = SudokuCube(
                    column+j * cubeWidth, row + i * cubeHeight, cubeWidth, cubeHeight, number)
                self.allCubes.append(singleCube)

    def displayBoard(self, sudokuWindow):
        for singleCube in self.allCubes:
            singleCube.displayCube(sudokuWindow)


class SudokuGame:
    def __init__(self):
        self.sudokuBoard = [[0, 0, 0, 3, 1, 0, 6, 0, 0],
                            [6, 0, 0, 2, 0, 0, 1, 0, 0],
                            [0, 8, 0, 0, 5, 0, 2, 0, 0],
                            [0, 5, 4, 0, 0, 0, 0, 0, 0],
                            [9, 7, 0, 0, 0, 0, 0, 8, 3],
                            [0, 0, 0, 0, 0, 0, 7, 4, 0],
                            [0, 0, 3, 0, 2, 0, 0, 6, 0],
                            [0, 0, 8, 0, 0, 4, 0, 0, 7],
                            [0, 0, 2, 0, 3, 7, 0, 0, 0]]
        self.window = None

    def displayWindow(self):
        sudokuScreen = pygame.display.set_mode(windowSize)
        pygame.display.set_caption("Sudoku Solver")
        self.window = SudokuBoard(25, 25, 400, 400, self.sudokuBoard)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            sudokuScreen.fill((255, 255, 255))
            self.window.displayBoard(sudokuScreen)
            pygame.display.flip()


def main():
    game = SudokuGame()
    game.displayWindow()


if __name__ == '__main__':
    main()
