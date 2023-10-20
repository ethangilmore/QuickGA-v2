from .traits import Trait

class Organism:

    def __init__(self):
        self._traits = dict()

    def __setattr__(self, name, value):
        if isinstance(value, Trait):
            if self.__dict__.get('_traits') is None:
                raise AttributeError("Cannot assign traits before Organism.__init__() is called")
            self._traits[name] = value
            super().__setattr__(name, value.sample())
        else:
            super().__setattr__(name, value)

    def fitness(self):
        raise NotImplementedError(f"Organism {type(self).__name__} must implement the \"fitness\" method")

    @classmethod
    def evolve(cls):
        raise NotImplementedError()

