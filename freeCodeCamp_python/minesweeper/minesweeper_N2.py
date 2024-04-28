import random
import re

class Minesweeper:
    def __init__(self, dim_size, bomb_num):
        self.dim_size = dim_size
        self.bomb_num = bomb_num

        #need this later to visualise board and for logic
        self.dug = set()

        self.board = self.make_new_board()
        self.assign_values_to_board()

    def __str__(self):
        visible_board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])

        col_numbers = [str(i) for i in range(self.dim_size)]
        board_for_print = '   '+'  '.join(col_numbers)+' \n'
        board_for_print += f'{'-'*(3*self.dim_size + 5)}\n'
        for row_number, row_print in enumerate(visible_board):
            board_for_print += str(row_number)+ ' |' + ' |'.join(row_print) + ' |\n'

        board_for_print += f'{'-'*(3*self.dim_size + 5)}\n'

        return board_for_print
        

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        count = 0
        while count < self.bomb_num:
            coord = random.randint(0,self.dim_size ** 2 - 1)
            row = coord // 10
            col = coord % 10

            if board[row][col] == '*':
                continue

            board[row][col] = '*'

            count += 1

        return board
    
    def assign_values_to_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue
                
                self.board[row][col] = self.get_num_neighbouring_bombs(row, col)

    def get_num_neighbouring_bombs(self, r, c):

        num_bombs = 0
        #checkin whether the coords are within board
        for row in range(max(0, r-1), min((r+1)+1, self.dim_size)):
            for col in range(max(0, c-1), min((c+1)+1, self.dim_size)):
                if row == r and col == c:
                    continue
                if self.board[row][col] == '*':
                    num_bombs += 1

        return num_bombs
    
    def dig(self, r, c):
        
        if (r, c) in self.dug:
            return False

        self.dug.add((r,c))

        if self.board[r][c] == '*':
            return False
        
        if self.board[r][c] > 0:
            return True
        
        #if there are no bombs then continue to dig recursively
        #until there is a square with bomb nearby
        for row in range(max(0, r-1), min((r+1)+1, self.dim_size)):
            for col in range(max(0, c-1), min((c+1)+1, self.dim_size)):
                if row == r and col == c:
                    continue

                self.dig(row, col)

        #So that program doesn't detonate bomb
        return True
    

def play(dim_size=10, bomb_num=10):
    game = Minesweeper(dim_size, bomb_num)
    print(game)

    while len(game.dug) < dim_size ** 2 - bomb_num:
        coord = re.split(',[\\s]*', input('Where would you like to dig? Input as a row, col: '))
        row, col = int(coord[0]), int(coord[-1])

        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print('Invalid numbers. Please, try again')
            continue

        safe = game.dig(row, col)

        if not safe and game.board[row][col] != '*':
            print('You already digged here. Try another spot')
            continue

        if not safe and game.board[row][col] == '*':
            game.dug = [(r,c) for r in range(dim_size) for c in range(dim_size)]
            print(game) 
            break
        
        print(game)

    if safe:
        print('Congratulations! You found all bombs!')
    else:
        print('GAME OVER')

if __name__ == '__main__':
    play()





    


                
                




