import random

from .selectionstrategy import SelectionStrategy

class RouletteSelection(SelectionStrategy):
    
    def select(self, population):
        return random.choices(population.organisms, weights=[o.fitness for o in population.organisms])[0]