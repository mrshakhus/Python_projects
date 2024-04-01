import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.key = key
            for _ in range(value):
                self.contents.append(key)

    def draw(self, amount_to_draw):
        taken_balls = []
        if amount_to_draw > len(self.contents):
            amount_to_draw = len(self.contents)
        for _ in range(amount_to_draw):
            taken_balls.append(self.contents.pop(random.randrange(len(self.contents))))
        
        return taken_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    suitable_cases = 0
    drawn_balls = hat.draw(num_balls_drawn)
    for _ in range(num_experiments):
        ball_counter = 0
        for_calculation = 0
        for color, ball_amount in expected_balls.items():
            for expected_color in drawn_balls:
                if expected_color == color:
                    ball_counter += 1
                if ball_amount <= ball_counter:
                    for_calculation += 1
                    break
        if len(expected_balls) == for_calculation:
            suitable_cases += 1

    return round(suitable_cases/num_experiments, 3)

hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red":2,"green":1},
    num_balls_drawn=5,
    num_experiments=2000
    )

print(probability)