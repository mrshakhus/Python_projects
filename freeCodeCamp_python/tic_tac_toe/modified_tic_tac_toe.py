import time
from tic_tac_toe_players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.winner = None
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
        #return ['X', 'O', 'X', 'X', 'O', ' ', ' ', ' ', 'O']

    @staticmethod
    def print_board_nums():
        numerated_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in numerated_board:
            print('| '+' | '.join(row)+' |')

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')
        print('')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.is_winner(square, letter):
                self.winner = letter
            return True
        return False
    
    def is_winner(self, square, letter):
        #horizontal:
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([letter == spot for spot in row]):
            return True
        
        #vertical:
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([letter == spot for spot in col]):
            return True
        
        #diagonal:
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([letter == spot for spot in diagonal1]):
                return True
            if all([letter == spot for spot in diagonal2]):
                return True

        return False
    
    def empty_squares(self):
        return ' ' in self.board
    
    def empty_squares_number(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
    
def play(game, o_player, x_player, print_board = True):
    letter = 'X'

    if print_board:
        game.print_board_nums()
    
    while game.empty_squares():
        if print_board:
            game.print_board_nums()

        if print_board:
            print(f'{letter}\'s turn. ', end='')

        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        
        if game.make_move(square, letter):
            game.board[square] = letter
            if print_board:
                print(f'{letter} makes a move to square {square}')
                game.print_board()

            if game.winner:
                if print_board:
                    print(f'{letter} wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

            if print_board:
                time.sleep(0.5)
    if print_board:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1):
        human = SmartComputerPlayer('X')
        computer = RandomComputerPlayer('O')
        ttt = TicTacToe()
        if play(ttt, computer, human, print_board=False) == 'X':
            x_wins += 1
        elif play(ttt, computer, human, print_board=False) == 'O':
            o_wins += 1
        else: 
            ties += 1

    print(f'{x_wins} X wins, {o_wins} O wins, {ties} ties')