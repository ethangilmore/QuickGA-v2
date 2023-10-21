class Trait():
    
    def __init__(self):
        if type(self) is Trait:
            raise Exception('Trait is an abstract class and cannot be instantiated directly')

    def sample(self):
        raise NotImplementedError(f"Trait {type(self).__name__} must implement the \"sample\" method")

    def mutate(self, value, mutation_rate):
        raise NotImplementedError(f"Trait {type(self).__name__} must implement the \"mutate\" method")
    
    def crossover(self, a, b):
        raise NotImplementedError(f"Trait {type(self).__name__} must implement the \"crossover\" method")
