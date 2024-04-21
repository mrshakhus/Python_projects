class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def valid_in_row(self, number, row):
        return number not in self.board[row]

    def valid_in_col(self, number, col):
        return all(
            number != self.board[row][col]
            for row in range(9)
        )

    def valid_in_nonet(self, number, row, col):
        nonet_row_index = (row // 3) * 3
        nonet_col_index = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if number == self.board[nonet_row_index + i][nonet_col_index + j]:
                    return False
        return True
                    
    
    def valid_number(self, number, next_empty_cell):
        row, col = next_empty_cell
        return all([
            self.valid_in_row(number, row),
            self.valid_in_col(number, col),
            self.valid_in_nonet(number, row, col)
        ])
    
    def find_empty_cell(self):
        for row, numbers in enumerate(self.board):
            try:
                col = numbers.index(-1)
                empty_cell = [row, col]
                return empty_cell
            except ValueError:
                pass
        return None


    def solve_sudoku(self):
        next_empty_cell = self.find_empty_cell()
        if next_empty_cell is None:
            return True
        else:
            for guess_number in range(1,10):
                if self.valid_number(guess_number, next_empty_cell):
                    row, col = next_empty_cell
                    self.board[row][col] = guess_number
                    if self.solve_sudoku():
                        return True
                    self.board[row][col] = -1
        
        return False
    
def solve_sudoku(board):
    sudoku_solver = SudokuSolver(board)
    if sudoku_solver.solve_sudoku():
        print('Sudoku solved!')

        for row_i, row in enumerate(board):
            for col_i, number in enumerate(row):
                board[row_i][col_i] = str(number)

                if col_i != 0 and (row_i + 1) % 3 == 0 and (col_i + 1) % 9 == 0:
                    board[row_i][col_i] += '\n'

                if (col_i + 1) % 3 == 0:
                    board[row_i][col_i] += '  '

            line = '  '.join(row)
            print(line)

    else:
        print('ERROR: Provided sudoku board is unsolvable')

if __name__ == "__main__":
    example_board = [
        [ 3,  9, -1,   -1,  5, -1,   -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,   -1, -1,  5],
        [-1, -1, -1,    7,  1,  9,   -1,  8, -1],

        [-1,  5, -1,   -1,  6,  8,   -1, -1, -1],
        [ 2, -1,  6,   -1, -1,  3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1,  4],

        [ 5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [ 6,  7, -1,    1, -1,  5,   -1,  4, -1],
        [ 1, -1,  9,   -1, -1, -1,    2, -1, -1]
    ]

    solve_sudoku(example_board)