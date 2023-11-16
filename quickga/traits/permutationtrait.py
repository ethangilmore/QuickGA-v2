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
        # partially mapped crossover https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#Partially_mapped_crossover_(PMX)
        
        # select two random indices
        start_index, end_index = random.sample(range(len(a)), 2)
        if start_index > end_index:
            start_index, end_index = end_index, start_index

        # copy down segment from first parent
        child = [None] * len(a)
        child[start_index:end_index] = a[start_index:end_index]

        # map values from second parent
        for i, value in enumerate(b[start_index:end_index]):
            if value in child[start_index:end_index]:
                continue
            mapped_index = self.map_index(i+start_index, b, a, start_index, end_index)
            child[mapped_index] = value

        # copy all other values from second parent
        for i, value in enumerate(child):
            if value is None:
                child[i] = b[i]

        return child

    def map_index(self, index: int, a: list, b: list, region_start: int, region_end: int) -> int:
        map_index = lambda index : a.index(b[index])
        i = index
        while region_start <= i and i < region_end:
            i = map_index(i)
        return i
