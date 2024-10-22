import random

from .trait import Trait

class IntegerTrait(Trait):
    
    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def sample(self):
        return random.randint(self.min, self.max)
    
    def mutate(self, value, mutation_rate):
        return value if random.random() > mutation_rate else self.sample()
    
    def crossover(self, a, b):
        return random.choice([a, b])