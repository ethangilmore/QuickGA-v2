class SelectionStrategy:
    """Selects parents from a population to be used in evolution."""

    def select(self, population, amount):
        """Returns a list of parents from the given population.
        
        Returns a list of parent organisms from the given population. These parent organisms are used to produce child organisms in the following generation.
        
        Args:
            population:
                The population to select parent organisms from.
            amount:
                The number of parents to select.
            
        Returns:
            list: A list of parent organisms from the given population.
        """
        raise NotImplementedError(f"SelectionStrategy {type(self).__name__} must implement the \"select\" method")