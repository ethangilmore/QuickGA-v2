class Population:
    
    def __init__(self, organisms):
        self.organisms = organisms
        self.organisms.sort(key=lambda o: o.fitness, reverse=True)

    def most_fit(self, amount=1):
        return self.organisms[0] if amount == 1 else self.organisms[:amount]
    
    def least_fit(self, amount=1):
        return self.organisms[-1] if amount == 1 else self.organisms[-amount:]
    
    def max_fitness(self):
        return self.most_fit().fitness
    
    def min_fitness(self):
        return self.least_fit().fitness
    
    def avg_fitness(self):
        return sum([o.fitness for o in self.organisms])/len(self.organisms)