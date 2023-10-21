from quickga import Organism
from quickga.traits import IntegerTrait

from time import sleep

class TestOrganism(Organism):

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self.value = IntegerTrait(min_value, max_value)

    def fitness_function(self):
        sleep(1)
        return 0

o1 = TestOrganism(0, 5)
o2 = TestOrganism(0, 5)
# print(f"o1: {o1.__dict__} - o2: {o2.__dict__} - o1+o2: {(o1 + o2).__dict__}")
print(o1.fitness)
print(o1.fitness)
print((o1+o2).fitness)



# TestOrganism.evolve()

# t = IntegerTrait(min_value=0, max_value=10)

# print(t.sample())
# print(t.mutate(5))
# print(t.crossover(2, 4))