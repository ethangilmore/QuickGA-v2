import random

from .trait import Trait

class BinaryTrait(Trait):

    def sample(self):
        return random.choice([True, False])
    
    def mutate(self, value, mutation_rate):
        return not value if random.random() < mutation_rate else value
    
    def crossover(self, a, b):
        return random.choice([a, b])