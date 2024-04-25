import random
import re

class Minesweeper:
    def __init__(self, dim_size, bomb_num):
        self.dim_size = dim_size
        self.bomb_num = bomb_num

        #need this later to visualise board and for logic
        self.dug = set()

        self.board = self.make_new_board()
        

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        count = 0
        while count < self.bomb_num:
            coord = random.randint(0,self.dim_size ** 2 - 1)
            row = coord // 10
            col = coord % 10

            if self.board[row][col] == '*':
                continue

            self.board[row][col] = '*'

            count += 1

        self.assign_values_to_board

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
                num_bombs += 1

        return num_bombs
    
    def dig(self, r, c):
        
        if (r, c) in self.dug:
            return False

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

    

    #while len(game.dug) != dim_size - bomb_num:


                
                




