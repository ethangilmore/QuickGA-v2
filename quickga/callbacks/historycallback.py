from .callback import Callback

class HistoryCallback(Callback):
    
    def __init__(self):
        self.min_fitness = []
        self.max_fitness = []
        self.avg_fitness = []
        self.fitness_heatmap = []

    def on_generation_end(self, population):
        self.min_fitness.append(population.min_fitness())
        self.max_fitness.append(population.max_fitness())
        self.avg_fitness.append(population.avg_fitness())
        self.fitness_heatmap.append(self.create_heatmap(population))

    def create_heatmap(self, population):
        heatmap = []
        for individual in population.organisms:
            heatmap.append(individual.fitness)
        return heatmap