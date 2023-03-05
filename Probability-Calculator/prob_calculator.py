import random
import copy
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # expected_balls = [key for key, val in expected_balls.items() for _ in range(val)]
  experimnet_count = 0
  for _ in range(num_experiments):
      another_hat = copy.deepcopy(hat)
      balls_drawn = another_hat.draw(num_balls_drawn)
      check = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
      experimnet_count += 1 if check == len(expected_balls) else 0
  return experimnet_count / num_experiments
  
