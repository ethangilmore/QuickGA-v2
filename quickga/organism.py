import random
from functools import cached_property

from .traits import Trait
from .population import Population
from .selectionstrategies import RouletteSelector
from .callbacks import HistoryCallback

class Organism:
    """An object with traits that can be evolved based on a given fitness function.

    Attributes:
        fitness (float):
            The fitness of the organism (defined by implementing fitness_function()). Higher fitness means the organism performs better.
    """

    def __init__(self, *args, **kwargs):
        """Initializes an organism.

        Initializes the trait dictionary and stores the arguments and keyword arguments to be passed into children organisms' constructors.
        
        Args:
            *args: 
                Arguments to be passed to children organisms' constructors.
            **kwargs:
                Keyword arguments to be passed to children organisms' constructors.
        """
        self._init_args = args
        self._init_kwargs = kwargs
        self._traits = dict()

    def __setattr__(self, name, value):
        """Sets attributes and handles trait initialization
        
        Sets attributes normally, but if the value is a Trait, it is added to the trait dictionary and the trait is sampled for a value to set the attribute.

        Args:
            name (str):
                Name of the attribute.
            value:
                Value of the attribute.

        Raises:
            AttributeError:
                If the value is a Trait and Organism.__init__() has not been called yet.
        """
        if isinstance(value, Trait):
            if self.__dict__.get('_traits') is None:
                raise AttributeError("Cannot assign traits before Organism.__init__() is called")
            self._traits[name] = value
            super().__setattr__(name, value.sample())
        else:
            super().__setattr__(name, value)
    
    def __add__(self, other):
        """Performs crossover between two organisms
        
        Performs crossover between two organisms by creating a new organism of the same type and crossing over each trait.
        The new organism's traits are set to the result of the crossover.
        
        Args:
            other (Organism):
                The organism to crossover with.
                
        Returns:
            Organism:
                The resulting organism of the crossover.
        
        Raises:
            TypeError:
                If the other organism is not the same type as this organism.
        """
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
        """The fitness of the organism

        The fitness of the organism is calculated by calling the fitness_function() method, and cached as a property to avoid expensive calculations.

        Returns:
            float:
                The fitness of the organism.
        """
        return self.fitness_function()
    
    def fitness_function(self):
        """The fitness function of the organism

        The fitness function of the organism, implemented by the user. A higher fitness means the organism performs better.

        Returns:
            float:
                The fitness of the organism.
        """
        raise NotImplementedError(f"Organism {type(self).__name__} must implement the \"fitness_function\" method")
    
    def mutate(self, mutation_rate):
        """Mutates the organism.

        Mutates the organism by calling the mutate() method on each individual trait.
        
        Args:
            mutation_rate (float):
                The probability that a trait will mutate (used independently for each trait).
        """
        for name, trait in self._traits.items():
            original_value = self.__dict__.get(name)
            mutated_value = trait.mutate(original_value, mutation_rate)
            self.__dict__[name] = mutated_value
    
    def evolve(self, population_size, num_generations, crossover_rate=0.8, mutation_rate=0.05, elite_rate=0.05, selection_strategy=RouletteSelector(), callbacks=[]):
        """Evolves the organism

        Evolves the organism by creating a population of the organism, and evolving the population for the specified number of generations.
        The most fit organism from the final generation is used to set the attributes of this organism.

        Args:
            population_size (int):
                The size of the population.
            num_generations (int):
                The number of generations to evolve.
            crossover_rate (float, optional):
                The probability that two organisms will crossover (default 0.8).
            mutation_rate (float, optional):
                The probability that a trait will mutate (used independently for each trait) (default 0.05).
            elite_rate (float, optional):
                The percentage of the population that will be preserved as elites (default 0.05).
            selector (Selector, optional):
                The selector to use to select parents and survivors (default RouletteSelector()).
            callbacks (list of Callback, optional):
                The list of callbacks to use (default []).

        Returns:
            HistoryCallback:
                The history of the evolution.
        """
        history = HistoryCallback()
        callbacks.append(history)

        population = Population([type(self)(*self._init_args, **self._init_kwargs) for _ in range(population_size)])
        for generation in range(num_generations):
            for callback in callbacks:
                callback.on_generation_begin(population)

            num_elites = int(population_size*elite_rate)
            new_organisms = population.most_fit(num_elites)
            while len(new_organisms) < population_size:
                if random.random() < crossover_rate:
                    parents = selection_strategy.select(population, 2)
                    child = parents[0] + parents[1]
                else:
                    child = selection_strategy.select(population, 1)[0]
                child.mutate(mutation_rate)
                new_organisms.append(child)
            population = Population(new_organisms)

            for callback in callbacks:
                callback.on_generation_end(population)
        
        best = population.most_fit()
        for name, trait in self._traits.items():
            self.__dict__[name] = best.__dict__.get(name)

        return history