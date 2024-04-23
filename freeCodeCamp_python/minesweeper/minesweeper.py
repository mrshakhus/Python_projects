import random
import string
import re

class Minesweeper:
    def __init__(self):
        self.field = self.make_field()
        self.coords_of_bombs = dict()
        self.define_bomb_coords()
        self.game_over = False

    @staticmethod
    def make_field():
        return [[' ' for _ in range(10)] for _ in range(10)]
    
    def print_field(self):
        row_numbers = [str(i) for i in range(10)]
        print('   '+'  '.join(row_numbers)+' ')
        print(f'{'-'*34}')
        for col_number, row_print in enumerate(self.field):
            print(str(col_number)+ ' |' + ' |'.join(row_print) + ' |')

        print(f'{'-'*34}\n')
        

    def define_bomb_coords(self):
        pass
        # bomb_amount = 10
        # count = 0
        # while len(self.coords_of_bombs) < bomb_amount:
        #     self.coords_of_bombs[count] = [(random.randrange(len(self.field))),(random.randrange(len(self.field)))]
        #     count += 1
    
    def print_all_bombs(self):
        pass
    #     self.game_over = True
    #     for bomb_coords in self.coords_of_bombs:
    #         bomb_row = self.coords_of_bombs[bomb_coords][0]
    #         bomb_col = self.coords_of_bombs[bomb_coords][1]

    #         self.field[bomb_row][bomb_col] = '*'

    def define_square_number(self, coords, is_first_pick=True):
        bomb_counter = 0
        row = coords[0]
        col = coords[1]

        for bomb_coords in self.coords_of_bombs:

            for i in range(3):
                #skip iteration if checking square outside of field
                row_less_than_0 = row + (i-1) <= 0
                row_more_than_9 = col + (i-1) >= 9
                if row_less_than_0 or row_more_than_9:
                    continue

                for j in range(3):
                    #skip iteration if checking square outside of field
                    col_less_than_0 = row + (j-1) <= 0
                    col_more_than_9 = col + (j-1) >= 9
                    if col_less_than_0 or col_more_than_9:
                        continue
                    
                    #checking whether current square has bomb
                    is_same_row = self.coords_of_bombs[bomb_coords][0] == row + (i-1)
                    is_same_col = self.coords_of_bombs[bomb_coords][1]  == col + (j-1)

                    if is_same_row and is_same_col:
                        bomb_counter += 1

                        #printing all bombs if player chose square with bomb 
                        if j == 0 and i == 0 and is_first_pick:
                            self.print_all_bombs()

        self.field[row][col] = str(bomb_counter)

        #continue when no bombs detected
        if bomb_counter == 0:
            if col <= 8:
                self.define_square_number([row, col + 1], False)
            elif row <= 8:
                self.define_square_number([row + 1, col], False)
                
            

        
def play(game):
    while not game.game_over:
        game.print_field()

        is_valid = False
        valid_chars =  string.digits + ' ,'
        coords = []

        while not is_valid:
            #there's definately a more delicat way to write it
            user_input = input('Where would you like to dig? Input as row, col: ')
            if not re.search(fr'[^{valid_chars}]', user_input):
                try:
                    coords = user_input.split(',')
                    coords[0] = int(coords[0])
                    coords[1] = int(coords[1])

                    if len(coords) == 2 and coords[0] < 10 and coords[1] < 10:
                        is_valid = True
                    else:
                        print('Invalid input. Please, try again')
                except(ValueError):
                    print('Invalid input. Please, try again')
            else:
                print('Invalid input. Please, try again')
        
        game.define_square_number(coords)
        game.print_field()

    if game.game_over:
        print('GAME OVER')

game = Minesweeper()
game.print_field()
play(game)