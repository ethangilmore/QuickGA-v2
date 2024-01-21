class Trait():
    """A trait of an organism
    
    A trait of an organism. Traits are used to define the properties of an organism, and are used to perform crossover and mutation.
    These are values that are optimized during evolution, and should be the values used to determine the fitness of an organism.   
    """
    
    def __init__(self):
        """Initializes the trait."""
        if type(self) is Trait:
            raise Exception('Trait is an abstract class and cannot be instantiated directly')

    def sample(self):
        """Samples a value from the trait's sample space.

        Samples a value from the trait's sample space. This is a value used to assign to organism attributes, and should be determined randomly.

        Returns:
            A value sampled from the trait's sample space.
        """
        raise NotImplementedError(f"Trait {type(self).__name__} must implement the \"sample\" method")

    def mutate(self, value, mutation_rate):
        """Mutates a value sampled from the trait's sample space.

        Mutates a value sampled from the trait's sample space. Mutation rate is handled independently for each trait.

        Args:
            value:
                The value to mutate.
            mutation_rate:
                The mutation rate.

        Returns:
            The mutated value.
        """
        raise NotImplementedError(f"Trait {type(self).__name__} must implement the \"mutate\" method")
    
    def crossover(self, a, b):
        """Performs crossover between two values sampled from the trait's sample space.

        Performs crossover between two values sampled from the trait's sample space. The result of the crossover should be a value that is some combination of the two input values.

        Args:
            a:
                The first value to crossover.
            b:
                The second value to crossover.

        Returns:
            The result of the crossover.
        """
        raise NotImplementedError(f"Trait {type(self).__name__} must implement the \"crossover\" method")
