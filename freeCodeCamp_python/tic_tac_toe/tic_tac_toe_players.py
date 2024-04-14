import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            value = input('Input move (0-8): ')
            try:
                value = int(value)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid squre number. Please, try again')
        return value


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if game.empty_squares() == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        
        return square
    
    def minimax(self, state, player): # state - a 'screenshot' of board
        max_player = self.letter #it's you (SmartComputerPlayer) 
        other_player = 'O' if player == 'X' else 'X'

        #conditions of win and tie
        if state.winner:
            return {'position': None, 'score': 1 * (state.empty_squares_number() + 1) if other_player == max_player else -1 * (state.empty_squares_number() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #maximizing max_players's score
        else:
            best = {'position': None, 'score': math.inf} #minimizin the other player's score

        for available_move in state.available_moves():
            state.make_move(available_move, player) #making move
            sim_score = self.minimax(state, other_player) 
            #making move (simulating) after previous one with another player
            #here with recursion it goes on util there is whether a tie or a win
            #then it returns values back in order of stack

            #reverting moves after simulation
            sim_score['position'] = available_move
            state.winner = None
            state.board[available_move] = ' '

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # maximizing the score of max_plater
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # but minimizing score of other player

        return best