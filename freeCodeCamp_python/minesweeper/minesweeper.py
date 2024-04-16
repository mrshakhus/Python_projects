import random
import string
import re

class Minesweeper:
    def __init__(self):
        self.field = self.make_field()

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
        where_to_place = dict()
        count = 0
        while len(where_to_place) <= bomb_amount:
            where_to_place[count] = [(random.randrange(len(self.field))),(random.randrange(len(self.field)))]
            count += 1
    


    def define_square_number(self):
        pass

        




def play(game):
    game.print_field()

    is_valid = False
    valid_chars =  string.digits + ' ,'
    
    while not is_valid:
        user_input = input('Where would you like to dig? Input as row, col: ')
        if not re.search(fr'[^{valid_chars}]', user_input):
            coordinates = user_input.split(',')
            if len(coordinates) == 2 and int(coordinates[0]) < 10 and int(coordinates[1]) < 10:
                is_valid = True
        else:
            print('Invalid input. Please, try again')

        
    
    


game = Minesweeper()
game.print_field()
play(game)