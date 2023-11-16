import random

from .trait import Trait

class SequenceTrait(Trait):

    def __init__(self, length, element_trait):
        self.length = length
        self.element_trait = element_trait

    def sample(self):
        return [self.element_trait.sample() for _ in range(self.length)]
    
    def mutate(self, value, mutation_rate):
        return [self.element_trait.mutate(element, mutation_rate) for element in value]
    
    def crossover(self, a, b):
        # one-point crossover https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#One-point_crossover
        
        index = random.randint(0, len(a))
        return a[:index] + b[index:]