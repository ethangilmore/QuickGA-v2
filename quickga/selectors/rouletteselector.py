import random

from .selector import Selector

class RouletteSelector(Selector):
    
    def get_survivors(self, population):
        return []
    
    def select_parent(self, population):
        return random.choices(population.organisms, weights=[o.fitness for o in population.organisms])[0]