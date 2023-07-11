"""Main module to run the program."""


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    if solve(board):
        return board
    else:
        raise ValueError("Sudoku impossible to solve")


def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    if len(board) != 9:
        return False

    for row in board:
        if len(row) != 9:
            return False

    for row in board:
        if not is_valid_row(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [
                board[row][col]
                for row in range(i, i + 3)
                for col in range(j, j + 3)
            ]
            if not is_valid_row(subgrid):
                return False

    return True


def is_valid_row(row: list[int]) -> bool:
    """Checks if a row is valid"""
    non_zero_values = [value for value in row if value != 0]
    return len(non_zero_values) == len(set(non_zero_values))


def solve(board: list[list[int]]) -> bool:
    """Helper function to solve the Sudoku board using backtracking"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


def is_valid_move(board: list[list[int]], row: int, col: int, num: int) -> bool:
    """Checks if a number can be placed in a cell without violating Sudoku rules"""
    if num in board[row]:
        return False

    if num in [board[r][col] for r in range(9)]:
        return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    subgrid = [
        board[r][c]
        for r in range(start_row, start_row + 3)
        for c in range(start_col, start_col + 3)
    ]
    if num in subgrid:
        return False

    return True
