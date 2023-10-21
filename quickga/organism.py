import random
from functools import cached_property

from .traits import Trait
from .population import Population
from .selectors import RouletteSelector

class Organism:

    def __init__(self, *args, **kwargs):
        self._init_args = args
        self._init_kwargs = kwargs
        self._traits = dict()

    def __setattr__(self, name, value):
        if isinstance(value, Trait):
            if self.__dict__.get('_traits') is None:
                raise AttributeError("Cannot assign traits before Organism.__init__() is called")
            self._traits[name] = value
            super().__setattr__(name, value.sample())
        else:
            super().__setattr__(name, value)
    
    def __add__(self, other):
        if type(other) is not type(self):
            raise TypeError(f"Organisms must be the same type")
        
        child = type(self)(*self._init_args, **self._init_kwargs)
        for name, trait in self._traits.items():
            self_trait = self.__dict__.get(name)
            other_trait = other.__dict__.get(name)
            child.__dict__[name] = trait.crossover(self_trait, other_trait)
        
        return child
    
    @cached_property
    def fitness(self):
        return self.fitness_function()
    
    def fitness_function(self):
        raise NotImplementedError(f"Organism {type(self).__name__} must implement the \"fitness_function\" method")
    
    def mutate(self, mutation_rate):
        for name, trait in self._traits.items():
            original_value = self.__dict__.get(name)
            mutated_value = trait.mutate(original_value, mutation_rate)
            self.__dict__[name] == mutated_value
    
    def evolve(self, population_size, num_generations, crossover_rate=0.8, mutation_rate=0.05, selector=RouletteSelector()):
        population = Population([type(self)(*self._init_args, **self._init_kwargs) for _ in range(population_size)])

        for generation in range(num_generations):
            new_organisms = selector.get_survivors(population)
            while len(new_organisms) < population_size:
                parent = selector.select_parent(population)
                child = parent + selector.select_parent(population) if random.random() < crossover_rate else parent
                child.mutate(mutation_rate)
                new_organisms.append(child)
            population = Population(new_organisms)
        
        return population.most_fit