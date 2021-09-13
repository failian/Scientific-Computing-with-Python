import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs:
            for n in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, n):
        random.shuffle(self.contents)
        draws_list = []
        for _ in range(n):
            try:
                draws_list.append(self.contents.pop())
            except IndexError:
                break
        return draws_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = []
    match = 0

    for key in expected_balls:
        count.append(expected_balls[key])

    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        draw_list = experiment_hat.draw(num_balls_drawn)

        no_of_balls = []
        for key in expected_balls:
            no_of_balls.append(draw_list.count(key))
        if no_of_balls >= count:
            match += 1

    return match/num_experiments
