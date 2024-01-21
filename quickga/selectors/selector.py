class Selector:
    """Selects parents and survivors from a population to be used in evolution."""

    def get_survivors(self, population):
        """Returns a list of survivors from the given population.

        Returns a list of survivor organisms from the given population. These survivors are directly passed into the following generation, and are not crossed over or mutated.

        Args:
            population: The population to select survivor organisms from.

        Returns:
            list: A list of surviving organisms from the given population.
        """
        raise NotImplementedError(f"Selector {type(self).__name__} must implement the \"get_survivors\" method")

    def select_parent(self, population):
        """Returns a parent organism from the given population.
        
        Returns a parent organism from the given population. This parent organism is used to produce a child organism in the following generation.
        
        Args:
            population: The population to select a parent organism from.
            
        Returns:
            Organism: A parent organism from the given population.
        """
        raise NotImplementedError(f"Selector {type(self).__name__} must implement the \"select_parent\" method")
