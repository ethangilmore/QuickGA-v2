import random

from .selectionstrategy import SelectionStrategy

class RouletteSelector(SelectionStrategy):
    
    def select(self, population, amount):
        return random.choices(population.organisms, weights=[o.fitness for o in population.organisms], k=amount)