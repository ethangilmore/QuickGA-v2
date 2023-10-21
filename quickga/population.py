from .organism import Organism

class Population:
    
    def __init__(self, organisms):
        self.organisms = organisms
        self.max_fitness = 0
        self.most_fit = None

    @property
    def most_fit(self):
        max_fitness = 0
        most_fit = None

        for organism in self.organisms:
            if organism.fitness > max_fitness:
                max_fitness = organism.fitness
                most_fit = organism

        return most_fit
    
    @property
    def max_fitness(self):
        return self.most_fit.fitness