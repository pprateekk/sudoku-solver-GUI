import pygame
from main import sudokuSolver
pygame.init()

font = pygame.font.SysFont('Courier New', 20)
windowSize = (500, 570)


class SudokuCube:
    # xAxis and yAxis: top-left coordinates of the cube;
    # width and height: of that single cube;
    def __init__(self, xAxis, yAxis, width, height, number):
        self.xCoord = xAxis
        self.yCoord = yAxis
        self.cubeWidth = width
        self.cubeHeight = height
        self.number = number

    def displayCube(self, sudokuWindow):
        if self.number != 0:
            numberDisplayed = font.render(str(self.number), True, (0, 0, 0))
            # get the centre coordinates of the cube;
            # then, subtract it w/ the coordinates of the text - to align the text to the centre of the cube
            centreXCube = self.xCoord + self.cubeWidth/2
            centreYCube = self.yCoord + self.cubeHeight/2
            centreXCube -= numberDisplayed.get_width()/2
            centreYCube -= numberDisplayed.get_height()/2
            sudokuWindow.blit(
                numberDisplayed, (centreXCube, centreYCube))


class SudokuBoard:
    # xAxis and yAxis: top-left coordinates of the board;
    # width and height: of the sudoku board;
    def __init__(self, xAxis, yAxis, width, height, sudokuBoard):
        self.allCubes = []
        self.xCoords = xAxis
        self.yCoords = yAxis
        self.boardWidth = width
        self.boardHeight = height
        self.cubeWidth = width / 9
        self.cubeHeight = height / 9
        for i in range(9):
            for j in range(9):
                number = sudokuBoard[i][j]
                # get the top-left coordinates of that specific cube and pass it the cube class
                topXCoord = self.xCoords + j * self.cubeWidth
                topYCoord = self.yCoords + i * self.cubeHeight
                singleCube = SudokuCube(
                    topXCoord, topYCoord, self.cubeWidth, self.cubeHeight, number)
                self.allCubes.append(singleCube)

    def displayBoard(self, sudokuWindow):
        # draw the grid lines to separate the 9 blocks
        for i in range(10):
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            # draw the row lines
            pygame.draw.line(sudokuWindow, (0, 0, 0),
                             (self.xCoords, self.yCoords + i * self.cubeWidth), (self.xCoords + self.boardWidth, self.yCoords + i * self.cubeWidth), thickness)
            # draw the column lines
            pygame.draw.line(sudokuWindow, (0, 0, 0),
                             (self.xCoords + i * self.cubeWidth, self.yCoords), (self.xCoords + i * self.cubeWidth, self.yCoords + self.boardHeight), thickness)

        # fill in the numbers
        for singleCube in self.allCubes:
            singleCube.displayCube(sudokuWindow)


class SolveButton:
    def __init__(self, xAxis, yAxis, width, height):
        self.xCoord = xAxis
        self.yCoord = yAxis
        self.button = pygame.Rect(self.xCoord, self.yCoord, width, height)

    def displayButton(self, sudokuWindow):
        pygame.draw.rect(sudokuWindow, (0, 0, 0), self.button, 2)
        solveText = font.render('SOLVE', True, (0, 0, 0))
        textCoord = solveText.get_rect(center=self.button.center)
        sudokuWindow.blit(solveText, textCoord)

    def buttonClicked(self, position):
        return self.button.collidepoint(position)


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
        self.xCoords = 50
        self.yCoords = 50
        self.buttonWidth = 90
        self.buttonHeight = 40
        self.boardWidth = 400
        self.boardHeight = 400

    def run(self):
        sudokuScreen = pygame.display.set_mode(windowSize, pygame.RESIZABLE)
        pygame.display.set_caption("Sudoku Solver")
        sudokuScreenBoard = SudokuBoard(self.xCoords, self.yCoords,
                                        self.boardWidth, self.boardHeight, self.sudokuBoard)
        solveButton = SolveButton(
            (windowSize[0]/2) - (self.buttonWidth/2), (self.yCoords*2) + self.boardHeight, self.buttonWidth, self.buttonHeight)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if solveButton.buttonClicked(position):
                        sudokuSolver(self.sudokuBoard, 0, 0)
                        updatedSudoku = self.sudokuBoard
                        sudokuScreenBoard = SudokuBoard(self.xCoords, self.yCoords,
                                                        self.boardWidth, self.boardHeight, self.sudokuBoard)
                        sudokuScreenBoard.displayBoard(sudokuScreen)
                        pygame.display.flip()

            sudokuScreen.fill((203, 203, 203))
            sudokuScreenBoard.displayBoard(sudokuScreen)
            solveButton.displayButton(sudokuScreen)
            pygame.display.flip()


if __name__ == '__main__':
    game = SudokuGame()
    game.run()
