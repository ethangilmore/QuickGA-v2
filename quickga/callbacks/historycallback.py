from .callback import Callback

class HistoryCallback(Callback):
    
    def __init__(self):
        self.min_fitness = []
        self.max_fitness = []
        self.avg_fitness = []

    def on_generation_end(self, population):
        self.min_fitness.append(population.min_fitness())
        self.max_fitness.append(population.max_fitness())
        self.avg_fitness.append(population.avg_fitness())