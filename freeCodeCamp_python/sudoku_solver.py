import random

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def valid_in_row(self, number, row):
        for check_number in self.board[row]:
            if number == check_number:
                return False
        return True

    def valid_in_col(self, number, col):
        for row in range(9):
            if number == self.board[row][col]:
                return False
        return True

    def valid_in_nonet(self, number, row, col):
        nonet_row_index = row // 3
        nonet_col_index = col // 3
        for i in range(3):
            for j in range(3):
                if number == self.board[3*nonet_row_index + i][3*nonet_col_index + j]:
                    return False
        return True
                    
    
    def valid_number(self, number, row, col):
        #self.valid_in_row(number, row),
        if all([
            self.valid_in_col(number, col),
            self.valid_in_nonet(number, row, col)
        ]):
            return True
        
        return False


    def solve_sudoku(self):

        for row_index, row in enumerate(self.board):
            numbers = set(range(1,10))
            numbers_list = []
            
            #removing existing numbers in board row from set
            for number in row:
                if number != -1:
                    numbers.remove(number)
            
            for col_index, number in enumerate(row):

                is_valid_number = False
                if number != -1:
                    continue

                while not is_valid_number:
                    #if there wasn't a valid number
                    if len(numbers) == 0:
                        return False
                    
                    #choosing random number from list
                    numbers_list = [number for number in numbers]
                    number = random.choice(numbers_list)

                    #if chosen numbers is valid then put it into field, end while loop
                    for number in numbers_list:
                        if self.valid_number(number, row_index, col_index):
                            self.board[row_index][col_index] = number
                            numbers.remove(number)
                            break
                        elif len(numbers) == 1:
                            return False

                    if self.solve_sudoku():
                        is_valid_number = True
                        return True
                    elif not self.solve_sudoku():
                        self.board[row_index][col_index] = -1
                        numbers.add(number)
                    
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
    print(sudoku_solver.solve_sudoku())
    print(example_board)