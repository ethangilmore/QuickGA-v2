import random

from .trait import Trait

class PermutationTrait(Trait):
    
    def __init__(self, elements):
        self.elements = elements

    def sample(self):
        # return a shuffled copy of the elements
        return random.sample(self.elements, len(self.elements))
    
    def mutate(self, value, mutation_rate):
        mutated_value = value.copy()
        for i in range(len(mutated_value)):
            if random.random() < mutation_rate:
                j = random.randint(0, len(mutated_value)-1)
                mutated_value[i], mutated_value[j] = mutated_value[j], mutated_value[i]
        return mutated_value

    def crossover(self, a, b):
        # Ordered Crossover
        size = len(a)
        p1, p2 = sorted(random.sample(range(size), 2))

        # Copy the segment from first parent to offspring
        offspring = [None] * size
        offspring[p1:p2] = a[p1:p2]

        # Fill the remaining positions from the second parent
        b_filtered = [item for item in b if item not in offspring[p1:p2]]
        offspring[:p1] = b_filtered[:p1]
        offspring[p2:] = b_filtered[p1:]

        return offspring