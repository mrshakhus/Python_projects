import random
import string
import re

class Minesweeper:
    def __init__(self):
        self.field = self.make_field()
        self.coordinates_of_bombs = dict()
        self.define_bomb_coordinates()
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
        

    def define_bomb_coordinates(self):
        bomb_amount = 10
        count = 0
        while len(self.coordinates_of_bombs) < bomb_amount:
            self.coordinates_of_bombs[count] = [(random.randrange(len(self.field))),(random.randrange(len(self.field)))]
            count += 1
    
    def print_all_bombs(self):
        self.game_over = True
        for bomb_coordinates in self.coordinates_of_bombs:
            self.field[self.coordinates_of_bombs[bomb_coordinates][0]][self.coordinates_of_bombs[bomb_coordinates][1]]

    def define_square_number(self, coordinates):
        bomb_counter = 0
        for bomb_coordinates in self.coordinates_of_bombs:

            for i in range(3):
                is_same_row = self.coordinates_of_bombs[bomb_coordinates][0] == int(coordinates[0]) + (i-1)

                for j in range(3):
                    is_same_col = self.coordinates_of_bombs[bomb_coordinates][1]  == int(coordinates[1]) + (j-1)

                    if is_same_row and is_same_col:
                        bomb_counter += 1

                        if j == 0 and i == 0:
                            self.print_all_bombs()

        self.field[coordinates[0]][coordinates[1]] = bomb_counter

        if bomb_counter == 0:
            self.define_bomb_coordinates([str(coordinates[0]),str(coordinates[1])])

        
def play(game):
    while not game.game_over:
        game.print_field()

        is_valid = False
        valid_chars =  string.digits + ' ,'
        coordinates = []

        while not is_valid:
            #there's definately a more delicat way to write it
            user_input = input('Where would you like to dig? Input as row, col: ')
            if not re.search(fr'[^{valid_chars}]', user_input):
                try:
                    coordinates = user_input.split(',')
                    if len(coordinates) == 2 and int(coordinates[0]) < 10 and int(coordinates[1]) < 10:
                        is_valid = True
                    else:
                        print('Invalid input. Please, try again')
                except(ValueError):
                    print('Invalid input. Please, try again')
            else:
                print('Invalid input. Please, try again')
        
        game.define_square_number(coordinates)
        game.print_field()

    if game.game_over:
        print('GAME OVER')

game = Minesweeper()
game.print_field()
play(game)