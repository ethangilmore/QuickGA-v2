class Callback:
    """A callback that can track aspects of the evolution process.
    
    A callback that can track aspects of the evolution process. Callbacks are called at various points during evolution, and can be used to track the evolution process.
    """

    def on_generation_begin(self, population):
        """Called at the beginning of each generation.
        
        Args:
            population: The current population.
        """
        pass
    
    def on_generation_end(self, population):
        """Called at the end of each generation.
        
        Args:
            population: The current population.
        """
        pass