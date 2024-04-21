import random

class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.counter = 0
        self.recursion_count = 0

    def valid_in_row(self, board, number, row):
        for check_number in board[row]:
            if number == check_number:
                return False
        return True

    def valid_in_col(self, board, number, col):
        for row in range(9):
            if number == board[row][col]:
                return False
        return True

    def valid_in_nonet(self, board, number, row, col):
        nonet_row_index = row // 3
        nonet_col_index = col // 3
        for i in range(3):
            for j in range(3):
                if number == board[3*nonet_row_index + i][3*nonet_col_index + j]:
                    return False
        return True
                    
    
    def valid_number(self, board, number, row, col):
        #self.valid_in_row(number, row),
        if all([
            self.valid_in_col(board, number, col),
            self.valid_in_nonet(board, number, row, col)
        ]):
            return True
        
        return False


    def solve_sudoku(self, board):
        for row_index, row in enumerate(board):
            numbers = set(range(1,10))
            counter = 0
            
            #removing existing numbers in board row from set
            for number in row:
                if number != -1:
                    numbers.remove(number)
            
            #checking whether the algorithm stuck
            for col_index, number in enumerate(row):
                if number == -1:
                    counter += 1

            if counter in [1,2]:
                self.counter += 1

            #skipping squares with numbers
            for col_index, number in enumerate(row):
                is_valid_number = False 
                if number != -1:
                    continue
                
                while not is_valid_number:
                    #if chosen numbers is valid then put it into field, end while loop
                    for number in numbers:
                        if self.valid_number(board, number, row_index, col_index):
                            board[row_index][col_index] = number
                            break
                        elif self.counter >= 2:
                            self.counter = 0
                            return {'board': self.board, 'statement': 0}

                    self.recursion_count += 1
                    dictionary = self.solve_sudoku(board)
                    if dictionary['statement']:
                        is_valid_number = True
                        return {'board': board, 'statement': 1}
                    else:
                        self.recursion_count -= 1
                        if self.recursion_count == 0:
                            return {'board': self.board, 'statement': 1}
                        return {'board': self.board, 'statement': 0}
                        

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

    sudoku_solver = SudokuSolver(example_board)
    print(sudoku_solver.solve_sudoku(example_board))
    print(example_board)