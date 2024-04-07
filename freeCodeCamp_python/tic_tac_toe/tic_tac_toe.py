# Either human or computer can play: human vs computer, human vs human, computer vs computer
# Should separate player and game into 2 separate classes

import random

class Player:
    #Defines who's playing agains whom
    def __init__(self, players):
        self.players = f'{players.lower()}'
    
class Game:
    #The game itself, game logic is located here
    #Uses Player class to identify opponents
    def __init__(self, players):
        self._opponents = players.players

        self._filling_list = [index for index in range(9)]
        self._square_numbers = list(range(9))
        self._whos_turn = random.choice(['X','O'])
        self._is_gaming = True
        self._grid = list(range(9))

    def start_game(self):
        self.__refill_grid(self._filling_list)
        print(''.join(self._grid))

        match self._opponents:
            case 'human vs computer':
                self.__launch_human_vs_computer()
            case 'human vs human':
                self.__launch_human_vs_human()
            case 'computer vs computer':
                self.__launch_computer_vs_computer() 


    def __define_whos_turn(self):
        self._whos_turn = 'X' if self._whos_turn == 'O' else 'O'
            
    def __chose_square_number(self):
        square = random.choice(self._square_numbers)
        self._square_numbers.remove(square)
        return square

    def __refill_grid(self, filling_list):
        for index, item in enumerate(filling_list): 
            if (index+1) % 3 != 0:
                self._grid[index] = f'| {item} '
            else:
                self._grid[index] = f'| {item} |\n'

    def __check_if_someone_won(self, square_number):
        is_win = True
        
        for index in range(2):
            #vertical:
            incremented_index = index + 1
            if self._filling_list[(square_number + 3*incremented_index)%9] != self._whos_turn:
                is_win = False

            #horizontal:
            if square_number < 3:
                divider = 3
            elif square_number < 6:
                divider = 6
            else: 
                divider = 9

            if self._filling_list[(square_number + incremented_index)%divider] != self._whos_turn:
                is_win = False
            
            #diagonal:

        
        return is_win


    def __make_move_for_computer(self):

        self.__define_whos_turn()
        square_number = self.__chose_square_number()

        print(f"{self._whos_turn} makes a move to square {square_number}")
        for index in self._square_numbers:
            self._filling_list[index] = ' '
        self._filling_list[square_number] = self._whos_turn

        self.__refill_grid(self._filling_list)
        print(''.join(self._grid))



    def __launch_human_vs_computer(self):
        pass

    def __launch_human_vs_human(self):
        pass

    def __launch_computer_vs_computer(self): 
        while self._is_gaming:
            self.__make_move_for_computer()
            if not self._square_numbers:
                self._is_gaming = False
        
            

players = Player('computer vs computer')
tic_tac_toe = Game(players)
tic_tac_toe.start_game()



    

    