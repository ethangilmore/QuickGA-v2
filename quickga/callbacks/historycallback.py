from .callback import Callback

class HistoryCallback(Callback):
    
    def __init__(self):
        self.min_fitness = []
        self.max_fitness = []
        self.avg_fitness = []

    def on_generation_end(self, population):
        fitnesses = [o.fitness for o in population.organisms]
        self.min_fitness.append(min(fitnesses))
        self.max_fitness.append(max(fitnesses))
        self.avg_fitness.append(sum(fitnesses)/len(fitnesses))