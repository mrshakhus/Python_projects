import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, amount_to_draw):
        taken_balls = []
        content_copy = copy.deepcopy(self.contents)
        if amount_to_draw > len(self.contents):
            amount_to_draw = len(self.contents)
        for _ in range(amount_to_draw):
            taken_balls.append(content_copy.pop(random.randrange(len(content_copy))))
        
        return taken_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    suitable_cases = 0

    for _ in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        number_of_matches = 0

        for expected_ball_color, expected_balls_amount in expected_balls.items():
            match_counter = 0

            for ball_color in drawn_balls:

                if ball_color == expected_ball_color:
                    match_counter += 1
                if match_counter == expected_balls_amount:
                    number_of_matches += 1
                    break

        if len(expected_balls) == number_of_matches:
            suitable_cases += 1


    return suitable_cases/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
    expected_balls={"red":2,"green":1},
    num_balls_drawn=5,
    num_experiments=2000)

print(probability)