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
            
    def __chose_square_number_for_computer(self):
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
        is_win = [False for _ in range(3)]
        for index in range(3):
            #vertical:
            if self._filling_list[(square_number + 3*index)%9] == self._whos_turn:
                is_win[index] = True
                if index == 2 and all(is_win):
                    return True

        is_win = [False for _ in range(3)]
        for index in range(3):
            #horizontal:
            if square_number < 3:
                divider = 3
            elif square_number < 6:
                divider = 6
            else: 
                divider = 9
        
            if self._filling_list[(square_number + index + 1)%divider] == self._whos_turn:
                is_win[index] = True
                if index == 2 and all(is_win):
                    return True

        is_win = [False for _ in range(3)]
        for index in range(3):  
            #diagonal:
            if self._filling_list[4*index] == self._whos_turn:
                is_win[index] = True
                if index == 2 and all(is_win):
                    return True

        is_win = [False for _ in range(3)]
        for index in range(3): 
            if self._filling_list[2+2*index] == self._whos_turn:
                is_win[index] = True
                if index == 2 and all(is_win):
                    return True
                
        return False

    def __get_valid_square_number(self):
        user_input = int(input(f"{self._whos_turn}'s turn. Input move (0-8): "))
        while user_input not in self._square_numbers:
            user_input = int(input("Input move (0-8): "))

        self._square_numbers.remove(user_input)
        return user_input
        
    
    def __allow_human_to_make_move(self):
        
        self.__define_whos_turn()
        square_number = self.__get_valid_square_number() 

        print(f"{self._whos_turn} makes a move to square {square_number}")
        for index in self._square_numbers:
            self._filling_list[index] = ' '
        self._filling_list[square_number] = self._whos_turn

        self.__refill_grid(self._filling_list)
        print(''.join(self._grid))

        if self.__check_if_someone_won(square_number):
            print(f'"{self._whos_turn}" won')
            self._is_gaming = False


    def __make_move_for_computer(self):

        self.__define_whos_turn()
        square_number = self.__chose_square_number_for_computer()

        print(f"{self._whos_turn} makes a move to square {square_number}")
        for index in self._square_numbers:
            self._filling_list[index] = ' '
        self._filling_list[square_number] = self._whos_turn

        self.__refill_grid(self._filling_list)
        print(''.join(self._grid))

        if self.__check_if_someone_won(square_number):
            print(f'"{self._whos_turn}" won')
            self._is_gaming = False

    


    def __launch_human_vs_computer(self):
        while self._is_gaming:
            if not self._square_numbers:
                self._is_gaming = False
                print('Tie')
            self.__allow_human_to_make_move()
            if self._is_gaming:
                self.__make_move_for_computer()

    def __launch_human_vs_human(self):
        while self._is_gaming:
            self.__allow_human_to_make_move()
            if not self._square_numbers:
                self._is_gaming = False
                print('Tie')

    def __launch_computer_vs_computer(self): 
        while self._is_gaming:
            self.__make_move_for_computer()
            if not self._square_numbers:
                self._is_gaming = False
                print('Tie')
        
players = Player('human vs computer')
tic_tac_toe = Game(players)
tic_tac_toe.start_game()