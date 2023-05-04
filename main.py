def outOfColumns(row, column):
    # if reached the last column, go to the next row, else go to the next column
    if (column == 8):
        row += 1
        column = 0
    else:
        column += 1
    return row, column


def alreadyPresent(sudokuBoard, row, column, num):
    # check if the number is already present in the same row
    for i in range(0, 9):
        if (sudokuBoard[row][i] == num):
            return True

    # check if the number is already present in the same column
    for i in range(0, 9):
        if (sudokuBoard[i][column] == num):
            return True

    # check if the number is already present in that 3x3 box
    # first get the starting row and column of that box
    newRow = row - (row % 3)
    newColumn = column - (column % 3)
    for i in range(3):
        for j in range(3):
            if (sudokuBoard[i + newRow][j + newColumn] == num):
                return True

    return False


def sudokuSolver(sudokuBoard, row, column):
    if row == 9:  # if at the end of the board, no more backtracking
        return True

    rowUpdated, columnUpdated = outOfColumns(row, column)

    # if a number is already in place, go to the next
    if (sudokuBoard[row][column] > 0):
        return sudokuSolver(sudokuBoard, rowUpdated, columnUpdated)

    for i in range(1, 10):
        if not (alreadyPresent(sudokuBoard, row, column, i)):
            sudokuBoard[row][column] = i
            if sudokuSolver(sudokuBoard, rowUpdated, columnUpdated):
                return True
        sudokuBoard[row][column] = 0

    return False


def printSudoku(sudokuBoard):
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(0, 9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(sudokuBoard[i][j], end=" ")
        print()
    print()


if __name__ == "__main__":
    sudokuBoard = [[0, 0, 0, 3, 1, 0, 6, 0, 0],
                   [6, 0, 0, 2, 0, 0, 1, 0, 0],
                   [0, 8, 0, 0, 5, 0, 2, 0, 0],
                   [0, 5, 4, 0, 0, 0, 0, 0, 0],
                   [9, 7, 0, 0, 0, 0, 0, 8, 3],
                   [0, 0, 0, 0, 0, 0, 7, 4, 0],
                   [0, 0, 3, 0, 2, 0, 0, 6, 0],
                   [0, 0, 8, 0, 0, 4, 0, 0, 7],
                   [0, 0, 2, 0, 3, 7, 0, 0, 0]]

    print("Unsolved Sudoku:\n")
    printSudoku(sudokuBoard)
    sudokuSolver(sudokuBoard, 0, 0)
    print("Solved Sudoku:\n")
    printSudoku(sudokuBoard)
